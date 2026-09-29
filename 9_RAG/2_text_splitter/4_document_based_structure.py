# for special files like coding files and markdown files
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

# text = """
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def hello():
#     return {"message": "Hello World"}


# @app.get("/about")
# def about():
#     return {"message": "This is my first FastAPI application"}

# """

text = """

## ✨ Features

| Feature | Description |
| :--- | :--- |
| 🎭 **3 Personas** | Switch between Angry, Funny, and Sad AI personalities instantly. |
| 🧠 **Chat Memory** | Uses `st.session_state` to retain the full conversation context. |
| 💬 **Modern UI** | Built with `st.chat_input` and `st.chat_message` for a clean, chat-like interface. |
| 🔄 **Reset Chat** | One-click button to clear the conversation and start fresh. |
| 🔒 **Security** | Loads API keys securely using `python-dotenv`. |

---

## 🛠️ Tech Stack

| Category | Technology |
| :--- | :--- |
| Frontend UI | Streamlit |
| AI Framework | LangChain |
| Language Model | Mistral AI (`mistral-small-2603`) |
| Environment | Python 3.9+ |

---

## 📁 Project Structure

```text
Mood_AI_Chatbot/
├── UIchatbot.py                 # Main Streamlit application
├── requirements.txt       # List of Python dependencies
├── .env                   # API keys (DO NOT push to GitHub)
└── README.md              # Project documentation
"""


# splitter = RecursiveCharacterTextSplitter.from_language(
#     language=Language.PYTHON, chunk_size=30, chunk_overlap=0
# )
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN, chunk_size=100, chunk_overlap=0
)

# perform the split
chunks = splitter.split_text(text)
print(len(chunks))
print(chunks)
# same for PHP,JS,C++,HTML,MARKDOWN
