import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI



OPENROUTER_API_KEY ="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"
print(OPENROUTER_API_KEY)

chat = ChatOpenAI(
    model="mistralai/mistral-7b-instruct:free",
    temperature=0.0,
    openai_api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "https://localhost:3000", # Required for OpenRouter free models
        "X-Title": "TestApp"
    }
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
