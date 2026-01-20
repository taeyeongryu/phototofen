from pydantic import BaseModel
from typing import Optional

class AnalysisResponse(BaseModel):
    fen: str
    confidence: Optional[float] = None
    # We can add more fields later like detected_board (base64)
