import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import numpy as np
import os
from app.core.config import ClassifierConfig
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
             raise FileNotFoundError(f"Model file not found at {model_path}")

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
        raise e

def preprocess_square(image: np.ndarray) -> torch.Tensor:
    """
    Preprocess a square image (numpy array from OpenCV) for the model.
    """
    if _model_transform is None:
        load_model()
        
    # Convert OpenCV (BGR) to PIL (RGB)
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

def predict(square_image: np.ndarray) -> int:
    """
    Predict the class index for a single square image.
    """
    model = load_model()
    device = ClassifierConfig.DEVICE
    
    input_tensor = preprocess_square(square_image)
    input_tensor = input_tensor.to(device)
    
    with torch.no_grad():
        outputs = model(input_tensor)
        _, preds = torch.max(outputs, 1)
        
    return preds.item()
