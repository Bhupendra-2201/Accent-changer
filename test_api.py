dimport requests

# Test the API
response = requests.post(
    "http://localhost:8000/translate",
    json={
        "message": "Arre, I be fuming that me blender lid flew off!",
        "style": "Professional business English"
    }
)

result = response.json()
print("\n✅ Translation Result:")
print(f"Original: {result['original_message']}")
print(f"Translated: {result['translated_message']}")
print(f"Style: {result['style']}")
