# 📄 Document Q&A using LangChain & Streamlit

An interactive Streamlit web app that allows users to **upload PDF documents**, create **semantic embeddings**, and **ask natural language questions** about the uploaded files.

The app uses **LangChain**, **Google Gemini (or OpenAI)**, and **Chroma vector store** to perform intelligent document retrieval and question-answering.

---

## 🚀 Features

* 📚 Upload and process multiple PDF documents
* 🔍 Automatic text chunking and vector embedding generation
* 💬 Ask questions and get answers based on document content
* 🧠 Uses **LangChain**, **Chroma**, and **LLMs (Gemini or OpenAI)**
* 💾 Persistent vector database for fast querying
* 🌐 Simple and beautiful Streamlit UI

---

## 🧩 Tech Stack

| Component    | Technology                          |
| ------------ | ----------------------------------- |
| Frontend UI  | Streamlit                           |
| AI Framework | LangChain                           |
| Embeddings   | Google Generative AI / OpenAI       |
| Vector Store | ChromaDB                            |
| PDF Loader   | PyMuPDF / LangChain Document Loader |
| Language     | Python 3.11+                        |

---

## ⚙️ Installation

1️⃣ **Clone the Repository**

```bash
git clone https://github.com/Shakthi003/Document-Q-A-using-LangChain.git
cd Document-Q-A-using-LangChain
```

2️⃣ **Create Virtual Environment**

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3️⃣ **Install Requirements**

```bash
pip install -r requirements.txt
```

4️⃣ **Run the Streamlit App**

```bash
streamlit run app.py
```

---

## 🧠 Usage

1. Upload one or more PDF files.
2. Click **“Process documents and (re)build index”**.
3. Type a question related to your documents.
4. The app will return an AI-generated answer based on your uploaded files.

---

## 🛠️ Example Questions

* “What is the summary of Chapter 3?”
* “Who is the author of the document?”
* “List the key findings from this report.”

---

## 📂 Project Structure

```
📦 Document-Q-A-using-LangChain
 ┣ 📁 data/              # Uploaded PDF files
 ┣ 📁 db/                # Persistent Chroma vector database
 ┣ 📜 app.py             # Main Streamlit app
 ┣ 📜 utils.py           # Utility functions
 ┣ 📜 requirements.txt   # Dependencies
 ┣ 📜 .env               # (Not committed) API keys
 ┗ 📜 .gitignore         # Ignore sensitive files
```

---

## 🚧 Future Improvements

* Support for DOCX and TXT uploads
* Multi-model selection (Gemini / OpenAI / Claude)
* Summarization and chat history memory
* Streamed token responses for real-time answers

---
