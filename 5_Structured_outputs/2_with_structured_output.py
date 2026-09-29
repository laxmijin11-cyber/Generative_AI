from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
from typing import TypedDict, Annotated, Optional, Literal

model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")


# schema
class Review(TypedDict):

    key_themes: Annotated[
        list[str], "Discuss the keythemes discussed in the review in list"
    ]
    summary: Annotated[str, "brief overview of the review"]
    # sentiment: Annotated[
    #     str, "Sentiment of the review,either positive,neutral or negative"
    # ]
    sentiment: Annotated[
        Literal["pos", "neg"],
        "Sentiment of the review,either positive or negative",
    ]
    pros: Annotated[Optional[list[str]], "write down all pros ijn a list"]
    cons: Annotated[Optional[list[str]], "write down all cons ijn a list"]
    name: Annotated[Optional[str], "name of the reviewer"]


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
# print(result)
# print(result["summary"])
print(result["sentiment"])
print(result.keys())
print(result["name"])

# summary can return str or anything else there is no guarantee hence its an issue
# no data validation
# literal usee to have options pos or neg
