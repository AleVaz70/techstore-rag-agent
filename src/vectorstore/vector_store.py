from langchain_chroma import Chroma


class VectorStore:
    """
    Administra la base de datos vectorial utilizando ChromaDB.
    """

    def __init__(self):
        self.db = None
