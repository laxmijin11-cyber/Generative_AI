from langchain_openai import ChatOpenAI

# BaseChatOpenAI-->BaseChatModel(mother class-all chat models using it)
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=1, max_completion_tokens=5)

result = model.invoke("What is capital of India")
result = model.invoke("name 5 male names")
result = model.invoke("name 5 lines poem on cricket")


print(result.content)

# string-->chatmodel-->dictionery(content+ kwargs)
# **`max_tokens`** = older param for total output length.
# **`max_completion_tokens`** = newer param (for newer OpenAI models like GPT-4o) — includes reasoning tokens.

# `temperature` must be between **0 and 2**.
