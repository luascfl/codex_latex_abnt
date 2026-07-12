#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROFILE_DIR = ROOT / "profile"
PROFILE_USER_DIR = PROFILE_DIR / "User"
MANIFEST_PATH = PROFILE_DIR / "manifest.json"
DEFAULT_CONFIG_DIR = Path.home() / ".config" / "sublime-text"
PACKAGE_NAME = "Latex Build On Window Blur"
PACKAGE_LINK_NAME = PACKAGE_NAME


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def load_sublime_json(path: Path) -> dict:
    raw = read_text(path)
    raw = re.sub(r"//.*", "", raw)
    raw = re.sub(r",(\s*[}\]])", r"\1", raw)
    return json.loads(raw)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def backup_path(path: Path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = path.with_name(f"{path.name}.bak-{timestamp}")
    path.rename(backup)
    return backup


def expected_target() -> Path:
    return ROOT


def verify_symlink(package_link: Path) -> tuple[bool, str]:
    if not package_link.exists() and not package_link.is_symlink():
        return False, f"missing: {package_link}"
    if not package_link.is_symlink():
        return False, f"not a symlink: {package_link}"
    resolved = package_link.resolve(strict=False)
    if resolved != expected_target():
        return False, f"points to {resolved}, expected {expected_target()}"
    return True, f"ok -> {resolved}"


def verify_binaries(required_binaries: list[str]) -> list[tuple[str, bool, str]]:
    rows = []
    for name in required_binaries:
        found = shutil.which(name)
        rows.append((name, bool(found), found or "not found"))
    return rows


def verify_user_files(user_dir: Path, manifest: dict) -> list[tuple[str, bool, str]]:
    results = []
    for name in manifest["user_files"]:
        source = PROFILE_USER_DIR / name
        target = user_dir / name
        if not target.exists():
            results.append((name, False, "missing in Packages/User"))
            continue
        if read_text(source) != read_text(target):
            results.append((name, False, "content differs"))
            continue
        results.append((name, True, "ok"))
    return results


def verify_installed_packages(user_dir: Path, manifest: dict) -> tuple[bool, str]:
    target = user_dir / "Package Control.sublime-settings"
    if not target.exists():
        return False, "missing Package Control.sublime-settings"
    current = load_sublime_json(target)
    expected = sorted(manifest["installed_packages"])
    actual = sorted(current.get("installed_packages", []))
    if actual != expected:
        missing = sorted(set(expected) - set(actual))
        extra = sorted(set(actual) - set(expected))
        return False, f"installed_packages mismatch; missing={missing}, extra={extra}"
    return True, "ok"

def verify_synctex_inverse_search(user_dir: Path) -> tuple[bool, str]:
    target = user_dir / "LaTeXTools.sublime-settings"
    if not target.exists():
        return False, "missing LaTeXTools.sublime-settings"

    settings = load_sublime_json(target)
    linux = settings.get("linux", {})
    viewer = settings.get("viewer", "")
    forward_sync = bool(settings.get("forward_sync", False))
    sublime_executable = linux.get("sublime_executable", "")

    problems = []
    if viewer != "evince":
        problems.append(f"viewer={viewer!r} (expected 'evince')")
    if not forward_sync:
        problems.append("forward_sync is false")
    if not sublime_executable:
        problems.append("linux.sublime_executable is empty")
    else:
        sublime_path = Path(sublime_executable)
        if not sublime_path.exists():
            problems.append(f"sublime_executable missing at {sublime_path}")
        elif not os.access(sublime_path, os.X_OK):
            problems.append(f"sublime_executable is not executable: {sublime_path}")

    if problems:
        return False, "; ".join(problems)

    return True, "evince inverse search configured for Ctrl+click back to Sublime Text"



def apply_user_files(user_dir: Path, manifest: dict) -> list[str]:
    messages = []
    user_dir.mkdir(parents=True, exist_ok=True)
    for name in manifest["user_files"]:
        source = PROFILE_USER_DIR / name
        target = user_dir / name
        if target.exists() and read_text(source) == read_text(target):
            messages.append(f"kept {target} (already in sync)")
            continue
        if target.exists():
            backup = backup_path(target)
            messages.append(f"backed up {target} -> {backup}")
        write_text(target, read_text(source))
        messages.append(f"wrote {target}")
    return messages


def apply_symlink(package_link: Path) -> list[str]:
    messages = []
    target = expected_target()
    package_link.parent.mkdir(parents=True, exist_ok=True)
    if package_link.is_symlink() and package_link.resolve(strict=False) == target:
        messages.append(f"kept symlink {package_link} -> {target}")
        return messages
    if package_link.exists() or package_link.is_symlink():
        backup = backup_path(package_link)
        messages.append(f"backed up {package_link} -> {backup}")
    package_link.symlink_to(target, target_is_directory=True)
    messages.append(f"linked {package_link} -> {target}")
    return messages


def cmd_verify(config_dir: Path) -> int:
    manifest = load_manifest()
    packages_dir = config_dir / "Packages"
    user_dir = packages_dir / "User"
    package_link = packages_dir / PACKAGE_LINK_NAME

    ok = True

    print(f"Config dir: {config_dir}")
    print(f"Bundle dir: {ROOT}")

    symlink_ok, symlink_msg = verify_symlink(package_link)
    print(f"[package-link] {'OK' if symlink_ok else 'FAIL'} {symlink_msg}")
    ok &= symlink_ok

    pkg_ok, pkg_msg = verify_installed_packages(user_dir, manifest)
    print(f"[package-control] {'OK' if pkg_ok else 'FAIL'} {pkg_msg}")
    ok &= pkg_ok

    for name, status, detail in verify_user_files(user_dir, manifest):
        print(f"[user-file] {'OK' if status else 'FAIL'} {name}: {detail}")
        ok &= status

    synctex_ok, synctex_msg = verify_synctex_inverse_search(user_dir)
    print(f"[synctex] {'OK' if synctex_ok else 'FAIL'} {synctex_msg}")
    ok &= synctex_ok
 
    for name, status, detail in verify_binaries(manifest["required_binaries"]):
        print(f"[binary] {'OK' if status else 'FAIL'} {name}: {detail}")
        ok &= status

    if ok:
        print("Verification passed.")
        return 0
    print("Verification failed.")
    return 1


def cmd_apply(config_dir: Path) -> int:
    manifest = load_manifest()
    packages_dir = config_dir / "Packages"
    user_dir = packages_dir / "User"
    package_link = packages_dir / PACKAGE_LINK_NAME

    messages = []
    messages.extend(apply_user_files(user_dir, manifest))
    messages.extend(apply_symlink(package_link))

    for msg in messages:
        print(msg)

    print("Apply completed. Restart Sublime Text or run Package Control's package synchronization if needed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify or apply the bundled Sublime Text LaTeX profile.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--verify", action="store_true", help="check the current Sublime setup against this bundle")
    mode.add_argument("--apply", action="store_true", help="install this bundle into the current Sublime setup")
    parser.add_argument("--config-dir", type=Path, default=DEFAULT_CONFIG_DIR, help="override the Sublime Text config dir")
    args = parser.parse_args()

    if args.verify:
        return cmd_verify(args.config_dir)
    return cmd_apply(args.config_dir)


if __name__ == "__main__":
    raise SystemExit(main())
