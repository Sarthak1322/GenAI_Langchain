from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatOpenAI()

# schema
# here we give all the below field for all the field like summary, sentiment, pros....
json_schema = {
    "title":"student",
    "description":"schema about students",
    "type":"ogject",
    "properties":{
        "key_theme": {
            "type": "string"
        },
        "description": "write down all the key themes discussed in the review in a list"
    },
    "summary": {

    },
    "pros":{

    },
    
}

structured_model = model.with_structured_output(json_schema)


result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that i can't remove. 
             Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.

             """)

print(result.summary)
