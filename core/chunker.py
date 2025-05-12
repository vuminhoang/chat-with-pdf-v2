from typing import List, Optional, Dict, Any

class TextChunker:
    """
    Class for splitting text into smaller chunks for processing.
    """
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Initialize the text chunker.
        
        Args:
            chunk_size: Maximum size of each chunk in characters.
            chunk_overlap: Number of characters to overlap between chunks.
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
    
    def split_text(self, text: str) -> List[str]:
        """
        Split text into chunks.
        
        Args:
            text: The text to split.
            
        Returns:
            List of text chunks.
        """
        # Placeholder for text splitting logic
        # In a real implementation, this would handle proper splitting at sentence boundaries
        chunks = []
        for i in range(0, len(text), self.chunk_size - self.chunk_overlap):
            chunk = text[i:i + self.chunk_size]
            if chunk:
                chunks.append(chunk)
        return chunks
    
    def split_text_with_metadata(self, text: str, metadata: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Split text into chunks and include metadata with each chunk.
        
        Args:
            text: The text to split.
            metadata: Metadata to include with each chunk.
            
        Returns:
            List of dictionaries containing text chunks and metadata.
        """
        chunks = self.split_text(text)
        return [{"text": chunk, "metadata": metadata} for chunk in chunks]