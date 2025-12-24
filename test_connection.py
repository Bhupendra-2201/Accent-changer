import requests

key = "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"

resp = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://localhost:3000",
        "X-Title": "TestApp"
    },
    json={
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [{"role": "user", "content": "Hi"}]
    }
)

print(f"Status: {resp.status_code}")
print(f"Response: {resp.text}")
