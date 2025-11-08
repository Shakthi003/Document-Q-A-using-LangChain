# 📄 Document Q&A using LangChain & Streamlit

An interactive Streamlit web app that allows users to upload PDF documents, create semantic embeddings locally using Ollama (Gemma), and ask natural language questions grounded in the uploaded files.

The app leverages LangChain, Ollama (Gemma 2B), and ChromaDB for intelligent document retrieval and question-answering — all running locally without cloud dependencies.

🚀 Features

📚 Upload and process multiple PDF documents

🔍 Automatic text chunking and embedding creation with Gemma via Ollama

💬 Ask questions and get contextual answers from your PDFs

🧠 Powered by LangChain, Ollama, and Chroma

💾 Persistent local vector database for quick retrieval

🌐 Clean and responsive Streamlit interface

🧩 Tech Stack
Component	Technology
Frontend UI	Streamlit
AI Framework	LangChain
Embeddings	Ollama (Gemma 2B)
Vector Store	ChromaDB
PDF Loader	LangChain PyPDFLoader
Language	Python 3.11+
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/Shakthi003/Document-Q-A-using-LangChain.git
cd Document-Q-A-using-LangChain

2️⃣ Create a Virtual Environment
python -m venv .venv
.venv\Scripts\activate   # On Windows

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Ensure Ollama is Installed

Download and install Ollama from https://ollama.ai

Then pull the Gemma model:

ollama pull gemma:2b

5️⃣ Run the Streamlit App
streamlit run app.py

🧠 Usage

Upload one or more PDF files under “📄 Upload PDF(s)”.

Click 🛠️ Process documents and (re)build index to generate embeddings.

Enter your question in the text box — the app retrieves and answers from your documents.

🛠️ Example Questions

“What is the purpose of this report?”

“Summarize the main findings.”

“Who is mentioned in section 2?”

🚧 Future Improvements

Add support for DOCX, TXT, and HTML documents

Allow switching between multiple Ollama models (Mistral, Llama3, Gemma)

Integrate chat history and memory

Enable streamed token responses for faster interaction


2️⃣ Create a Virtual Environment

python -m venv .venv
.venv\Scripts\activate   # On Windows


3️⃣ Install Requirements

pip install -r requirements.txt


4️⃣ Ensure Ollama is Installed

Download and install Ollama from https://ollama.ai

Then pull the Gemma model:

ollama pull gemma:2b


5️⃣ Run the Streamlit App

streamlit run app.py


🧠 Usage

Upload one or more PDF files under “📄 Upload PDF(s)”.

Click 🛠️ Process documents and (re)build index to generate embeddings.

Enter your question in the text box — the app retrieves and answers from your documents.

🛠️ Example Questions

“What is the purpose of this report?”

“Summarize the main findings.”

“Who is mentioned in section 2?”


🚧 Future Improvements

Add support for DOCX, TXT, and HTML documents

Allow switching between multiple Ollama models (Mistral, Llama3, Gemma)

Integrate chat history and memory

Enable streamed token responses for faster interaction

---
