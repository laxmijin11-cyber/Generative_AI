from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Delhi is capital of India.",
    "Paris is capital of France.",
    "Kolkata is capital of West Bengal.",
]

vector = embeddings.embed_documents(documents)

print(str(vector))
