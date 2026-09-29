from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

# import torch

os.environ["HF_HOME"] = "D:/huggingface_cache"
# device = 0 if torch.cuda.is_available() else -1
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    # device = device,
    pipeline_kwargs=dict(max_new_tokens=15, temperature=0.5),
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("who is radha krishna?")
print(result.content)

# dowload hongi files on ram
# gpu se fast hoga inference
# Start-Process code -Verb RunAs:run as administrator to get acces sof D drive
"""
<|user|>
who is radha krishna?</s>
<|assistant|>
Radha Krishna is a popular Hindu deity
"""
