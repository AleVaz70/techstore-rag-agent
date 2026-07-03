"""
Divide documentos en fragmentos (chunks).
"""


class Chunker:
    """
    Divide un texto en fragmentos con solapamiento.
    """

    def split(self, text: str, chunk_size: int = 500, overlap: int = 50):

        chunks = []

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunks.append(text[start:end])

            start += chunk_size - overlap

        return chunks