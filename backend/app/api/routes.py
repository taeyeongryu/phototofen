from fastapi import APIRouter, UploadFile, File, HTTPException
from app.models.api_models import AnalysisResponse
from app.services import image_processing, board_detector, piece_classifier, fen_generator

router = APIRouter()

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_puzzle(file: UploadFile = File(...)):
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")
    
    try:
        # 1. Read bytes
        contents = await file.read()
        
        # 2. Decode image
        image = image_processing.load_image_from_bytes(contents)
        
        # 3. Detect board
        warped_board = board_detector.detect_board(image)
        
        # 4. Extract squares
        squares = board_detector.extract_squares(warped_board)
        
        # 5. Classify pieces
        pieces = [piece_classifier.classify_square(sq) for sq in squares]
        
        # 6. Generate FEN
        fen = fen_generator.generate_fen(pieces)
        
        return AnalysisResponse(
            fen=fen,
            confidence=0.8
        )
        
    except board_detector.BoardDetectionError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        # General error handling for now
        print(f"Error processing image: {e}")
        raise HTTPException(status_code=500, detail="Internal server error during processing.")
