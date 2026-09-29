from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
from typing import TypedDict, Annotated, Optional, Literal

from pydantic import Field, BaseModel

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")


# schema
class Review(BaseModel):

    key_themes: list[str] = Field(
        description="Discuss the keythemes discussed in the review in list"
    )

    summary: str = Field(description="brief overview of the review")
    sentiment: Literal["pos", "neg"] = Field(
        description="Sentiment of the review,either positive or negative"
    )
    pros: Optional[list[str]] = Field(
        description="write down all pros in a list", default=None
    )
    cons: Optional[list[str]] = Field(
        description="write down all cons in a list", default=None
    )
    name: Optional[str] = Field(
        default=None, description="write the name of the reviewer"
    )


structured_model = model.with_structured_output(Review)
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

# jaise object ko access karte hain!
print(result.name)
