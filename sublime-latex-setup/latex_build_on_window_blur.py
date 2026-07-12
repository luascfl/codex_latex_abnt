import time
import sublime
import sublime_plugin


SETTINGS_FILE = "LatexBuildOnWindowBlur.sublime-settings"
DIRTY_KEY = "latex_build_on_window_blur.dirty_since_build"


def is_tex_view(view, settings):
    if not view:
        return False

    selector = settings.get("selector", "text.tex.latex")
    extensions = settings.get("extensions", [".tex"])
    file_name = view.file_name() or ""
    return view.match_selector(0, selector) or any(
        file_name.endswith(ext) for ext in extensions
    )




class LatexBuildOnWindowBlur(sublime_plugin.EventListener):
    _last_build_at = 0

    def _handle_blur(self, window, view):
        settings = sublime.load_settings(SETTINGS_FILE)
        if not settings.get("enabled", True):
            return
        if not window or not view or not is_tex_view(view, settings):
            return

        # Build only after actual edits since the previous build. This prevents
        # rebuilding every time the user clicks Evince or another application.
        if not view.settings().get(DIRTY_KEY, False):
            return

        now = time.monotonic()
        if now - self._last_build_at < 1.0:
            return
        self._last_build_at = now

        delay_ms = int(settings.get("build_delay_ms", 300))
        save_all = bool(settings.get("save_all_dirty_views", True))

        views = window.views() if save_all else [view]
        for candidate in views:
            if candidate.is_dirty() and not candidate.is_scratch():
                candidate.run_command("save")

        def run_build():
            view.settings().erase(DIRTY_KEY)
            window.run_command("build")

        sublime.set_timeout(run_build, delay_ms)

    def on_modified(self, view):
        settings = sublime.load_settings(SETTINGS_FILE)
        if settings.get("enabled", True) and is_tex_view(view, settings):
            view.settings().set(DIRTY_KEY, True)

    def on_deactivated_window(self, window):
        self._handle_blur(window, window.active_view() if window else None)

    def on_deactivated(self, view):
        # Some Sublime Text builds do not reliably fire on_deactivated_window
        # when focus moves to another application. View deactivation does fire,
        # and still does not run on Ctrl+S.
        self._handle_blur(view.window() if view else None, view)
