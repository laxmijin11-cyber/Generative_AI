#  !pip install langchain chromadb huggingface tiktoken pypdf langchain_huggingface langchain-community

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from langchain_core.documents import Document

doc1 = Document(
    page_content="Virat Kohli – The chase master and greatest modern-day batsman, known for his aggression, consistency, and fitness revolution in Indian cricket.",
    metadata={"team": "Royal Challenger Bangalore"},
)
doc2 = Document(
    page_content="Rohit Sharma – The Hitman, holder of three ODI double centuries, known for his elegant pull shots and record-breaking sixes.",
    metadata={"team": "Mumbai Indans"},
)
doc3 = Document(
    page_content="MS Dhoni – Captain Cool, India's most successful skipper, famous for his calmness, finishing ability, and iconic 2011 World Cup six.",
    metadata={"team": "Chennai Super Kings"},
)
doc4 = Document(
    page_content="Jasprit Bumrah – The world's best fast bowler, deadly yorkers, unorthodox action, and India's go-to man in death overs.",
    metadata={"team": "Mumbai indians"},
)
doc5 = Document(
    page_content="Ravindra Jadeja – Sir Jadeja, an elite all-rounder, brilliant left-arm spinner, gun fielder, and handy lower-order batsman.",
    metadata={"team": "Royal Challenger Bangalore"},
)

docs = [doc1, doc2, doc3, doc4, doc5]

vector_store = Chroma(
    embedding_function=HuggingFaceEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2"
    ),
    persist_directory="my_chroma_db",
    collection_name="sample",
)
# sqlite h sql file mai bhi run ho sakta h

# print(vector_store)

# add documents
# vector_store.add_documents(docs)
# id -own generate or khud daal do id

# print(vector_store.get(include=["embeddings", "documents", "metadatas"]))
# ek dictionary return ho rahi jisme id sabka dikha then embeddings then documents of all then metadata of all


# search documents
# print(vector_store.similarity_search(query="Who among these are a bowler?", k=2))
# k=2 kitne similar objects you want?

# search with similarity score
# print(
#     vector_store.similarity_search_with_score(query="who among are these bowler?", k=2)
# )
# kam score -bahut acha distance kam hai toh close hai

# metadata filtering
# print(
#     vector_store.similarity_search_with_score(
#         query="", filter={"team": "Chennai Super Kings"}
#     )
# )

# update document

# updated_doc1 = Document(
#     page_content="Virat kohli is a good writer", metadata={"team": "RCB"}
# )

# vector_store.update_document(
#     document_id="6811acfc-d096-4cc5-827e-556d5f387696", document=updated_doc1
# )

# view document
# vector_store.get(include=["embeddings", "documents", "metadata"])

# delete document
vector_store.delete(ids=["7d3ea007-6bf4-45b3-9d65-9ac587f60d9"])

# view_document
result = vector_store.get(include=["embeddings", "documents", "metadatas"])
print(result)

