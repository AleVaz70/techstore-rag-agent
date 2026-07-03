from src.loaders.document_loader import DocumentLoader
from src.loaders.pdf_loader import PDFLoader
from src.loaders.csv_loader import CSVLoader
from src.processors.text_processor import TextProcessor
from src.chunking.chunker import Chunker


def main():
    document_loader = DocumentLoader()
    pdf_loader = PDFLoader()
    csv_loader = CSVLoader() 
    processor = TextProcessor()
    chunker = Chunker()

    pdfs = document_loader.get_pdf_files()
    

    print("📂 Leyendo documentos...\n")

    for pdf in pdfs:

        document = pdf_loader.read_pdf(pdf)

        document.content = processor.clean(document.content)

        chunks = chunker.split(document.content)

        print(f"📄 {document.name}")
        print(f"Caracteres extraídos: {len(document.content)}")
        print(f"Cantidad de chunks: {len(chunks)}")
        print("Primeros 250 caracteres:\n")

        print(document.content[:250])

        print("-" * 60)


    csvs = document_loader.get_csv_files()

    print("\n📊 Leyendo archivos CSV...\n")

    for csv in csvs:

        document = csv_loader.read_csv(csv)

        print(f"📄 {document.name}")
        print("Primeros 500 caracteres:\n")

        print(document.content[:500])

        print("-" * 60)

    
if __name__ == "__main__":
    main()