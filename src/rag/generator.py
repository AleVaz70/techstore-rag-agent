import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


class Generator:
    """
    Genera respuestas utilizando Gemini a partir del contexto recuperado.
    """

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "No se encontró la variable GEMINI_API_KEY en el archivo .env"
            )

        self.client = genai.Client(api_key=api_key)

        self.model = "gemini-2.5-flash"

    def generate(self, question: str, context: str) -> str:

        prompt = f"""
Eres un asistente de TechStore.

Responde únicamente utilizando la información del contexto.

Si la respuesta no aparece en el contexto responde exactamente:

"No encontré esa información en los documentos disponibles."

Al finalizar la respuesta indica los documentos utilizados.

Contexto:

{context}

Pregunta:

{question}
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return response.text