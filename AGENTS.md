# Repository Guidelines

## Purpose for Agents
AGENTS.md is a predictable entry point for coding agents. Use it to understand how to work in this ABNT-focused LaTeX repo and how to apply the local prompt (`prompt_mestre_abnt-latex.txt`) when generating content.

## Project Structure & Modules
- Root LaTeX template: `template_resenha.tex` with companions `template_resenha.bib`, `abntex2-alf-local.bst`, and `logo_uneb.png`.
- Submodules: each `tmp_*` directory is an independent LaTeX project; keep them synced with `git submodule update --init --recursive` before editing and before push.
- Automation: `create_and_push_repo.sh` handles pushing root + submodules using `GITHUB_TOKEN.txt`. Prefer it to manual remote setup.
- Large binaries: `.gitattributes` routes heavy PDFs through Git LFS—store new large assets the same way.

## Build & Test Commands
- Compile: `latexmk -xelatex -interaction=nonstopmode template_resenha.tex` (rerun to settle citations).
- Clean aux files: `latexmk -c template_resenha.tex`.
- Submodules: run the same `latexmk` inside each `tmp_*` you touch.
- Setup helpers: `git lfs install --skip-repo` and `git submodule update --init --recursive`.

## LaTeX Style & Naming
- Engine/class: XeLaTeX only, `abntex2` (oneside, 12pt), A4 with 3/3/2/2 cm margins, `fontspec` + Arial (per prompt mestre).
- Paragraphs: 1.25 cm indent, 1.5 spacing; long quotes in 10pt with 4 cm indent.
- Headings: chapters in uppercase, sections sentence case; use existing metadata commands (`\nomeinstituicao`, `\tituloprincipal`, etc.) in Portuguese.
- Citations: `abntex2cite` with `abnt-emphasize=bf`; keep `abntex2-alf-local.bst` as style.
- Estilo textual: redija em português claro e acessível, evitando jargão desnecessário e frases labirínticas; priorize clareza de raciocínio, sem usar travessões ou em dashes no lugar de vírgula; use sentence case quando possível, sem maiúsculas estilísticas.
- Palavras-chave: no resumo/abstract, inicie cada termo com inicial maiúscula e separe com ponto final, mantendo recuo zero.
- Persona: escreva na perspectiva de estudante de Psicologia (Lucas Camilo Carvalho, Salvador-BA; PT primário, EN secundário) quando metadados pessoais forem relevantes.

## Using prompt_mestre_abnt-latex
- When generating or modifying LaTeX, follow `prompt_mestre_abnt-latex.txt` as the authoritative spec (XeLaTeX, margins, spacing, title/page rules, `\autorcite` macro, pre-textual formatting, TOC stub via `filecontents*`).
- Keep new macros near the existing metadata block; avoid diverging from the provided `autorcite` signature and numbering/page rules.

## Testing & Validation
- Passing build = `latexmk` finishes cleanly with minimal warnings; rebuild bibliography when `.bib` changes.
- Visually compare PDFs to `template_resenha.pdf` for cover, summary, and citation formatting; ensure image paths remain relative.

## Commit & PR Guidelines
- Prefer clear, imperative commit subjects (e.g., `adjust cover spacing`, `fix citation indent`) instead of generic “push.”
- In PRs, describe what changed and why, mention affected files/submodules, and note any remaining LaTeX warnings. If submodules changed, list the `tmp_*` names. 
