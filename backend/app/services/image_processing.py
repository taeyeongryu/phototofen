import cv2
import numpy as np

def load_image_from_bytes(image_bytes: bytes) -> np.ndarray:
    """
    Decodes image bytes into a cv2 image (numpy array).
    """
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Could not decode image")
    return img

def to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Converts a BGR image to grayscale.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def parse_fen_filename(filename: str) -> list[str]:
    """
    Parses a FEN-encoded filename (ranks separated by '-') into a list of 64 piece labels.
    Example: '1b1B1b2-....jpeg' -> ['empty', 'black_bishop', 'empty', 'white_bishop', ...]
    """
    # Remove extension if present
    base_name = filename.split('.')[0]
    ranks = base_name.split('-')
    
    piece_map = {
        'p': 'black_pawn', 'r': 'black_rook', 'n': 'black_knight', 'b': 'black_bishop', 'q': 'black_queen', 'k': 'black_king',
        'P': 'white_pawn', 'R': 'white_rook', 'N': 'white_knight', 'B': 'white_bishop', 'Q': 'white_queen', 'K': 'white_king'
    }
    
    board = []
    for rank in ranks:
        for char in rank:
            if char.isdigit():
                board.extend(['empty'] * int(char))
            else:
                board.append(piece_map.get(char, 'empty'))
    
    if len(board) != 64:
        raise ValueError(f"Invalid FEN filename: {filename} (parsed {len(board)} squares)")
        
    return board

def split_board_image(image: np.ndarray, target_size: int = 50) -> list[np.ndarray]:
    """
    Splits a 400x400 (or other square) board image into 64 square images.
    """
    height, width = image.shape[:2]
    square_h, square_w = height // 8, width // 8
    
    squares = []
    for row in range(8):
        for col in range(8):
            y1, y2 = row * square_h, (row + 1) * square_h
            x1, x2 = col * square_w, (col + 1) * square_w
            square = image[y1:y2, x1:x2]
            
            if target_size and (square_h != target_size or square_w != target_size):
                square = cv2.resize(square, (target_size, target_size))
            
            squares.append(square)
            
    return squares
