class Retriever:
    """
    Recupera los documentos más relevantes desde la base vectorial.
    """

    def __init__(self, vector_store):
        self.vector_store = vector_store

    def search(self, query: str, k: int = 10):
        """
        Realiza una búsqueda semántica y devuelve los documentos relevantes.
     """

        results = self.vector_store.db.similarity_search_with_score(query, k=k)

        documents = []

        for doc, score in results:

            text = doc.page_content.lower()

            # Ignorar índices
            if "índice" in text:
               continue

            # Ignorar fragmentos demasiado pequeños
            if len(doc.page_content.strip()) < 120:
               continue

            documents.append(doc)

        return documents

    def build_context(self, query: str, k: int = 10):
        
        results = self.search(query, k)

        # quedarse con los mejores 4 ya filtrados
        results = results[:4]

        parts = []

        for result in results:
            parts.append(
                f"Documento: {result.metadata.get('source')}\n"
                f"Tipo: {result.metadata.get('type')}\n"
                f"Fragmento:\n{result.page_content}\n"
                f"{'-'*50}\n"
            )

        return "\n".join(parts)