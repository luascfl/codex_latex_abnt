# Testing Strategy

A estratégia de testes aqui é centrada em comportamento observável do documento: compilar sem erro fatal, conferir o log e validar o PDF gerado. Como o repositório não expõe API nem serviço, o equivalente ao teste automatizado é a execução disciplinada do build LaTeX.

## Test types
- **Build validation**: `latexmk -xelatex -interaction=nonstopmode template_resenha.tex` no template raiz.
- **Repeated build**: segunda passada para estabilizar referências, sumário e citações.
- **Subproject build**: repetir `latexmk` dentro de cada `tmp_*` tocado no ciclo.
- **Visual inspection**: comparar o PDF gerado com o padrão esperado para capa, headings, citações, sumário e referências.

## Running tests
- Template raiz: `latexmk -xelatex -interaction=nonstopmode template_resenha.tex`
- Segunda passada do template raiz: repetir o mesmo comando
- Limpeza opcional: `latexmk -c template_resenha.tex`
- Subprojetos tocados: executar o mesmo `latexmk` no diretório correspondente

## Quality gates
- O build deve finalizar sem erro fatal.
- Referências e sumário devem estabilizar após a recompilação.
- Ativos relativos, como `logo_uneb.png` e `.bst`, devem ser resolvidos sem quebra.
- Qualquer mudança relevante no template raiz pede inspeção visual do PDF resultante.
- O contexto operacional deve ser atualizado em `.context/docs/planning_gsd/STATE.md` ao fim do ciclo.

## Troubleshooting
Os problemas mais comuns são arquivo relativo ausente, macro quebrada, citação inválida e `.toc` inconsistente. Quando houver comportamento estranho de `filecontents*`, revise também a política de overwrite dos auxiliares antes de assumir erro no conteúdo.
