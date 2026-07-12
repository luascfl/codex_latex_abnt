# PROJECT

## Nome
Base ABNT em XeLaTeX com template raiz e projetos derivados

## Objetivo
Manter `codex_latex_abnt` como fonte de verdade confiável para produção acadêmica em ABNT, preservando um template raiz estável, um prompt mestre consistente e contexto canônico suficiente para execução incremental por stories.

## Escopo
- Contexto operacional em `.context/docs`, `.context/docs/planning_gsd`, `.context/prd_ralph` e `.context/workflow`.
- Template raiz `template_resenha.tex` e seus ativos compartilhados.
- Automação de publicação do repositório raiz e dos submódulos.
- Coordenação dos diretórios `tmp_*` apenas quando forem tocados em um ciclo específico.

## Fora de escopo
- Reescrever todos os projetos `tmp_*` para um único padrão em um único ciclo.
- Trocar XeLaTeX, `abntex2` ou `abntex2-alf-local.bst`.
- Gerar `README.md` da raiz automaticamente sem curadoria humana.

## Milestones
1. **M1, Fundação do contexto canônico**
   - Dependências: nenhuma
   - Entregas: `.context` inicializado, planejamento GSD criado, PRD inicial criado, workflow ativo e documentação mínima preenchida.
2. **M2, Auditoria do template raiz**
   - Dependências: M1
   - Entregas: mapeamento dos principais drifts entre `template_resenha.tex` e `prompt_mestre_abnt-latex.txt`, com a primeira correção de alto impacto validada por compilação.
3. **M3, Endurecimento do fluxo operacional**
   - Dependências: M2
   - Entregas: revisão do script `create_and_push_repo.sh`, política de submódulos e critérios de fechamento por ciclo.
4. **M4, Evolução orientada a stories derivadas**
   - Dependências: M2
   - Entregas: melhorias incrementais no template e nos derivados, sempre uma story por ciclo com evidência técnica.
