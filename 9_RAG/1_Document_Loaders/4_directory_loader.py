from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
    TextLoader,
)

# loader = DirectoryLoader(path="demo-folder", glob="*.pdf", loader_cls=PyPDFLoader)
loader = DirectoryLoader(
    path=r"C:\users\admin\OneDrive\Desktop\New folder\LANGCHAIN_MODELS\9_RAG\1_Document_Loaders\demo-folder",
    glob="*.txt",
    loader_cls=TextLoader,
)


# docs = loader.load()
docs = loader.lazy_load()

for document in docs:
    print(document.metadata)


# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)
# print(doc[326].page_content)
