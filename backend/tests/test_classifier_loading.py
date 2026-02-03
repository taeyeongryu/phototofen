import pytest
from app.services.classifier import load_model

def test_load_model_file_not_found():
    """
    Test that load_model raises FileNotFoundError (or similar) when the model file does not exist.
    """
    # We pass a path that definitely doesn't exist
    fake_path = "non_existent_model.pth"
    device = "cpu"
    
    # Since the implementation isn't there yet, we expect NotImplementedError from the stub
    # But eventually we expect FileNotFoundError or a custom exception.
    # For this Phase 2 task, we just want to ensure the test structure is in place.
    
    # Once T009 is implemented, we would expect:
    # with pytest.raises(FileNotFoundError):
    #     load_model(fake_path, device)
    
    # Now that it is implemented:
    with pytest.raises(FileNotFoundError):
        load_model(fake_path, device)

def test_load_model_invalid_file():
    """
    Test loading a corrupt file.
    """
    # Placeholder for future test
    pass
