"""
Divide documentos en fragmentos (chunks).
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter


class Chunker:
    """
    Divide un texto utilizando el separador de LangChain.
    """

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=700,
            chunk_overlap=100,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split(self, text: str):

        return self.splitter.split_text(text)