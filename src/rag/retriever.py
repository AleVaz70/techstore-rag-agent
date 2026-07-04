class Retriever:
    """
    Recupera los documentos más relevantes desde la base vectorial.
    """

    def __init__(self, vector_store):
        self.vector_store = vector_store

    def search(self, query: str, k: int = 3):
        """
        Realiza una búsqueda semántica.
        """
        return self.vector_store.search(query, k)

    def build_context(self, query: str, k: int = 3) -> str:
        """
        Construye el contexto que será enviado al LLM.
        """

        results = self.search(query, k)

        parts = []

        for result in results:
            parts.append(
                f"Documento: {result.metadata.get('source')}\n"
                f"Tipo: {result.metadata.get('type')}\n"
                f"Fragmento:\n{result.page_content}\n"
                f"{'-' * 50}\n"
            )

        return "\n".join(parts)