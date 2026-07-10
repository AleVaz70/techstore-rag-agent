from src.loaders.document_loader import DocumentLoader
from src.loaders.pdf_loader import PDFLoader
from src.loaders.csv_loader import CSVLoader
from src.processors.text_processor import TextProcessor
from src.chunking.chunker import Chunker


class IndexService:
    """
    Se encarga de procesar los documentos e incorporarlos a la base vectorial.
    """

    def __init__(self, vector_store):
        self.document_loader = DocumentLoader()
        self.pdf_loader = PDFLoader()
        self.csv_loader = CSVLoader()
        self.processor = TextProcessor()
        self.chunker = Chunker()
        self.vector_store = vector_store

    def run(self):
        """
        Procesa todos los documentos disponibles.
        """
        self.vector_store.reset()
        pdfs = self.document_loader.get_pdf_files()

        print("📂 Leyendo documentos...\n")

        for pdf in pdfs:

            document = self.pdf_loader.read_pdf(pdf)

            document.content = self.processor.clean(document.content)

            chunks = self.chunker.split(document.content)

            self.vector_store.add_document(document, chunks)

            print(f"📄 {document.name}")
            print(f"Caracteres extraídos: {len(document.content)}")
            print(f"Cantidad de chunks: {len(chunks)}")
            print("-" * 60)

        