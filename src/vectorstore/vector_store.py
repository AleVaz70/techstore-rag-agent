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

        try:
            client.delete_collection("techstore")
        except Exception:
            # La colección no existe todavía
            pass

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