"""
Módulo encargado de cargar archivos CSV.
"""

from pathlib import Path

import pandas as pd

from src.models.document import Document


class CSVLoader:
    """Carga archivos CSV."""

    def read_csv(self, csv_path: Path) -> Document:
        """
        Lee un CSV y devuelve un objeto Document.
        """

        df = pd.read_csv(csv_path)

        return Document(
            name=csv_path.name,
            content=df.to_string(index=False),
            doc_type="csv"
        )