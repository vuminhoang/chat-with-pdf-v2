from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router

app = FastAPI(
    title="PDF Chatter",
    description="Chat with your PDF documents using RAG (Retrieval Augmented Generation)",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include API routes
app.include_router(router, prefix="/api")


@app.get("/")
async def root():
    return {
        "message": "Welcome to PDF Chatter API",
        "docs": "/docs",
        "endpoints": {
            "upload_pdf": "/api/upload-pdf",
            "ask": "/api/ask"
        }
    }
