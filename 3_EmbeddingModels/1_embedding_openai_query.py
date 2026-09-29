# jada bada vector-jada context capture hoga--but cost jada lagega
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

result = embedding.embed_query("What is capital of India?")

print(str(result))

# large model vector dim:3072
# small model vector dimensions:1536
