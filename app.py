import os
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

# LangChain imports
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Local utility imports
from utils import ensure_dirs, cleanup_uploaded_files, DATA_DIR, DB_DIR

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Document Q&A (Gemma + LangChain)", layout="wide")

ensure_dirs()

st.title("📄 Document Q&A — Gemma + LangChain")
st.caption("Upload PDFs, build embeddings using Ollama (Gemma), and ask questions grounded in your documents.")

col1, col2 = st.columns([3, 1])

# Left column — Upload & process
with col1:
    uploaded_files = st.file_uploader(
        "Upload PDF(s)", type=["pdf"], accept_multiple_files=True
    )

    if uploaded_files:
        st.info(f"Saving {len(uploaded_files)} file(s) to the data/ folder...")
        for up in uploaded_files:
            save_path = DATA_DIR / up.name
            with open(save_path, "wb") as f:
                f.write(up.getbuffer())
        st.success("✅ Files saved. Now press 'Process documents' to create embeddings.")

    if st.button("🛠️ Process documents and (re)build index"):
        all_docs = []
        for pdf_path in sorted(DATA_DIR.glob("*.pdf")):
            try:
                loader = PyPDFLoader(str(pdf_path))
                docs = loader.load()
                all_docs.extend(docs)
            except Exception as e:
                st.error(f"Failed to load {pdf_path.name}: {e}")

        if not all_docs:
            st.warning("No documents found in data/ — upload PDFs first.")
        else:
            st.info("📚 Splitting documents into chunks...")
            splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
            split_docs = splitter.split_documents(all_docs)

            st.info("✨ Creating embeddings using Ollama (Mistral)...")
            embeddings = OllamaEmbeddings(model="gemma:2b")

            st.info("🔍 Building Chroma vectorstore (persisting to db/)...")
            vectordb = Chroma.from_documents(
                split_docs,
                embedding=embeddings,
                persist_directory=str(DB_DIR)
            )
            vectordb.persist()
            st.success("✅ Index built and persisted to db/")

# Right column — maintenance
with col2:
    st.markdown("### Controls")
    if st.button("🧹 Clear uploaded files (data/)"):
        cleanup_uploaded_files()
        st.success("data/ cleaned.")
    if st.button("🧾 Clear vector DB (db/)"):
        import shutil
        try:
            # Try to gracefully shut down Chroma if it's running
            try:
                from langchain_community.vectorstores import Chroma
                dummy_embeddings = OllamaEmbeddings(model="gemma:2b")  # or whatever you're using
                vectordb = Chroma(persist_directory=str(DB_DIR), embedding_function=dummy_embeddings)
                vectordb._client.close()  # Close the Chroma client
            except Exception as e:
                st.info("Chroma was not active or already closed.")

            # Now delete the files
            for p in DB_DIR.glob("*"):
                if p.is_file():
                    p.unlink()
                else:
                    shutil.rmtree(p, ignore_errors=True)
            st.success("db/ cleared.")
        except Exception as e:
            st.error(f"Failed to clear db/: {e}")


st.markdown("---")

# Query UI
query = st.text_input("💬 Ask a question about your uploaded documents:")

if query:
    if not DB_DIR.exists() or not any(DB_DIR.iterdir()):
        st.warning("No vector DB found. Please upload PDFs and click 'Process documents'.")
    else:
        with st.spinner("🤔 Thinking..."):
            embeddings = OllamaEmbeddings(model="gemma:2b")
            vectordb = Chroma(persist_directory=str(DB_DIR), embedding_function=embeddings)
            retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 4})

            llm = Ollama(model="gemma:2b", temperature=0.0)

            # LCEL-style chain
            # Retrieve relevant documents
            docs = retriever.invoke(query)
            context = "\n\n".join([doc.page_content for doc in docs])

            # Format prompt manually
            prompt = f"""Use the following context to answer the question.

            Context:
            {context}

            Question:
            {query}
            """

            # Run the LLM
            answer = llm.invoke(prompt)
            st.markdown("### 🧠 Answer")
            st.write(answer)