"""
{'ids': ['6811acfc-d096-4cc5-827e-556d5f387696', '23cbe684-7e9d-487b-849e-fd220c313844', 'bb9efd6a-11bb-4402-a929-296eb19c1085', 'e8b583f4-8fab-4da5-89d4-858e4075e64a', '7d3ea007-6bf4-45b3-9d65-9ac587f60d99', '7f41a8bf-a9c0-4638-bdf4-16d633e8b9a9', 'c43adc61-dbf0-4155-8b82-6537e6851e63', '44f2af9a-19c8-46f5-99af-13a4d257f4b7', '986f8e91-9821-44b9-bc50-c5405240ccc0', '379eec21-02e9-4c95-8c0c-5df86582c28c'], 'embeddings': array([[ 0.0138568 ,  0.10819412, -0.08422185, ..., -0.02208439,
         0.07761966, -0.0031867 ],
       [-0.00393943,  0.0332064 , -0.07671764, ..., -0.06232869,
         0.01254802,  0.05151311],
       [-0.0359785 ,  0.02011102,  0.00658582, ...,  0.01030423,
        -0.05562608, -0.03496559],
       ...,
       [-0.0359785 ,  0.02011102,  0.00658582, ...,  0.01030423,
        -0.05562608, -0.03496559],
       [-0.0058366 , -0.00711671, -0.06604353, ..., -0.11337732,
         0.01757094,  0.10075535],
       [-0.0169093 ,  0.04517508, -0.0153631 , ..., -0.09834138,
        -0.04433132, -0.00040305]], shape=(10, 384)), 'documents': ['Virat Kohli – The chase master and greatest modern-day batsman, known for his aggression, consistency, and fitness revolution in Indian cricket.', 'Rohit Sharma – The Hitman, holder of three ODI double centuries, known for his elegant pull shots and record-breaking sixes.', "MS Dhoni – Captain Cool, India's most successful skipper, famous for his calmness, finishing ability, and iconic 2011 World Cup six.", "Jasprit Bumrah – The world's best fast bowler, deadly yorkers, unorthodox action, and India's go-to man in death overs.", 'Ravindra Jadeja – Sir Jadeja, an elite all-rounder, brilliant left-arm spinner, gun fielder, and handy lower-order batsman.', 'Virat Kohli – The chase master and greatest modern-day batsman, known for his aggression, consistency, and fitness revolution in Indian cricket.', 'Rohit Sharma – The Hitman, holder of three ODI double centuries, known for his elegant pull shots and record-breaking sixes.', "MS Dhoni – Captain Cool, India's most successful skipper, famous for his calmness, finishing ability, and iconic 2011 World Cup six.", "Jasprit Bumrah – The world's best fast bowler, deadly yorkers, unorthodox action, and India's go-to man in death overs.", 'Ravindra Jadeja – Sir Jadeja, an elite all-rounder, brilliant left-arm spinner, gun fielder, and handy lower-order batsman.'], 'uris': None, 'included': ['embeddings', 'documents', 'metadatas'], 'data': None, 'metadatas': [{'team': 'Royal Challenger Bangalore'}, {'team': 'Mumbai Indans'}, {'team': 'Chennai Super Kings'}, {'team': 'Mumbai indians'},{'team': 'Royal Challenger Bangalore'}, {'team': 'Royal Challenger Bangalore'}, {'team': 'Mumbai Indans'}, {'team': 'Chennai Super Kings'}, {'team': 'Mumbai indians'}, {'team': 'Royal Challenger Bangalore'}]}
        
"""
# if i run it again it will again produce embedingd or use older one?
# **No** — it will **reuse** older embeddings if the same documents with the same IDs already exist in the collection.

"""
---here why its not deleted?

**It will still produce NEW embeddings if you run it again.**

Here's why:

## The Real Behavior

You have **10 documents** in Chroma. The `add_documents` line is **commented out**, so nothing new gets added. But if you **uncomment** it and run again:

- Chroma will generate **5 new random IDs** for the 5 documents in `docs`
- It will compute **5 new embeddings**
- It will **add** them (not replace)
- Total becomes **15 documents**

## What "Reuse Older" Actually Means

My earlier answer was **partially wrong**. Let me clarify:

| Scenario | What Happens |
|----------|-------------|
| Same ID, same content | Reuses embedding (no recompute) |
| Same content, **new random ID** | **New embedding computed** |
| Different content | New embedding |

**Chroma does not deduplicate based on content.** It only checks IDs.

## In Your Case

- `add_documents(docs)` generates **new random IDs each run**
- So embeddings are **recomputed every time**
- You get duplicates

## How to Actually Reuse Embeddings

You must **assign fixed IDs yourself**:

```python
doc1 = Document(
    page_content="Virat Kohli...",
    metadata={"team": "RCB"},
    id="virat"          # fixed ID
)
```

Now if you run again:
- Chroma sees ID `"virat"` already exists
- It **skips** recomputation (or updates if content changed)

## Bottom Line

- **Without fixed IDs** → new embeddings every run, duplicates grow
- **With fixed IDs** → embeddings reused, no duplicates
- Your current code will keep adding duplicates

**Fix:** Delete the `my_chroma_db` folder, add fixed IDs, and re-run once.
"""
