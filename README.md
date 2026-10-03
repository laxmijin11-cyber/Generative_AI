# 🚀 Generative AI with LangChain — Complete Learning Journey

A hands-on repository documenting my complete journey through **Generative AI, LLMs, RAG, and Agentic AI** — built while following the CampusX Gen AI playlist.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-1.0-green)
![Gemini](https://img.shields.io/badge/Gemini-2.0-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📚 What's Inside

| **Module** | **Topics Covered** |
|------------|---------------------|
| **1. LLMs & Models** | OpenAI, Gemini, Hugging Face, ChatModels, Embeddings |
| **2. Prompts** | Prompt Templates, ChatPromptTemplate, MessagesPlaceholder |
| **3. Output Parsers** | StrOutputParser, PydanticOutputParser, JSON Parser |
| **4. Chains** | Sequential, Parallel, Conditional (RunnableBranch), LCEL |
| **5. RAG** | Document Loaders, Text Splitters, Vector Stores (FAISS, ChromaDB), Retrievers |
| **6. Tools** | Tool Calling, Custom Tools, API Integration |
| **7. Agents** | LangGraph, ReAct Agents, Weather Agent, Multi-step Reasoning |
| **8. Projects** | YouTube Transcript RAG, PDF Chatbot, Agentic Systems |

---

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **Framework:** LangChain 1.0+, LangGraph
- **LLMs:** Google Gemini 2.0, OpenAI GPT, Hugging Face (Llama 3.1)
- **Vector DBs:** FAISS, ChromaDB
- **Embeddings:** Hugging Face (all-MiniLM-L6-v2)
- **Frontend:** Streamlit
- **Backend:** FastAPI (for projects)

---

## 🚀 Key Projects

### 1. **RAG YouTube Transcript Chatbot**
- Loads YouTube transcripts → Embeds → FAISS → Gemini answers questions.
- **Stack:** LangChain + FAISS + Gemini + Streamlit

### 2. **Multi-Tool Agent**
- An agent that can call weather APIs, search tools, and more.
- **Stack:** LangGraph + Tool Calling + Gemini

### 3. **PDF Chatbot** (coming soon)
- Upload PDFs → Ask questions → Get contextual answers.

---

## ⚡ Quick Start

```bash
# Clone
git clone https://github.com/laxmijin11-cyber/Generative_AI.git
cd Generative_AI

# Setup venv
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Setup API keys
echo "GOOGLE_API_KEY=your_key" > .env
echo "HUGGINGFACEHUB_API_TOKEN=your_token" >> .env

# Run any notebook in Jupyter
jupyter notebook
