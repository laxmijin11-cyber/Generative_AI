from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
# https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    max_new_tokens=4,
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("who is PM of India")

print(result.content)
