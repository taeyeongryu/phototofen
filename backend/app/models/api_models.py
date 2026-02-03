from pydantic import BaseModel
from typing import Optional
from enum import Enum

class PieceClass(str, Enum):
    EMPTY = "empty"
    # White pieces
    WHITE_PAWN = "P"
    WHITE_KNIGHT = "N"
    WHITE_BISHOP = "B"
    WHITE_ROOK = "R"
    WHITE_QUEEN = "Q"
    WHITE_KING = "K"
    # Black pieces
    BLACK_PAWN = "p"
    BLACK_KNIGHT = "n"
    BLACK_BISHOP = "b"
    BLACK_ROOK = "r"
    BLACK_QUEEN = "q"
    BLACK_KING = "k"

class AnalysisResponse(BaseModel):
    fen: str
    confidence: Optional[float] = None
    # We can add more fields later like detected_board (base64)
