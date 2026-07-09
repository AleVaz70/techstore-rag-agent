from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document as LangChainDocument
import chromadb


class VectorStore:
    """
    Administra la base de datos vectorial utilizando ChromaDB.
    """

    def __init__(self):

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        persist_directory = "data/chroma_db"

        client = chromadb.PersistentClient(path=persist_directory)
        
        self.db = Chroma(
            client=client,
            collection_name="techstore",
            embedding_function=self.embeddings,
        )

    def add_document(self, document, chunks):
        """
        Agrega los chunks de un documento al índice vectorial.
        """

        langchain_docs = []

        for i, chunk in enumerate(chunks):
            langchain_docs.append(
                LangChainDocument(
                    page_content=chunk,
                    metadata={
                        "source": document.name,
                        "type": document.doc_type,
                        "chunk": i,
                    },
                )
            )

        self.db.add_documents(langchain_docs)

    def search(self, query: str, k: int = 3):
        """
        Busca los k fragmentos más relevantes para la consulta.
        """
        return self.db.similarity_search(query, k=k)
    
    def reset(self):
        """
         Elimina todos los documentos de la colección.
        """

        self.db.delete_collection()

        self.db = Chroma(
            client=chromadb.PersistentClient(path="data/chroma_db"),
            collection_name="techstore",
            embedding_function=self.embeddings,
        )

    def is_empty(self):
        """
        Indica si la colección está vacía.
        """
        return self.db._collection.count() == 0