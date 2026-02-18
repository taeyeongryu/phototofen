import torch
import torch.nn as nn
from app.services.classifier import load_model
from app.core.config import ClassifierConfig
from unittest.mock import patch, MagicMock

def test_model_architecture():
    """
    Test that the loaded model has the expected MobileNetV2 architecture with correct output size.
    """
    # We patch _model_instance to ensure a fresh load for this test
    with (
        patch('os.path.exists') as mock_exists,
        patch('torch.load') as mock_load,
        patch('app.services.classifier._model_instance', None)
    ):
        mock_exists.return_value = True
        # Mocking a minimal state dict to avoid load errors
        with patch('torch.nn.Module.load_state_dict') as mock_lsd:
            model = load_model("dummy.pth", "cpu")
            
            # Check output features
            assert isinstance(model.classifier[1], nn.Linear)
            assert model.classifier[1].out_features == ClassifierConfig.NUM_CLASSES

def test_model_input_output_shapes():
    """
    Verify model can handle expected input tensor shape and produces correct output shape.
    """
    with (
        patch('os.path.exists') as mock_exists,
        patch('torch.load') as mock_load,
        patch('app.services.classifier._model_instance', None)
    ):
        mock_exists.return_value = True
        with patch('torch.nn.Module.load_state_dict') as mock_lsd:
            model = load_model("dummy.pth", "cpu")
            
            # Create a dummy input (B, C, H, W)
            dummy_input = torch.randn(1, 3, ClassifierConfig.INPUT_SIZE, ClassifierConfig.INPUT_SIZE)
            
            with torch.no_grad():
                output = model(dummy_input)
                
            assert output.shape == (1, ClassifierConfig.NUM_CLASSES)
