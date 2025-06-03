@echo off
pandoc draft.md -o draft_direct.pdf --pdf-engine=xelatex --bibliography=references.bib --citeproc --csl=apa.csl --metadata link-citations=true --metadata reference-section-title=References --verbose
