# LangChain Translation API

A sophisticated FastAPI application that translates text into different styles using LangChain and OpenAI/OpenRouter.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
.\venv\Scripts\pip install -r requirements.txt
```

### 2. Run the Server
```bash
.\venv\Scripts\python.exe main.py
```

The server will start at `http://localhost:8000`

## 📚 API Documentation

Once running, visit:
- **Interactive API Docs**: `http://localhost:8000/docs`
- **Alternative Docs**: `http://localhost:8000/redoc`

## 🎯 Endpoints

### `GET /`
Health check endpoint
```json
{
  "status": "healthy",
  "message": "LangChain Translation API is running",
  "model": "mistralai/mistral-7b-instruct:free"
}
```

### `POST /translate`
Translate text to a specified style
```json
{
  "message": "Your text here",
  "style": "American English in a calm and respectful tone"
}
```

Response:
```json
{
  "success": true,
  "original_message": "Your text here",
  "translated_message": "Translated text...",
  "style": "American English in a calm and respectful tone"
}
```

### `GET /models`
Get current model information

## 📝 Example Usage

### Using curl
```bash
curl -X POST "http://localhost:8000/translate" \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Arre, I be fuming!\", \"style\": \"Professional business English\"}"
```

### Using Python
```python
import requests

response = requests.post(
    "http://localhost:8000/translate",
    json={
        "message": "Arre, I be fuming!",
        "style": "Professional business English"
    }
)
print(response.json())
```

## 🛠️ Tech Stack
- **FastAPI**: Modern web framework
- **LangChain**: AI orchestration
- **OpenRouter**: LLM API gateway
- **Pydantic**: Data validation
- **Uvicorn**: ASGI server

## 📂 Project Structure
```
.
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── .env                # Environment variables (create this)
├── .gitignore          # Git ignore rules
└── venv/               # Virtual environment
```

## 🔑 Environment Variables
Create a `.env` file with:
```
OPENROUTER_API_KEY=your_api_key_here
```

---
**Built with ❤️ using FastAPI and LangChain**
