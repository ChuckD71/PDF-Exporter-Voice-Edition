
from fpdf import FPDF
import datetime
import os

class PDFExporter:
    def __init__(self, title="AI Export", author="AIDIVISION"):
        self.title = title
        self.author = author
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)

    def add_title(self):
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(200, 10, txt=self.title, ln=True, align='C')
        self.pdf.set_font("Arial", size=12)
        self.pdf.ln(10)

    def add_text(self, text):
        self.pdf.multi_cell(0, 10, text)

    def save(self, filename="export.pdf"):
        export_path = os.path.join(os.getcwd(), filename)
        self.pdf.output(export_path)
        print(f"PDF saved to: {export_path}")
        return export_path

# Example usage:
if __name__ == "__main__":
    content = "This is a sample export from Nyx or VSO_Kyuss. Customize as needed."
    exporter = PDFExporter(title="VSO_Kyuss Claim Summary")
    exporter.add_title()
    exporter.add_text(content)
    exporter.save("vso_claim_export.pdf")
