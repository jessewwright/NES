@echo off
echo Starting Pandoc...
pandoc --version
echo.
pandoc draft.md -o draft.pdf --pdf-engine=xelatex --bibliography=references.bib --citeproc --csl=apa.csl --metadata link-citations=true --metadata reference-section-title=References --verbose
echo.
echo Pandoc finished with error level %ERRORLEVEL%
pause
