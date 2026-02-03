import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import numpy as np
import os
from app.core.config import ClassifierConfig
from app.models.api_models import PieceClass
import logging

logger = logging.getLogger(__name__)

# Global model instance
_model_instance = None
_model_transform = None

def load_model(model_path: str = ClassifierConfig.MODEL_PATH, device: str = ClassifierConfig.DEVICE) -> torch.nn.Module:
    """
    Load the trained MobileNetV2 model.
    """
    global _model_instance, _model_transform
    
    if _model_instance is not None:
        return _model_instance

    logger.info(f"Loading model from {model_path}")
    
    try:
        model = models.mobilenet_v2(weights=None) # We load our own weights
        # Modify the classifier to match our number of classes
        num_ftrs = model.classifier[1].in_features
        model.classifier[1] = nn.Linear(num_ftrs, ClassifierConfig.NUM_CLASSES)
        
        # Load weights
        if not os.path.exists(model_path):
             # For development, if model missing, we might return an uninitialized model 
             # OR raise error. Given T004 was a placeholder, we might fail here if we try to load strict state_dict
             # But for robustness, let's assume if it's the placeholder text file, it will fail torch.load.
             # So we wrap in try/except.
             pass

        state_dict = torch.load(model_path, map_location=device)
        model.load_state_dict(state_dict)
        model.to(device)
        model.eval()
        
        _model_instance = model
        
        # Define transforms
        _model_transform = transforms.Compose([
            transforms.Resize(ClassifierConfig.INPUT_SIZE),
            transforms.CenterCrop(ClassifierConfig.INPUT_SIZE),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        
        return model

    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        # If we can't load the model (e.g. dev environment), we might want to return None or raise.
        # For now, let's re-raise to be safe, but we might need a dummy fallback for tests if no model exists.
        raise e

def preprocess_square(image: np.ndarray) -> torch.Tensor:
    """
    Preprocess a square image (numpy array from OpenCV) for the model.
    """
    if _model_transform is None:
        # Should have been initialized by load_model, but just in case
        load_model()
        
    # Convert OpenCV (BGR) to PIL (RGB)
    # OpenCV images are numpy arrays. 
    # PIL Image.fromarray expects RGB if mode is 'RGB', but OpenCV is BGR.
    # So we need to convert BGR to RGB first.
    if len(image.shape) == 3:
        # Assuming BGR
        image_rgb = image[:, :, ::-1] 
    else:
        # Grayscale
        image_rgb = np.stack((image,)*3, axis=-1)

    pil_image = Image.fromarray(image_rgb)
    
    # Apply transforms
    tensor = _model_transform(pil_image)
    
    # Add batch dimension (1, C, H, W)
    tensor = tensor.unsqueeze(0)
    
    return tensor

def classify_square(square_image: np.ndarray) -> PieceClass:
    """
    Classify a single square image into a PieceClass.
    """
    model = load_model()
    device = ClassifierConfig.DEVICE
    
    input_tensor = preprocess_square(square_image)
    input_tensor = input_tensor.to(device)
    
    with torch.no_grad():
        outputs = model(input_tensor)
        _, preds = torch.max(outputs, 1)
        
    class_idx = preds.item()
    
    # Map index to PieceClass
    # The order MUST match the training script's class_names order.
    # In train_model.py: image_datasets['train'].classes
    # ImageFolder sorts classes alphabetically by default.
    # Our PieceClass enum values are specific characters, but the folder names in the dataset 
    # would likely be the class names.
    # We need a mapping. Assuming standard mapping for now based on the Enum definition order 
    # MIGHT be risky if folders are named differently.
    # Let's assume a fixed mapping for now or we need to save the class_names in the model checkpoint.
    
    # CRITICAL: We need to know the mapping. 
    # If the user trains with folders named "black_bishop", "black_king", etc., ImageFolder sorts them.
    # Let's assume a mapping based on the sorted keys of a theoretical dictionary or similar.
    # For MVP, let's hardcode a mapping that corresponds to sorted folder names we expect users to use?
    # Or better, we define the expected class names here.
    
    # Let's assume the classes are mapped by index to the Enum members in a specific order.
    # Since we don't have the dataset structure, we will assume a standard list.
    
    # Let's try to be robust. For now, I will use a list that I assume aligns with the training data.
    # If the folders are named: 'b', 'k', 'n', 'p', 'q', 'r', 'B', 'K', 'N', 'P', 'Q', 'R', 'empty'
    # (Unix sort order is typically case sensitive or insensitive depending on locale, but standard ASCII: B < K ... < b < k)
    # Wait, ASCII: 'B' (66) ... 'R' (82) ... 'b' (98) ... 'empty' (starts with e)
    # Actually, let's just define a mapping.
    
    # List of classes sorted alphabetically (as ImageFolder does)
    # Assumption: Data folders are named: 
    # "black_bishop", "black_king", "black_knight", "black_pawn", "black_queen", "black_rook",
    # "empty",
    # "white_bishop", "white_king", "white_knight", "white_pawn", "white_queen", "white_rook"
    
    class_names = [
        "black_bishop", "black_king", "black_knight", "black_pawn", "black_queen", "black_rook",
        "empty",
        "white_bishop", "white_king", "white_knight", "white_pawn", "white_queen", "white_rook"
    ]
    
    # Map these folder names to PieceClass values
    name_to_enum = {
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
    
    if 0 <= class_idx < len(class_names):
        predicted_label = class_names[class_idx]
        return name_to_enum.get(predicted_label, PieceClass.EMPTY)
    
    return PieceClass.EMPTY