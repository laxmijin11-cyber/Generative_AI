# from langchain_openai import ChatOpenAI

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
from langchain_core.prompts import PromptTemplate
import streamlit as st
from langchain_core.prompts import load_prompt

st.header("Research Tool")

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash", max_output_tokens=50)
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention is all you need",
        "BERT:Pre training of deep bisdirectional Model",
        "GPT-3:Language Models are Few Shot Learners",
        "Diffusion Models beat GANs on Image Synthesis",
    ],
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code oriented", "Mathematical"],
)

length_input = st.selectbox(
    "Select Explanation length",
    [
        "Short(1-2 small paragraphs)",
        "Medium(3-5 paragraphs)",
        "long(detailed paragraphs)",
    ],
)

'''
template = PromptTemplate(
    template="""
    Please Summarize the research paper titled "{paper_input}" with the following specifications:
explanation Style:{style_input}
Explanation Length:{length_input}
1.Mathematical details:
    -Include relevant mathematical equations if present in the paper
    -explain mathematical concept using simple,intuitive code snippets where applicable
2.Analogies:
    -Use relatable analogies to simplifyc complex ideas
    If certain infois not available "Insufficient information" instead of guessing
    Ensure the summary is clear,accurate and align with provided style and length
    """,
    input_variables=["paper_input", "style_input", "length_input"],
)
'''

template = load_prompt("template.json")

# fill the placeholders
prompt = template.invoke(
    {
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input,
    }
)
if st.button("Summarize"):
    with st.spinner("Generating"):
        result = model.invoke(prompt)
        st.write(result.content)
        # print(result.content)--vscode not in streamlit app
