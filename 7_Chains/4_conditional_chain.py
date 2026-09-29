from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=70,
)
model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal["Positive", "Negative"] = Field(
        description="give the sentiment of the feedback"
    )


parser2 = PydanticOutputParser(pydantic_object=Feedback)
prompt1 = PromptTemplate(
    template="Classify the sentiments of the following feedback text into positive or negative \n {feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()},
)

classifier_chain = prompt1 | model | parser2
# feedback_text = classifier_chain.invoke({"feedback": "this is terrible smartphone"})-->sentiment:'positive
# print(feedback_text)

# result = classifier_chain.invoke({"feedback": "this is terrible smartphone"}).sentiment
# print(result)

prompt2 = PromptTemplate(
    template="write an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"],
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=["feedback"],
)
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "Positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "Negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment"),
)
# if else statement in langchain

chain = classifier_chain | branch_chain
print(chain.invoke({"feedback": "this is terrible smartphone"}))

chain.get_graph().print_ascii()

"""
**Error:** `x` is a `Feedback` object, so use `x.sentiment` instead of `x["sentiment"]`.

**Fix:**
```python
(lambda x: x.sentiment == "Positive", prompt2 | model | parser),
(lambda x: x.sentiment == "Negative", prompt3 | model | parser),
```

**One-Line Summary:** *"Change `x['sentiment']` → `x.sentiment`."* 😊🚀
"""
