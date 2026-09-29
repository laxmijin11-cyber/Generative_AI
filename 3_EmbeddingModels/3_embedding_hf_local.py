from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "Delhi is capital of India."

vector = embeddings.embed_query(text)

print(str(vector))

"""
-model vs model_name: HuggingFaceEmbeddings uses model_name, not model.

-dimension parameter: HuggingFaceEmbeddings does not take a dimension parameter. Unlike OpenAI's text-embedding-3 models, all-MiniLM-L6-v2 produces a fixed 384-dimensional vector.

[0.03991769254207611, 0.02555042691528797, -0.032312311232089996, 0.024039490148425102, -0.02270696498453617, -0.068846195936203, 0.07166928052902222, 0.012198063544929028, -0.0071244980208575726, -0.029273375868797302, 0.016104958951473236, -0.11772721260786057, 0.07545888423919678, -0.061888277530670166....]
"""
