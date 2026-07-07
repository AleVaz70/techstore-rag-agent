# TechStore RAG

Asistente inteligente desarrollado para el Challenge Alura Agentes 2026.

El proyecto implementa una arquitectura **RAG (Retrieval-Augmented Generation)** para responder consultas utilizando exclusivamente la documentación interna de una empresa ficticia llamada **TechStore**.

La aplicación permite realizar preguntas sobre políticas, pagos, envíos, garantías y devoluciones, recuperando primero la información más relevante desde una base vectorial y utilizando posteriormente Gemini para generar una respuesta basada únicamente en ese contexto.

## Objetivo

Desarrollar un asistente capaz de:

- Consultar documentación interna en lenguaje natural.
- Recuperar automáticamente los fragmentos más relevantes.
- Generar respuestas fundamentadas únicamente en la documentación disponible.
- Evitar respuestas inventadas cuando la información no existe.

## Estado del proyecto

🚧 En desarrollo

## Características

- Lectura automática de documentos PDF y CSV.
- División de documentos en fragmentos (chunking).
- Búsqueda semántica mediante una base vectorial (ChromaDB).
- Generación de respuestas utilizando Gemini.
- Respuestas basadas únicamente en la documentación disponible.
- Interfaz web desarrollada con Streamlit.

## Tecnologías utilizadas

- Python 3.11
- Streamlit
- LangChain
- ChromaDB
- Sentence Transformers
- Google Gemini API
- python-dotenv

## Instalación

1. Clonar el repositorio.

```bash
git clone https://github.com/AleVaz70/TechStore-RAG.git
```

2. Ingresar al proyecto.

```bash
cd TechStore-RAG
```

3. Crear un entorno virtual.

```bash
python -m venv .venv
```

4. Activar el entorno virtual.

**Windows**

```bash
.venv\Scripts\activate
```

5. Instalar las dependencias.

```bash
pip install -r requirements.txt
```

6. Crear un archivo `.env` con la clave de Gemini.

```text
GEMINI_API_KEY=tu_api_key
```

## Ejemplos de consultas

- ¿Qué métodos de pago acepta TechStore?
- ¿Cuánto tarda un reembolso?
- ¿Cómo funcionan los envíos?
- ¿Cómo funciona la garantía?
- ¿Qué productos no pueden devolverse?