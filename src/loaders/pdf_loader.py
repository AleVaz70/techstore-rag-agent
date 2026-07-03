"""
Módulo encargado de cargar documentos PDF.
"""

from pathlib import Path

from pypdf import PdfReader

from src.models.document import Document


class PDFLoader:
    """Carga y extrae texto de archivos PDF."""

    def read_pdf(self, pdf_path: Path) -> Document:
        """
        Lee un archivo PDF y devuelve un objeto Document.
        """

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return Document(
            name=pdf_path.name,
            content=text,
            doc_type="pdf"
        )