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
