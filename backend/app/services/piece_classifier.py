import cv2
import numpy as np

def classify_square(square_image: np.ndarray) -> str:
    """
    Classifies a single square image using basic heuristics.
    Returns FEN character or '1' (empty).
    """
    if square_image.size == 0:
        return '1'

    # Convert to gray for analysis
    gray = cv2.cvtColor(square_image, cv2.COLOR_BGR2GRAY)
    
    # Check if empty (low variance)
    # This is a very naive heuristic.
    mean, stddev = cv2.meanStdDev(gray)
    
    m_val = mean[0][0]
    s_val = stddev[0][0]
    
    # Thresholds are arbitrary and would need calibration
    is_empty = s_val < 30
    result = '1'
    
    if is_empty:
        result = '1'
    else:
        # If it is a piece, determine color based on brightness
        if m_val > 100:
            result = 'P' # White Pawn placeholder
        else:
            result = 'p' # Black Pawn placeholder

    print(f"[DEBUG] Square Mean={m_val:.2f}, StdDev={s_val:.2f} -> Result='{result}'")
    return result
