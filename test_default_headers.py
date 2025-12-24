import openai

key = "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"

# Test with default_headers in OpenAI client
client = openai.OpenAI(
    api_key=key,
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "https://localhost:3000",
        "X-Title": "TestApp"
    }
)

response = client.chat.completions.create(
    model="mistralai/mistral-7b-instruct:free",
    messages=[{"role": "user", "content": "Say hi"}]
)

print("SUCCESS!")
print(response.choices[0].message.content)
