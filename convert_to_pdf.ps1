# Convert Markdown to LaTeX
pandoc draft.md -o temp.tex --biblatex --standalone

# Compile LaTeX to PDF
pdflatex temp.tex

# Run bibtex if references exist
if (Test-Path "temp.bcf") {
    biber temp
    pdflatex temp.tex
    pdflatex temp.tex
}

# Clean up intermediate files
$extensions = @("aux", "bbl", "bcf", "blg", "log", "out", "run.xml", "toc")
foreach ($ext in $extensions) {
    if (Test-Path "temp.$ext") {
        Remove-Item "temp.$ext"
    }
}

# Rename the final PDF
if (Test-Path "temp.pdf") {
    Move-Item -Path "temp.pdf" -Destination "draft_final.pdf" -Force
    Write-Host "Conversion complete: draft_final.pdf"
} else {
    Write-Host "Error: PDF generation failed. Check temp.log for details."
}
