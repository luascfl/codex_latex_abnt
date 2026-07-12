# STATE

## Data de referência
2026-07-12

## Fase ativa
Concluído

## Milestone ativo
**M2, Auditoria do template raiz**

### Objetivo do milestone
Validar o primeiro drift de alto impacto entre `template_resenha.tex` e `prompt_mestre_abnt-latex.txt`, corrigindo o contrato de citação `\autorcite` sem quebrar a compatibilidade ABNT nem a compilação do template.

### Dependências
- `US-CTX-001` concluída no ciclo anterior.
- `template_resenha.tex` e `prompt_mestre_abnt-latex.txt` presentes e legíveis.
- Build XeLaTeX funcional no ambiente local.

## Story ativa no Ralph
`US-ABNT-002` concluída.

## Próxima ação recomendada
Iniciar `US-OPS-003`, revisando `create_and_push_repo.sh`, `GITHUB_TOKEN.txt` e a política de submódulos para reduzir risco operacional de publicação.

## Evidências atuais
- O drift foi confirmado entre `prompt_mestre_abnt-latex.txt` e `template_resenha.tex`: o prompt exige que `\autorcite*{}` gere citação textual `Autor (ano, p.)`, mas o template estava retornando apenas o ano.
- `template_resenha.tex` foi corrigido para alinhar a forma estrelada de `\autorcite` ao contrato do prompt mestre.
- A frase de exemplo em `2.1 Primeiro eixo de análise` foi ajustada para usar `\autorcite*{autor_ano}` sem parênteses externos, preservando a semântica textual da macro.
- `latexmk -xelatex -interaction=nonstopmode template_resenha.tex` executou com sucesso em duas passadas após a correção.
- A extração textual de `template_resenha.pdf` confirmou as duas formas esperadas: `Contextualize ... (SOBRENOME, Ano).` na forma parentética e `Descreva ... SOBRENOME (Ano) ...` na forma textual.
- Avisos remanescentes, ainda fora do escopo desta story: recomendação do memoir contra `titlesec`, não sobrescrita de `template_resenha.bib` e `template_resenha.toc` por `filecontents*`, um overfull hbox na folha de rosto, warning `Object @page.1 already defined` no `xdvipdfmx` e warning BibTeX sobre `abnt-show-options=none`.
- `.context/workflow/status.yaml` registra o ciclo SMALL `template-audit-us-abnt-002` com fases P, E e V concluídas.
