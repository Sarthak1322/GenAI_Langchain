from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

st.header("Research Tool")

paper_input = st.selectbox("Select Research Paper Name",[
   "Select...", "Attention Is All You Need", "BERT: Pre-training of Deep Bidirection Transformers", 
   "GPT-3: Language Models are Few-Shot Learners"
])

style_input = st.selectbox("Select Explanation Style", ["Select...",
   "Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"
])

length_input = st.selectbox("Select Explanation Style", ["Select...",
   "Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"
])

# template
template = PromptTemplate(
   template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical Details:
    - Include relevant mathematical equations if present in the paper.
    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
2. Analogies:
    - Use relatable analogies to simplify complex idea.
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_input', 'style_input', 'length_input']
)

# fill the placeholder
prompt = template.invoke({
   'paper_input' : paper_input,
   'style_input' : style_input,
   'length_input' : length_input

})

if st.button('Summarize'):
   result = model.invoke(prompt)
   st.write(result.content)
