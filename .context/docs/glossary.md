# Glossary & Domain Concepts

Este repositório usa um vocabulário muito mais editorial do que programático. Os termos abaixo ajudam a distinguir o núcleo do template, os derivados e o fluxo de publicação.

## Type definitions
- Não há tipos exportados em linguagem de programação tradicional no repositório raiz.
- As entidades reutilizáveis são macros LaTeX e convenções documentais.

## Enumerations
- Não há enums formais no repositório raiz.
- As escolhas recorrentes aparecem como convenções fixas, por exemplo: engine XeLaTeX, classe `abntex2`, citação autor-data e uso de `abntex2-alf-local.bst`.

## Core terms
- **Template raiz** — `template_resenha.tex`, base genérica para novos trabalhos.
- **Prompt mestre** — `prompt_mestre_abnt-latex.txt`, especificação normativa e estilística.
- **Projeto derivado** — qualquer diretório `tmp_*` com material acadêmico próprio.
- **Submódulo** — diretório versionado separadamente e vinculado por `.gitmodules`.
- **Contexto canônico** — conjunto formado por `AGENTS.md`, `.context/docs`, `.context/docs/planning_gsd`, `.context/prd_ralph` e `.context/workflow`.
- **Story Ralph** — unidade incremental executável dentro do PRD canônico.
- **Milestone GSD** — agrupador macro de stories, dependências e objetivos.

## Acronyms & abbreviations
- **ABNT** — Associação Brasileira de Normas Técnicas.
- **PRD** — Product Requirements Document, aqui usado como backlog executável.
- **GSD** — camada de planejamento macro do projeto.
- **PREVC** — workflow de fases Plan, Review, Execute, Verify, Complete.
- **LFS** — Large File Storage do Git.

## Personas / actors
- **Autor acadêmico** — usa o template para produzir resenhas, fichamentos, apresentações ou relatórios.
- **Mantenedor do template** — cuida da estabilidade editorial do repositório raiz.
- **Agente de automação** — altera contexto, verifica consistência e executa ciclos incrementais por story.

## Domain rules & invariants
- XeLaTeX é obrigatório.
- O estilo bibliográfico raiz é `abntex2-alf-local.bst`.
- O template deve permanecer reutilizável e separado do conteúdo específico dos diretórios `tmp_*`.
- O estilo textual deve ser claro, em português, sem academicismo desnecessário e sem usar travessão como substituto de vírgula.
