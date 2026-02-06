from pypdf import PdfReader
import sys

def extract_text(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        
        # Write to a file so I can read it easily
        with open('extracted_text.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Text extraction successful.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_text(r"c:\Users\LENOVO\Desktop\REPOSITORIOS\RecreaWEB2\MATERIALES\Textos.pdf")
