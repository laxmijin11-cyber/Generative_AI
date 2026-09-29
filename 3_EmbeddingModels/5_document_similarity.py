# from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

from sklearn.metrics.pairwise import cosine_similarity

# embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents = [
    "Virat Kohli - The Run Machine",
    "Rohit Sharma - Hitman of Indian Cricket",
    "Smriti Mandhana - Queen of the Cover Drive",
    "MS Dhoni - Captain Cool",
    "Jasprit Bumrah - Yorker King",
    "Shubman Gill - Prince of Indian Cricket",
    "Harmanpreet Kaur - Six-Hitting Sensation",
    "Ravindra Jadeja - Sir Jadeja, The All-Rounder",
    "Sachin Tendulkar - The God of Cricket",
    "Yuvraj Singh - Six Sixes Hero",
]

query = "tell me about virat kohli"

doc_embeddings = embeddings.embed_documents(documents)
# 5 vectors-each 300 dimensional space
query_embedding = embeddings.embed_query(query)

# print(cosine_similarity([query_embedding], doc_embeddings))
# cosine similarity ko list bhejni h dono in 2D list
# cosine list-[[0.6666,0.3333,....]]
# we want 1d list
scores = cosine_similarity([query_embedding], doc_embeddings)[0]
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]
# list(enumerate(scores)) in it we get [(0,0.666),(1,0.333),....]
# sort on basis of score[1] and to get highest score we do -1
# sorted sorting in ascending order
print(query)
print(documents[index])
print("Cosine Similarity score is:", score)

# RAG based applications
# embeddings ko store karna chahiye ek baar run karke in vector database:retrieval

"""
Shape Handling: cosine_similarity([query_embedding], doc_embeddings)[0] correctly unpacks the 2D matrix down to a 1D list of similarity scores.

Top Match Retrieval: sorted(..., key=lambda x: x[1])[-1] correctly retrieves the highest-scoring tuple (index, score).
"""
