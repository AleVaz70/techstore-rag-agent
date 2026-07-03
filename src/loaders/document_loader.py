from pathlib import Path


class DocumentLoader:
    """Busca los documentos disponibles en la carpeta data."""

    def __init__(self, data_path="data"):
        self.data_path = Path(data_path)

    def get_pdf_files(self):
        return list((self.data_path / "pdf").glob("*.pdf"))

    def get_csv_files(self):
        return list((self.data_path / "csv").glob("*.csv"))