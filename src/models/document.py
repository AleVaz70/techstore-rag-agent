"""
Modelo de documento utilizado por el proyecto.
"""

from dataclasses import dataclass


@dataclass
class Document:
    """
    Representa un documento independientemente de su formato.
    """

    name: str
    content: str
    doc_type: str