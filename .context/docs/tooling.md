# Tooling & Productivity Guide

O ferramental do repositório é pequeno e objetivo. O ganho de produtividade vem menos de framework e mais de repetir um fluxo estável de edição, compilação, revisão e publicação.

## Required tooling
- **XeLaTeX / latexmk** — compilação principal do template e dos subprojetos.
- **BibTeX** — resolução de referências bibliográficas.
- **Git** — versionamento do repositório raiz e dos submódulos.
- **Git LFS** — armazenamento de PDFs e binários grandes conforme `.gitattributes`.
- **Shell POSIX** — execução de `create_and_push_repo.sh` e comandos auxiliares.

## Recommended automation
O principal atalho operacional é `create_and_push_repo.sh`, usado para coordenar push do repositório raiz e dos submódulos com o token local. Para desenvolvimento, `latexmk` já cobre o ciclo incremental de compilação. O ideal é editar pouco, compilar cedo e evitar lotes grandes de alteração no template raiz.

## IDE / editor setup
- Editor com suporte a LaTeX e destaque para UTF-8.
- Visualizador de PDF para checagem rápida da saída.
- Integração Git suficiente para enxergar mudanças em arquivos de texto e binários.

## Productivity tips
- Mantenha os ativos relativos ao lado do `.tex` que os consome.
- Trate cada diretório `tmp_*` como um projeto separado ao investigar problemas.
- Não confie apenas no mapa automático de código para este repositório; leia `template_resenha.tex` e o prompt mestre diretamente.
