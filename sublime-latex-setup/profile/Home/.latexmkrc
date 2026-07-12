# Força a geração de SyncTeX em qualquer build local (terminal ou Sublime)
$xelatex = 'xelatex -interaction=nonstopmode -synctex=1 %O %S';
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';
$lualatex = 'lualatex -interaction=nonstopmode -synctex=1 %O %S';
