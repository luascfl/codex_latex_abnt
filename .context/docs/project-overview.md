# Project Overview

`codex_latex_abnt` é um repositório-base para produção de trabalhos acadêmicos em XeLaTeX com foco em ABNT. Ele combina um template raiz reutilizável, um prompt mestre que fixa regras tipográficas e uma coleção de diretórios `tmp_*` que funcionam como projetos derivados ou estudos independentes.

O benefício principal é manter um ponto de verdade único para configuração editorial e, ao mesmo tempo, permitir que trabalhos específicos evoluam em submódulos sem contaminar o template raiz.

> **Detailed analysis**: o arquivo [`codebase-map.json`](./codebase-map.json) existe como suporte, mas a leitura manual de `template_resenha.tex`, `prompt_mestre_abnt-latex.txt` e `AGENTS.md` continua sendo a forma mais fiel de entender este repositório.

## Quick facts
- Root: `/home/lucas/Downloads/codex_latex_abnt`
- Linguagens dominantes na prática: LaTeX, BibTeX, Markdown e shell script
- Entradas principais: `template_resenha.tex`, `prompt_mestre_abnt-latex.txt`, `create_and_push_repo.sh`
- Estrutura derivada: múltiplos diretórios `tmp_*`, vários deles configurados como submódulos Git
- Análise estrutural auxiliar: [`codebase-map.json`](./codebase-map.json)

## Entry points
- `template_resenha.tex` — template raiz para novos trabalhos ABNT.
- `prompt_mestre_abnt-latex.txt` — contrato editorial e técnico para gerar ou revisar documentos.
- `AGENTS.md` — regras locais do repositório para agentes e mantenedores.
- `create_and_push_repo.sh` — automação de publicação do repositório raiz e dos submódulos.

## Key exports
- Macros editáveis do template: `
omeinstituicao`, `
omedepartamento`, `
omecurso`, `
omeautor`, `
omedisciplina`, `
omeorientador`, `	ituloprincipal`, `	itulocomplemento`, `	ipodocumento`, `\logoinstituicao`.
- Macro de citação reutilizável: `utorcite`.
- Convenções de exibição: chaves `\mostrar...` para capa, folha de rosto, resumo, abstract, sumário e texto.

## File structure & code organization
- `template_resenha.tex` — template central e demonstração compilável.
- `template_resenha.bib` — base bibliográfica raiz do template.
- `abntex2-alf-local.bst` — estilo bibliográfico fixo do projeto.
- `prompt_mestre_abnt-latex.txt` — especificação textual e tipográfica.
- `create_and_push_repo.sh` — automação operacional de Git e submódulos.
- `tmp_*` — projetos derivados, materiais-fonte, apresentações e experimentos acadêmicos.
- `.context/` — contexto operacional do projeto para planejamento, execução incremental e workflow.

## Technology stack summary
O stack é propositalmente simples: XeLaTeX com classe `abntex2`, BibTeX para referências, shell script para automação e Git submodules para isolar projetos derivados. Não há aplicação de runtime, servidor ou biblioteca distribuível. O contrato de qualidade está na compilação limpa, na fidelidade visual ao padrão ABNT e na preservação da estrutura documental entre raiz e subprojetos.

## Development tools overview
O trabalho diário gira em torno de `latexmk -xelatex -interaction=nonstopmode`, inspeção visual de PDF, atualização de submódulos via Git e uso do script `create_and_push_repo.sh` quando houver publicação coordenada.

## Getting started checklist
1. Rode `git submodule update --init --recursive` para materializar os projetos derivados.
2. Leia `AGENTS.md` e `prompt_mestre_abnt-latex.txt` antes de alterar o template raiz.
3. Compile o template com `latexmk -xelatex -interaction=nonstopmode template_resenha.tex`.
4. Compare a saída gerada com `template_resenha.pdf` e valide capa, sumário, citações e referências.
5. Consulte `development-workflow.md` e `testing-strategy.md` antes de fechar o ciclo.

## Next steps
O próximo uso mais valioso do repositório é manter o template raiz e o prompt mestre alinhados, reduzindo drift entre a especificação editorial e os projetos derivados.
