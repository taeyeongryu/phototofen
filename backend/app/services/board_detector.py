import cv2
import numpy as np
from typing import List

class BoardDetectionError(Exception):
    pass

def _order_points(pts: np.ndarray) -> np.ndarray:
    """
    Orders coordinates: top-left, top-right, bottom-right, bottom-left.
    """
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

def detect_board(image: np.ndarray) -> np.ndarray:
    """
    Detects the chessboard in the image and returns a top-down view (warped).
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Use Canny and adaptive thresholding to be robust
    edges = cv2.Canny(blur, 50, 150, apertureSize=3)
    
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Sort by area, largest first
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    
    board_contour = None
    
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        
        # We assume the board is a quadrilateral
        if len(approx) == 4:
            board_contour = approx
            print(f"[DEBUG] Board contour found. Area: {cv2.contourArea(c)}")
            break
            
    if board_contour is None:
        print("[DEBUG] No board contour found.")
        raise BoardDetectionError("Could not detect a chessboard in the image.")
        
    # Reshape contour to (4, 2)
    pts = board_contour.reshape(4, 2)
    rect = _order_points(pts)
    
    # Determine width and height of new image
    (tl, tr, br, bl) = rect
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    
    # Construct destination points
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")
        
    # Perspective transform
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    
    return warped

def extract_squares(board_image: np.ndarray) -> List[np.ndarray]:
    """
    Splits the board image into 64 squares.
    Returns a list of 64 images (top-left to bottom-right).
    """
    h, w = board_image.shape[:2]
    sq_h = h // 8
    sq_w = w // 8
    
    squares = []
    for row in range(8):
        for col in range(8):
            y1 = row * sq_h
            y2 = (row + 1) * sq_h
            x1 = col * sq_w
            x2 = (col + 1) * sq_w
            square = board_image[y1:y2, x1:x2]
            squares.append(square)
    return squares
