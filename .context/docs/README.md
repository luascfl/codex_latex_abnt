# Documentation Index

Este índice concentra o contexto canônico do repositório `codex_latex_abnt`.

## Core guides
- [Project Overview](./project-overview.md)
- [Architecture Notes](./architecture.md)
- [Development Workflow](./development-workflow.md)
- [Testing Strategy](./testing-strategy.md)
- [Glossary & Domain Concepts](./glossary.md)
- [Data Flow & Integrations](./data-flow.md)
- [Security & Compliance Notes](./security.md)
- [Tooling & Productivity Guide](./tooling.md)

## Repository snapshot
- `template_resenha.tex` é o template raiz em XeLaTeX e ABNT.
- `template_resenha.bib`, `abntex2-alf-local.bst` e `logo_uneb.png` compõem os insumos estáveis do template.
- `prompt_mestre_abnt-latex.txt` é a especificação editorial e tipográfica principal.
- `create_and_push_repo.sh` concentra a automação de push do repositório raiz e dos submódulos.
- Os diretórios `tmp_*` funcionam como projetos independentes, cada um com seu próprio conteúdo acadêmico e, em muitos casos, sua própria compilação LaTeX.
- `.context/docs/planning_gsd/` guarda milestones e estado executivo.
- `.context/prd_ralph/` guarda o backlog executável por story.
- `.context/workflow/` guarda o estado do workflow PREVC.

## Context caveats
- O `codebase-map.json` atual foi gerado a partir de um analisador orientado a código e subrepresenta a natureza LaTeX do repositório. Use-o como artefato auxiliar, não como inventário fiel.
- Este projeto não possui `README.md` na raiz no momento. Qualquer README futuro deve ser curado manualmente.

## Document map
| Guide | File | Focus |
| --- | --- | --- |
| Project Overview | `project-overview.md` | propósito, estrutura raiz e primeiros passos |
| Architecture Notes | `architecture.md` | camadas lógicas do repositório e trade-offs |
| Development Workflow | `development-workflow.md` | fluxo de edição, build e revisão |
| Testing Strategy | `testing-strategy.md` | compilação, inspeção visual e quality gates |
| Glossary & Domain Concepts | `glossary.md` | termos de domínio LaTeX/ABNT usados no projeto |
| Data Flow & Integrations | `data-flow.md` | fluxo de arquivos entre fonte, build e artefatos |
| Security & Compliance Notes | `security.md` | segredos locais e cuidado com ativos acadêmicos |
| Tooling & Productivity Guide | `tooling.md` | comandos, ferramentas e automações essenciais |
