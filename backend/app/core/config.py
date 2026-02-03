import os
from pathlib import Path

class ClassifierConfig:
    # Get the project root directory (backend/)
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    MODEL_PATH = os.path.join(BASE_DIR, "app", "assets", "model.pth")
    DEVICE = "cpu"  # Default to CPU, can be updated to 'cuda' or 'mps' if available
    NUM_CLASSES = 13
    INPUT_SIZE = 224  # MobileNetV2 default
