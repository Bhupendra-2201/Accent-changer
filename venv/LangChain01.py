import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI



import httpx

OPENROUTER_API_KEY ="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"
print(OPENROUTER_API_KEY)

http_client = httpx.Client(
    headers={
        "HTTP-Referer": "https://localhost:3000",
        "X-Title": "TestApp"
    }
)

chat = ChatOpenAI(
    model="mistralai/mistral-7b-instruct:free",
    temperature=0.0,
    openai_api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

customer_email = """    
Arre, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, \
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""
style = """ American English \
in a calm and respectful tone 
"""

prompt = f"""Translate the text \
that is delimited by triple backticks into a style that is {style}.
text: ```{customer_email}``` """

# Use LangChain's predict method
response = chat.invoke(prompt)
print(response)
