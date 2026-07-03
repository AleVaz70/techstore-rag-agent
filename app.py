from src.loaders.document_loader import DocumentLoader


def main():
    loader = DocumentLoader()

    pdfs = loader.get_pdf_files()
    csvs = loader.get_csv_files()

    print("📂 Buscando documentos...\n")

    for pdf in pdfs:
        print(f"✅ PDF: {pdf.name}")

    for csv in csvs:
        print(f"✅ CSV: {csv.name}")

    print(f"\nTotal de documentos encontrados: {len(pdfs) + len(csvs)}")


if __name__ == "__main__":
    main()