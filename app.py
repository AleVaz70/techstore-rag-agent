from src.vectorstore.vector_store import VectorStore
from src.rag.retriever import Retriever
from src.rag.generator import Generator

DEBUG = False


def main():

    print("🤖 TechStore RAG\n")

    vector_store = VectorStore()
    retriever = Retriever(vector_store)
    generator = Generator()

    while True:

        question = input("Pregunta (o 'salir'): ")

        if question.lower() == "salir":
            break

        if not question.strip():
            continue

        context = retriever.build_context(question)

        if DEBUG:
            print("\n========== CONTEXTO ==========\n")
            print(context)
            print("\n==============================\n")

        try:
            answer = generator.generate(question, context)

            print("\n" + "=" * 60)
            print(answer)
            print("=" * 60 + "\n")

        except Exception as e:
            print("\nError al consultar Gemini:")
            print(e)


if __name__ == "__main__":
    main()