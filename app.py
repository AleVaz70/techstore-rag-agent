from src.loaders.document_loader import DocumentLoader
from src.loaders.pdf_loader import PDFLoader


def main():
    document_loader = DocumentLoader()
    pdf_loader = PDFLoader()

    pdfs = document_loader.get_pdf_files()

    print("📂 Leyendo documentos...\n")

    for pdf in pdfs:

        text = pdf_loader.read_pdf(pdf)

        print(f"📄 {pdf.name}")
        print(f"Caracteres extraídos: {len(text)}")
        print(f"Primeros 250 caracteres:\n")

        print(text[:250])

        print("-" * 60)


if __name__ == "__main__":
    main()