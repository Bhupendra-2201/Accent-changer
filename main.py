import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
import uvicorn

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="LangChain Translation API",
    description="A sophisticated API for text style translation using LangChain and OpenAI",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "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")
MODEL_NAME = "mistralai/mistral-7b-instruct:free"

# Initialize ChatOpenAI
chat = ChatOpenAI(
    model=MODEL_NAME,
    temperature=0.0,
    openai_api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "https://localhost:3000",
        "X-Title": "LangChain Translation API"
    }
)

# Request/Response Models
class TranslationRequest(BaseModel):
    message: str = Field(..., description="The text message to translate", min_length=1)
    style: str = Field(
        default="American English in a calm and respectful tone",
        description="The target style for translation"
    )

class TranslationResponse(BaseModel):
    success: bool
    original_message: str
    translated_message: str
    style: str

class HealthResponse(BaseModel):
    status: str
    message: str
    model: str

# API Endpoints
@app.get("/")
async def serve_ui():
    """Serve the web interface"""
    return FileResponse("static/index.html")

@app.get("/favicon.ico")
async def favicon():
    """Return empty response for favicon to prevent 404 errors"""
    from fastapi.responses import Response
    return Response(status_code=204)

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        message="LangChain Translation API is running",
        model=MODEL_NAME
    )

@app.post("/translate", response_model=TranslationResponse)
async def translate_text(request: TranslationRequest):
    """
    Translate text to a specified style using LangChain and OpenAI
    
    - **message**: The text to translate
    - **style**: The target style (default: "American English in a calm and respectful tone")
    """
    try:
        # Create the translation prompt
        prompt = f"""Translate the text that is delimited by triple backticks into a style that is {request.style}.
text: ```{request.message}```"""
        
        # Get translation from LangChain
        response = chat.invoke(prompt)
        
        return TranslationResponse(
            success=True,
            original_message=request.message,
            translated_message=response.content,
            style=request.style
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")

@app.get("/models")
async def list_models():
    """Get information about the current model"""
    return {
        "current_model": MODEL_NAME,
        "base_url": "https://openrouter.ai/api/v1",
        "temperature": 0.0
    }

# Run the application
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
