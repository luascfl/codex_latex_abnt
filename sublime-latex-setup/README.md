# Latex Build On Window Blur

Este diretório agora funciona como duas coisas ao mesmo tempo:

1. pacote do Sublime Text para build automático ao perder foco
2. bundle da configuração LaTeX atual do Sublime, com verificação e aplicação por um único script com flags

## O que está incluído
- o plugin `latex_build_on_window_blur.py`
- os arquivos atuais de `Packages/User` relevantes para o fluxo LaTeX
- uma configuração explícita de `LaTeXTools.sublime-settings` com SyncTeX via Evince
- um manifesto com a lista de plugins esperados do Sublime

## Script único
Use:

```bash
python3 sublime_setup.py --verify
python3 sublime_setup.py --apply
```

Flags disponíveis:
- `--verify`: confere symlink do pacote, arquivos de `Packages/User`, plugins esperados e binários `evince`, `subl` e `synctex`
- `--apply`: copia os arquivos do bundle para `~/.config/sublime-text/Packages/User` e recria o symlink do pacote para esta pasta
- `--config-dir <caminho>`: sobrescreve o diretório padrão do Sublime Text

## SyncTeX incluído
O bundle fixa estes pontos do LaTeXTools:
- `viewer: evince`
- `forward_sync: true`
- `keep_focus: true`
- `linux.sublime_executable: /opt/sublime_text/sublime_text`
- `linux.sync_wait: 1.5`

Com isso, o fluxo esperado fica explícito:
- build e forward sync pelo LaTeXTools
- Ctrl+click no texto do Evince para voltar ao trecho equivalente no Sublime Text

## Observação importante
Na leitura do ambiente atual, o symlink em `~/.config/sublime-text/Packages/Latex Build On Window Blur` aponta para `/home/lucas/Downloads/sublime-latex-build-on-window-blur`, que hoje está ausente. O modo `--apply` corrige isso, apontando o pacote para esta pasta.
