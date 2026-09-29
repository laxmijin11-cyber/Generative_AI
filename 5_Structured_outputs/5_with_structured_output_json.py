from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
from typing import TypedDict, Annotated, Optional, Literal

from pydantic import Field, BaseModel

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")


# schema
json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {"type": "array", "items": {"type": "string"}},
        "summary": {"type": "string", "description": "A rief summmary of the review"},
        "sentiment": {
            "type": "string",
            "enum": ["pos", "neg"],
            "description": "Return sentiment of the review either negative,positive or neutral",
        },
        "pros": {
            "type": ["array", "null"],
            "items": {"type": "string"},
            "description": "write down all pros in list",
        },
        "cons": {
            "type": ["array", "null"],
            "items": {"type": "string"},
            "description": "write the names of all cons in a list",
        },
        "name": {
            "type": ["string", "null"],
            "description": "write the name of reviewer",
        },
    },
    "required": ["key_themes", "summary", "sentiment"],
}

structured_model = model.with_structured_output(json_schema)
result = structured_model.invoke("""
                    Overview
The OnePlus Nord 5 is a mid‑range smartphone launched in 2025, positioned as a performance‑focused upgrade over the Nord 4. It introduces a new design, a high‑refresh‑rate display, and a Snapdragon 8‑series chipset, making it one of the most powerful devices in its segment. 
Pros
Excellent performance for gaming
Smooth and bright 144Hz display
Strong battery life and fast charging
Clean and feature‑rich OxygenOS experience
Cons
Cameras not the best in the segment
Large and heavier than rivals
Glass design less distinctive than Nord 4’s metal build
91mobiles.com
91mobiles.com
Verdict
The OnePlus Nord 5 is a top choice for users prioritizing performance, gaming, and display quality. However, those seeking the best camera performance or a more compact design may find better alternatives in the same price range.

""")
print(result)

# literal use nahi karte,use enum
# yaha output is dictionary like typeddict not pydantic object
