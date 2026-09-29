# pip install langchain-experimental
from langchain_experimental.text_splitter import SemanticChunker

# from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv

load_dotenv()

model = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

# text_splitter = SemanticChunker(
#     OpenAIEmbeddings(),
#     breakpoint_threshold_type="standard_deviation",
#     breakpoint_threshold_amount=1,
#     # 1 std dev/2 std dev etc
# )


text_splitter = SemanticChunker(
    HuggingFaceEmbeddings(),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1,
    # 1 std dev/2 std dev etc
)
sample = """O my Lord Krishna, in this dark era,
You created me, and guide my soul’s terra.Cricket is a bat-and-ball game that is played between two teams of eleven players on a field
"""
docs = text_splitter.create_documents([sample])

print(len(docs))
print(docs)
