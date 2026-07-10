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

Responde únicamente utilizando la información proporcionada en el contexto.

Si la respuesta no aparece en el contexto responde exactamente:

"No encontré información suficiente en la documentación disponible para responder esa consulta."

Instrucciones importantes:
- No inventes información.
- No agregues conocimientos externos.

Al finalizar la respuesta escribe exactamente este formato:

Documentos utilizados:
- Nombre del documento

Utiliza únicamente el nombre del documento, sin la extensión ".pdf".
Escribe "Pagos", "Envíos", "Garantía" o "Devoluciones" según corresponda.
Deja una línea en blanco antes de "Documentos utilizados:".

Contexto:

{context}

Pregunta:

{question}
"""

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
            )

            return response.text

        except Exception as error:
            error_message = str(error)

            if "RESOURCE_EXHAUSTED" in error_message or "429" in error_message:

                return (
                    "⚠️ **Límite de consultas alcanzado.**\n\n"
                    "La API de Gemini no está disponible en este momento porque "
                    "se alcanzó la cuota permitida. Intentá nuevamente más tarde."
                )
            
            return (
                "⚠️ **Ocurrió un error al consultar Gemini.**\n\n"
                "Intentá nuevamente en unos minutos."
            )