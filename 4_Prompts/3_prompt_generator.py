# PromptTemplate is reusable anywhere.hence we use them instead of f string
from langchain_core.prompts import PromptTemplate

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
    validate_template=True,
    # validate_template=True checks if input variables are not less nor extra
)

template.save("template.json")
