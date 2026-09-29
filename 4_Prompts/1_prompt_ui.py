# Static Prompts-user ko kafi control
# galat name daal dia toh LLM hallucinate kar jayega ya wrong result
from langchain_google_genai import ChatGoogleGenerativeAI

# from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
import streamlit as st

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash", max_tokens=10)
st.header("Research Tool")
user_input = st.text_input("Enter your prompt")
if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)
