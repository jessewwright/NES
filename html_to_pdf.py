from weasyprint import HTML

# Convert HTML to PDF
HTML('draft.html').write_pdf('draft_final.pdf')
print("PDF created successfully: draft_final.pdf")
