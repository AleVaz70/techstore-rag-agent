import streamlit as st

from src.vectorstore.vector_store import VectorStore
from src.rag.retriever import Retriever
from src.rag.generator import Generator
from src.services.index_service import IndexService


# --------------------------------------------------
# Configuración de la página
# --------------------------------------------------

st.set_page_config(
    page_title="TechStore",
    page_icon="📦",
    layout="centered",
)


def load_css():
    with open("assets/style.css", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )


load_css()


# --------------------------------------------------
# Carga de componentes
# --------------------------------------------------

@st.cache_resource
def load_components():

    vector_store = VectorStore()

    if vector_store.is_empty():
        indexer = IndexService(vector_store)
        indexer.run()

    retriever = Retriever(vector_store)
    generator = Generator()

    return retriever, generator


# --------------------------------------------------
# Encabezado
# --------------------------------------------------

st.markdown(
    "<h1 class='main-title'>TechStore</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Asistente Inteligente para Documentación</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='description'>Consultá rápidamente la información disponible en la documentación interna de <b>TechStore</b>.</div>",
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Consultas frecuentes
# --------------------------------------------------

if "consultar_automatico" not in st.session_state:
    st.session_state.consultar_automatico = False

st.markdown("### Consultas frecuentes")

col1, col2 = st.columns(2)

with col1:

    if st.button("💳 Métodos de pago", use_container_width=True):
        st.session_state.question = "Qué métodos de pago acepta TechStore"
        st.session_state.consultar_automatico = True
        st.rerun()

    if st.button("📦 Envíos", use_container_width=True):
        st.session_state.question = "Cómo funcionan los envíos"
        st.session_state.consultar_automatico = True
        st.rerun()

with col2:

    if st.button("🔄 Reembolsos", use_container_width=True):
        st.session_state.question = "Cuánto tarda un reembolso"
        st.session_state.consultar_automatico = True
        st.rerun()

    if st.button("🛡️ Garantía", use_container_width=True):
        st.session_state.question = "Cómo funciona la garantía"
        st.session_state.consultar_automatico = True
        st.rerun()

# --------------------------------------------------
# Respuesta
# --------------------------------------------------

response_placeholder = st.container()


# --------------------------------------------------
# Consulta
# --------------------------------------------------

if "question" not in st.session_state:
    st.session_state.question = ""

with st.form("consulta_form"):

    question = st.text_input(
        "Escribí tu pregunta:",
        key="question",
        placeholder="Ej.: Cuánto tarda un reembolso",
    )

    consultar = st.form_submit_button(
        "🔎 Consultar",
        use_container_width=True,
    )

# --------------------------------------------------
# Respuesta
# --------------------------------------------------

if consultar or st.session_state.consultar_automatico:

    question = st.session_state.question

    if not question.strip():

        st.warning("⚠️ Ingresá una pregunta.")

    else:

        with st.spinner("Consultando la documentación..."):

            try:
                context = retriever.build_context(question)
                answer = generator.generate(question, context)

            except Exception:
                answer = (
                    "⚠️ **No fue posible obtener una respuesta en este momento.**\n\n"
                    "Intentá nuevamente más tarde."
                )

        st.session_state.consultar_automatico = False

        with response_placeholder:

            with st.container(border=True):

                 st.markdown(f"**Consulta:** {question}")

                 st.subheader("Respuesta")

                 st.markdown(answer)