"""
Módulo encargado de cargar archivos CSV.
"""

from pathlib import Path

import pandas as pd


class CSVLoader:
    """Carga archivos CSV utilizando pandas."""

    def read_csv(self, csv_path: Path) -> pd.DataFrame:
        """
        Lee un archivo CSV y devuelve un DataFrame.
        """
        return pd.read_csv(csv_path)