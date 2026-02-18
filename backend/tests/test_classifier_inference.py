import pytest
from unittest.mock import MagicMock, patch
import numpy as np
import torch
from torchvision import transforms
from app.services import classifier, piece_classifier
from app.models.api_models import PieceClass

@pytest.fixture
def mock_model():
    model = MagicMock()
    model.eval.return_value = None
    return model

@pytest.fixture(autouse=True)
def setup_classifier_transform():
    # Set a dummy transform for all tests in this module
    classifier._model_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    yield
    # Reset after tests
    classifier._model_transform = None

@patch('app.services.classifier.load_model')
def test_classify_square_inference(mock_load_model, mock_model):
    """
    Test the full inference flow with mocked model.
    """
    # Setup mock
    mock_load_model.return_value = mock_model
    
    # Create dummy output tensor (batch_size=1, num_classes=13)
    # List: black_bishop, black_king, black_knight, black_pawn, black_queen, black_rook,
    #       empty,
    #       white_bishop, white_king, white_knight, white_pawn, white_queen, white_rook
    
    # "white_pawn" is at index 10
    dummy_output = torch.randn(1, 13)
    dummy_output[0, 10] = 10.0 # Make it the max
    
    mock_model.return_value = dummy_output
    
    # Create a dummy image (224, 224, 3)
    dummy_image = np.zeros((224, 224, 3), dtype=np.uint8)
    
    # Run classification
    result = piece_classifier.classify_square(dummy_image)
    
    # Verify
    assert result == PieceClass.WHITE_PAWN
    mock_load_model.assert_called_once()
    mock_model.assert_called_once() # Called with input tensor

@patch('app.services.classifier.load_model')
def test_classify_square_empty(mock_load_model, mock_model):
    """
    Test prediction of empty square.
    """
    mock_load_model.return_value = mock_model
    
    # 'empty' is index 6
    dummy_output = torch.randn(1, 13)
    dummy_output[0, 6] = 10.0
    
    mock_model.return_value = dummy_output
    dummy_image = np.zeros((50, 50, 3), dtype=np.uint8)
    
    result = piece_classifier.classify_square(dummy_image)
    
    assert result == PieceClass.EMPTY
