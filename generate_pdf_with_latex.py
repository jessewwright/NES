import subprocess
import os
import sys

def convert_md_to_pdf(input_md, output_pdf):
    # Step 1: Convert Markdown to LaTeX
    latex_output = input_md.replace('.md', '.tex')
    pandoc_cmd = [
        'pandoc', input_md,
        '-o', latex_output,
        '--pdf-engine=xelatex',
        '--bibliography=references.bib',
        '--citeproc',
        '--csl=apa.csl',
        '--metadata', 'link-citations=true',
        '--metadata', 'reference-section-title=References',
        '--verbose'
    ]
    
    # Step 2: Compile LaTeX to PDF
    latex_cmd = ['xelatex', '-interaction=nonstopmode', latex_output]
    
    try:
        print(f"Converting {input_md} to LaTeX...")
        subprocess.run(pandoc_cmd, check=True)
        
        print(f"Compiling {latex_output} to PDF...")
        subprocess.run(latex_cmd, check=True)
        
        # Clean up auxiliary files
        base_name = os.path.splitext(latex_output)[0]
        for ext in ['.aux', '.log', '.out']:
            if os.path.exists(base_name + ext):
                os.remove(base_name + ext)
        
        print(f"Successfully generated {output_pdf}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_pdf_with_latex.py input.md output.pdf")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found")
        sys.exit(1)
        
    success = convert_md_to_pdf(input_file, output_file)
    sys.exit(0 if success else 1)
