from src.loaders.document_loader import DocumentLoader
from src.loaders.pdf_loader import PDFLoader
from src.loaders.csv_loader import CSVLoader


def main():
    document_loader = DocumentLoader()
    pdf_loader = PDFLoader()
    csv_loader = CSVLoader() 

    pdfs = document_loader.get_pdf_files()

    print("📂 Leyendo documentos...\n")

    for pdf in pdfs:

        text = pdf_loader.read_pdf(pdf)

        print(f"📄 {pdf.name}")
        print(f"Caracteres extraídos: {len(text)}")
        print(f"Primeros 250 caracteres:\n")

        print(text[:250])

        print("-" * 60)
            

    csvs = document_loader.get_csv_files()

    print("\n📊 Leyendo archivos CSV...\n")

    for csv in csvs:

        df = csv_loader.read_csv(csv)

        print(f"📄 {csv.name}")
        print(f"Cantidad de productos: {len(df)}")

        print("\nPrimeros 5 registros:\n")

        print(df.head())

        print("-" * 60)

if __name__ == "__main__":
    main()