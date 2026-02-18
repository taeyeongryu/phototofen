import pytest
import os
import torch
from app.services.classifier import load_model

def test_load_model_file_not_found():
    """
    Test that load_model raises FileNotFoundError when the model file does not exist.
    """
    fake_path = "non_existent_model.pth"
    device = "cpu"
    
    with pytest.raises(FileNotFoundError):
        load_model(fake_path, device)

def test_load_model_invalid_file(tmp_path):
    """
    Test loading a corrupt or invalid file.
    """
    # Create a dummy invalid file
    invalid_file = tmp_path / "invalid_model.pth"
    invalid_file.write_text("not a torch file")
    
    with pytest.raises(Exception): 
        load_model(str(invalid_file), "cpu")

def test_load_model_singleton():
    """
    Test that load_model returns the same instance when called multiple times.
    """
    from unittest.mock import patch, MagicMock
    
    # We need to patch where _model_instance is stored
    with patch('os.path.exists') as mock_exists, \
         patch('torch.load') as mock_load, \
         patch('app.services.classifier.models.mobilenet_v2') as mock_mobilenet, \
         patch('app.services.classifier._model_instance', None): 
        
        mock_exists.return_value = True
        mock_load.return_value = {} 
        
        # Mock the model object returned by mobilenet_v2
        mock_model_obj = MagicMock()
        mock_mobilenet.return_value = mock_model_obj
        
        model1 = load_model("dummy.pth", "cpu")
        model2 = load_model("dummy.pth", "cpu")
        
        assert model1 is model2
        # mobilenet_v2 should only be called once because of the singleton pattern
        assert mock_mobilenet.call_count == 1
