import numpy as np
from app.services import classifier
from app.models.api_models import PieceClass
import logging

logger = logging.getLogger(__name__)

# List of classes sorted alphabetically (as ImageFolder does)
CLASS_NAMES = [
    "black_bishop", "black_king", "black_knight", "black_pawn", "black_queen", "black_rook",
    "empty",
    "white_bishop", "white_king", "white_knight", "white_pawn", "white_queen", "white_rook"
]

# Map these folder names to PieceClass values
NAME_TO_ENUM = {
    "black_bishop": PieceClass.BLACK_BISHOP,
    "black_king": PieceClass.BLACK_KING,
    "black_knight": PieceClass.BLACK_KNIGHT,
    "black_pawn": PieceClass.BLACK_PAWN,
    "black_queen": PieceClass.BLACK_QUEEN,
    "black_rook": PieceClass.BLACK_ROOK,
    "empty": PieceClass.EMPTY,
    "white_bishop": PieceClass.WHITE_BISHOP,
    "white_king": PieceClass.WHITE_KING,
    "white_knight": PieceClass.WHITE_KNIGHT,
    "white_pawn": PieceClass.WHITE_PAWN,
    "white_queen": PieceClass.WHITE_QUEEN,
    "white_rook": PieceClass.WHITE_ROOK,
}

def classify_square(square_image: np.ndarray) -> PieceClass:
    """
    Classifies a single square image using the CNN model.
    Returns PieceClass enum.
    """
    try:
        # We try to use the general predict function from classifier service
        # This allows piece_classifier to be the specific application logic
        class_idx = classifier.predict(square_image)
        
        if 0 <= class_idx < len(CLASS_NAMES):
            predicted_label = CLASS_NAMES[class_idx]
            return NAME_TO_ENUM.get(predicted_label, PieceClass.EMPTY)
            
    except Exception as e:
        logger.error(f"Error in piece classification: {e}")
        # Fallback to legacy heuristic or just return EMPTY
        # For now, let's return EMPTY to avoid crashing the pipeline
        return PieceClass.EMPTY

    return PieceClass.EMPTY
