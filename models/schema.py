from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class PDFUploadResponse(BaseModel):
    """Response model for PDF upload endpoint."""
    filename: str
    status: str
    pdf_id: str = Field(..., description="Unique identifier for the uploaded PDF")

class QuestionRequest(BaseModel):
    """Request model for question answering endpoint."""
    question: str = Field(..., description="The question to answer")
    pdf_id: Optional[str] = Field(None, description="Optional PDF ID to restrict the search to a specific document")

class DocumentContext(BaseModel):
    """Model for document context used in answers."""
    id: str
    text: str
    score: float
    metadata: Optional[Dict[str, Any]] = None

class QuestionResponse(BaseModel):
    """Response model for question answering endpoint."""
    query: str
    answer: str
    context: List[DocumentContext]