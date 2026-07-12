# Development Workflow

O fluxo diário neste repositório começa pela leitura do contrato local (`AGENTS.md` e `prompt_mestre_abnt-latex.txt`), passa por edições pequenas e termina em compilação LaTeX e revisão visual. Como o repositório agrega vários diretórios `tmp_*`, cada mudança deve ser tratada no menor escopo possível.

## Branching & releases
- Branch principal observada: `main`.
- O repositório possui `origin`, então fechamentos relevantes devem terminar em commit.
- Quando houver submódulos alterados, valide o estado deles antes de publicar o conjunto.
- Não há pipeline de release automatizada; a publicação é operacional e pode ser mediada por `create_and_push_repo.sh`.

## Local development
- Materializar submódulos: `git submodule update --init --recursive`
- Compilar template raiz: `latexmk -xelatex -interaction=nonstopmode template_resenha.tex`
- Limpar auxiliares do template raiz: `latexmk -c template_resenha.tex`
- Repetir a compilação dentro de cada diretório `tmp_*` tocado no ciclo
- Instalar suporte a binários grandes: `git lfs install --skip-repo`

## Code review expectations
Revisão aqui significa duas coisas: respeitar o contrato ABNT e não quebrar os derivados. Toda alteração no template raiz deve confirmar engine XeLaTeX, classe `abntex2`, macro `utorcite`, margens, espaçamento, convenções de headings e referências. Também é esperado evitar duplicar convenções já consolidadas no prompt mestre.

## Onboarding tasks
Para entrar rápido no projeto:
1. Entenda a diferença entre template raiz e projetos `tmp_*`.
2. Compile o template raiz uma vez antes de editar.
3. Inspecione um subprojeto já concluído para ver o padrão de saída esperado.
4. Atualize `.context/docs/planning_gsd/STATE.md` sempre que um ciclo relevante for fechado.
