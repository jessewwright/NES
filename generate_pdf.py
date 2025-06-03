import sys
from weasyprint import HTML
from markdown import markdown

def convert_md_to_pdf(input_md, output_pdf):
    # Read Markdown content
    with open(input_md, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert Markdown to HTML
    html_content = markdown(md_content)
    
    # Generate full HTML document
    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
h1, h2, h3 {{ color: #2c3e50; }}
</style>
</head>
<body>
{html_content}
</body>
</html>"""
    
    # Generate PDF
    HTML(string=full_html).write_pdf(output_pdf)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_pdf.py input.md output.pdf")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_md_to_pdf(input_file, output_file)
    print(f"Successfully generated {output_file}")
