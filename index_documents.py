from src.vectorstore.vector_store import VectorStore
from src.services.index_service import IndexService


def main():

    vector_store = VectorStore()

    indexer = IndexService(vector_store)

    indexer.run()


if __name__ == "__main__":
    main()