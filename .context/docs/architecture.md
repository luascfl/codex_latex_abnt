# Architecture Notes

A arquitetura deste repositório é documental, não orientada a runtime. O centro do sistema é um template raiz em LaTeX, cercado por arquivos estáveis de estilo, um prompt mestre que define o contrato de saída e uma borda de projetos `tmp_*` que reutilizam ou adaptam esse núcleo.

## System architecture overview
A topologia é de um repositório-base com derivados. O fluxo principal parte de um arquivo `.tex` editável, passa por XeLaTeX e BibTeX e resulta em artefatos PDF e auxiliares (`.aux`, `.bbl`, `.toc`, `.log`, `.fdb_latexmk`, `.fls`). Em paralelo, submódulos `tmp_*` preservam trabalhos independentes sem fundir suas mudanças no template raiz.

## Architectural layers
- **Núcleo editorial**: `template_resenha.tex`, `template_resenha.bib`, `abntex2-alf-local.bst`, `logo_uneb.png`.
- **Especificação**: `prompt_mestre_abnt-latex.txt` e `AGENTS.md`.
- **Automação operacional**: `create_and_push_repo.sh`, `.gitmodules`, `.gitattributes`.
- **Projetos derivados**: diretórios `tmp_*`, vários com histórico e build próprios.
- **Contexto de execução**: `.context/docs/`, `.context/docs/planning_gsd/`, `.context/prd_ralph/`, `.context/workflow/`.

> Veja [`codebase-map.json`](./codebase-map.json) apenas como apoio. O mapa automático não captura bem a estrutura LaTeX e os submódulos deste repositório.

## Detected design patterns
| Pattern | Confidence | Locations | Description |
| --- | --- | --- | --- |
| Single source of truth | High | `template_resenha.tex`, `prompt_mestre_abnt-latex.txt` | O template e o prompt mestre centralizam regras tipográficas e editoriais. |
| Template derivative projects | High | diretórios `tmp_*` | Projetos derivados reaproveitam a base sem misturar necessariamente o conteúdo final no template raiz. |
| Asset sidecar files | High | `template_resenha.bib`, `abntex2-alf-local.bst`, `logo_uneb.png` | O documento principal depende de arquivos estáveis e relativos no mesmo diretório. |
| Scripted publish workflow | Medium | `create_and_push_repo.sh`, `.gitmodules` | O processo de publicação coordena repositório raiz e submódulos. |

## Entry points
- `template_resenha.tex`
- `prompt_mestre_abnt-latex.txt`
- `create_and_push_repo.sh`
- `AGENTS.md`

## Public API
| Symbol | Type | Location |
| --- | --- | --- |
| `utorcite` | LaTeX macro | `template_resenha.tex` |
| `
omeinstituicao` e afins | LaTeX metadata macros | `template_resenha.tex` |
| `\mostrar...` | LaTeX boolean switches | `template_resenha.tex` |

## Internal system boundaries
A fronteira mais importante separa o template raiz dos diretórios `tmp_*`. O template deve permanecer genérico e reutilizável. Já os derivados podem carregar conteúdo acadêmico específico, materiais-fonte, PDFs grandes e ajustes locais.

## External service dependencies
- **GitHub** — hospedagem do repositório e dos submódulos.
- **Git LFS** — versionamento de binários grandes, principalmente PDFs e ativos pesados.

## Key decisions & trade-offs
O projeto privilegia previsibilidade sobre abstração. Em vez de um gerador complexo ou DSL própria, o fluxo usa LaTeX explícito e arquivos auxiliares visíveis. Isso reduz mágica e facilita depuração, mas exige disciplina para não deixar os derivados divergir demais do template.

## Risks & constraints
- O analisador automático de contexto não entende bem LaTeX como linguagem principal.
- PDFs e ativos grandes podem poluir diffs se Git LFS não for seguido.
- Mudanças no template raiz podem quebrar projetos derivados se o contrato tipográfico mudar sem validação.

## Top directories snapshot
- `tmp_*` — coleção principal de trabalhos derivados e materiais acadêmicos.
- `.context/` — contexto de planejamento e execução.
- raiz do repositório — template, prompt mestre, automação e ativos compartilhados.

## Related resources
- [Project Overview](./project-overview.md)
- [Data Flow & Integrations](./data-flow.md)
- [Development Workflow](./development-workflow.md)
