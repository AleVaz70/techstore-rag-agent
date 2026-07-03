"""
Módulo encargado de cargar documentos PDF.
"""

from pathlib import Path

from pypdf import PdfReader


class PDFLoader:
    """Carga y extrae texto de archivos PDF."""

    def read_pdf(self, pdf_path: Path) -> str:
        """
        Lee un archivo PDF y devuelve todo su contenido como texto.
        """

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text