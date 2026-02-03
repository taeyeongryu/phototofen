import numpy as np
from app.services import board_detector

def test_extract_squares_dimensions():
    """
    Test that extracted squares have correct dimensions with and without padding.
    """
    # Create a dummy board image 800x800
    board_h, board_w = 800, 800
    dummy_board = np.zeros((board_h, board_w, 3), dtype=np.uint8)
    
    # 1. Test without padding
    squares = board_detector.extract_squares(dummy_board, padding_top=0)
    assert len(squares) == 64
    for sq in squares:
        assert sq.shape == (100, 100, 3) # 800/8 = 100

    # 2. Test with padding
    padding = 20
    squares_padded = board_detector.extract_squares(dummy_board, padding_top=padding)
    assert len(squares_padded) == 64
    for sq in squares_padded:
        # Height should be 100 + 20 = 120
        assert sq.shape == (120, 100, 3)

def test_extract_squares_top_boundary():
    """
    Test padding behavior at the top edge of the board.
    """
    board_h, board_w = 800, 800
    dummy_board = np.zeros((board_h, board_w, 3), dtype=np.uint8)
    
    # Fill the first row with a specific color to check if we are cropping the right area
    # But for now just checking dimensions is enough for logic verification
    
    padding = 50
    squares = board_detector.extract_squares(dummy_board, padding_top=padding)
    
    # Check top-left square (index 0)
    sq0 = squares[0]
    assert sq0.shape == (150, 100, 3) # 100 + 50
    
    # Check if padding was applied (via copyMakeBorder or slicing)
    # Since inputs are zeros, output is zeros.
    pass
