from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash", max_tokens=19)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="answer {question} from  {text}", input_variables=["text"]
)
url = "https://www.flipkart.com/realme-p4-lite-5g-mosaic-green-64-gb/p/itm90c243961f214?pid=MOBHN7A8SZ7F9C7T&param=24731&BU=Mobile&pageUID=1790343331627"
loader = WebBaseLoader(url)
docs = loader.load()
chain = prompt | model | parser
result = chain.invoke(
    {"question": "pros of product in 1 line", "text": docs[0].page_content}
)

print(result)
