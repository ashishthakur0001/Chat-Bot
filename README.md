# Chat-Bot

# 🤖 RAG-Based Generative AI Chat Assistant

An advanced **Retrieval-Augmented Generation (RAG)** chatbot built using **Chainlit, LangChain, ChromaDB, Groq, and Ollama** for accurate, context-aware conversational AI.

The assistant processes custom documents, retrieves relevant knowledge using vector embeddings, and generates intelligent responses with modern LLMs.

---

# 🚀 Features

- 🔍 Retrieval-Augmented Generation (RAG)
- 💬 Context-aware conversational AI
- 📄 PDF/Text document ingestion
- 🧠 Semantic search using embeddings
- ⚡ Fast inference using Groq LLMs
- 🖥️ Local LLM support with Ollama
- 🗂️ ChromaDB vector database integration
- 🔒 Privacy-focused local execution
- 📈 Scalable architecture for large datasets
- 🌐 Interactive UI using Chainlit

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core backend |
| Chainlit | Chat interface |
| LangChain | RAG orchestration |
| ChromaDB | Vector database |
| Ollama | Local LLM execution |
| Groq | High-speed inference |
| Sentence Transformers | Embeddings |
| PyPDF | PDF processing |

---

# 📁 Project Structure

```bash
rag-chat-assistant/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── data/
│   └── sample.pdf
│
├── chroma_db/
│
├── utils/
│   ├── loader.py
│   ├── embeddings.py
│   ├── retriever.py
│   └── llm.py
│
└── screenshots/
    └── demo.pngA Retrieval Augmented Generation (RAG) chatbot that can process PDF documents and answer questions using GROQ LLM.
Features
PDF document processing
RAG implementation using Chroma vector store
GROQ LLM integration
Conversational memory
Interactive web interface using Chainlit
Setup
Clone the repository
Create a .env file and add your GROQ API key:
GROQ_API_KEY=your_api_key_here
Run setup.bat as administrator to install Python and dependencies
Run run.bat to start the chatbot
Requirements
Python 3.10+
See requirements.txt for Python packages

