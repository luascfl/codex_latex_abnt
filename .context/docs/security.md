# Security & Compliance Notes

A superfície de segurança deste repositório é simples, mas sensível: o risco principal não está em autenticação de usuário final, e sim em segredos locais e publicação indevida de materiais acadêmicos ou binários pesados.

## Authentication & authorization
Não existe sistema de autenticação da aplicação porque não há aplicação em runtime. O controle relevante é operacional: acesso ao repositório Git, aos submódulos e a qualquer token usado pelo fluxo de publicação.

## Secrets & sensitive data
- `GITHUB_TOKEN.txt` é sensível e não deve ser exposto em documentação, screenshots ou logs.
- PDFs, relatórios e materiais de aula podem conter dados acadêmicos ou pessoais. Trate-os com revisão humana antes de publicar.
- Caminhos relativos para imagens e bibliografias devem ser preservados para evitar cópias desnecessárias de ativos.

## Compliance & policies
- Respeitar o padrão ABNT definido no prompt mestre faz parte do contrato de qualidade do projeto.
- Arquivos grandes devem seguir a política já refletida em `.gitattributes` e Git LFS.
- O fechamento de ciclos relevantes em repositório com remoto pede commit.

## Incident response
Se um segredo local ou ativo sensível for versionado por engano:
1. interrompa a publicação;
2. remova o arquivo ou regrave o histórico conforme a gravidade;
3. rotacione o token comprometido;
4. revise `create_and_push_repo.sh` e o staging antes de tentar novo push.
