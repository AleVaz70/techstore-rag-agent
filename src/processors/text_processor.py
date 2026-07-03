"""
Procesamiento y limpieza de texto.
"""

import re


class TextProcessor:
    """
    Limpia el texto antes del proceso de chunking.
    """

    def clean(self, text: str) -> str:

        # Elimina espacios múltiples
        text = re.sub(r"[ \t]+", " ", text)

        # Elimina líneas vacías repetidas
        text = re.sub(r"\n\s*\n+", "\n\n", text)

        return text.strip()