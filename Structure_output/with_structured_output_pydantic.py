from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatOpenAI()

# schema
# understand all the field in the Review are their in result , i had not written , be smart to understand
class Review(BaseModel):
    Key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str =  Field(description="Write down all the key themes discussed in the review in a list")
    sentiment: Literal["pos", "neg"] =  Field(description="Write down all the key themes discussed in the review in a list")
    pros: Optional[list[str]] =  Field(default=None, description="Write down all the key themes discussed in the review in a list")





    summary: str
    # summary : Annotated[str, "A brief summary of the review"]
    sentiment: str

structured_model = model.with_structured_output(Review)


result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that i can't remove. 
             Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.

             """)

print(result.summary)
