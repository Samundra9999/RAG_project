import os
import streamlit as st
from dotenv import load_dotenv

from retrivers.bm25 import BM25Retriever
from retrivers.hybrid import HybridRetriever
from chunking.factory import get_chunker
from loaders.factory import get_loader
from vector_store.factory import get_vectorstore
from llm.factory import get_llm
from pipeline.rag_pipeline import RAGPipeline

load_dotenv()

st.title("AI Notes Assistant")

# Load GROQ key from .env
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY not found in .env file")
    st.stop()

# -----------------------------
# Session state (store pipeline)
# -----------------------------
if "rag" not in st.session_state:
    st.session_state.rag = None

# -----------------------------
# Upload + Query Form
# -----------------------------
with st.form("rag_form"):

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    query = st.text_input("Enter your question")

    submit = st.form_submit_button("Submit")

# -----------------------------
# Process only on submit
# -----------------------------
if submit:

    if uploaded_file is None:
        st.warning("Please upload a PDF first.")
        st.stop()

    file_path = "temp.pdf"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Processing PDF..."):

        loader = get_loader(file_path)
        docs = loader.load(file_path)

        chunker = get_chunker("recursive", config={})
        chunks = chunker.chunk(docs)

        store = get_vectorstore("chroma")
        store.add_documents(chunks)

        bm25 = BM25Retriever(chunks)

        retriever = HybridRetriever(
            vector_store=store,
            bm25_retriever=bm25
        )

        llm = get_llm("groq", api_key=GROQ_API_KEY)

        st.session_state.rag = RAGPipeline(retriever, llm)

    # Run query after pipeline is ready
    if query.strip():

        with st.spinner("Generating answer..."):
            result = st.session_state.rag.ask(query, k=5)

        st.subheader("Answer")
        st.write(result["answer"])

    else:
        st.warning("Please enter a question.")