import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
import numpy as np

client = TestClient(app)

@pytest.fixture
def mock_image_processing():
    with patch('app.services.image_processing.load_image_from_bytes') as mock:
        mock.return_value = np.zeros((800, 800, 3), dtype=np.uint8)
        yield mock

@pytest.fixture
def mock_board_detector():
    with patch('app.services.board_detector.detect_board') as mock_detect:
        # Return a simple 80x80 image for mocking "warped board"
        mock_detect.return_value = np.zeros((80, 80, 3), dtype=np.uint8)
        with patch('app.services.board_detector.extract_squares') as mock_extract:
            # Return 64 small images
            mock_extract.return_value = [np.zeros((10, 10, 3), dtype=np.uint8) for _ in range(64)]
            yield mock_detect, mock_extract

@pytest.fixture
def mock_piece_classifier():
    with patch('app.services.piece_classifier.classify_square') as mock:
        # Return mostly empty
        mock.side_effect = lambda sq: '1' 
        yield mock

def test_analyze_endpoint(mock_image_processing, mock_board_detector, mock_piece_classifier):
    # Create a dummy image file
    file_content = b"fake image content"
    files = {"file": ("test.jpg", file_content, "image/jpeg")}
    
    response = client.post("/api/analyze", files=files)
    
    assert response.status_code == 200
    data = response.json()
    assert "fen" in data
    # With all '1', we expect "8/8/8/8/8/8/8/8 w - - 0 1"
    assert data["fen"] == "8/8/8/8/8/8/8/8 w - - 0 1"
    assert data["confidence"] == 0.8

def test_analyze_endpoint_with_active_color_black(mock_image_processing, mock_board_detector, mock_piece_classifier):
    # Create a dummy image file
    file_content = b"fake image content"
    files = {"file": ("test.jpg", file_content, "image/jpeg")}
    data = {"active_color": "b"}
    
    response = client.post("/api/analyze", files=files, data=data)
    
    assert response.status_code == 200
    res_data = response.json()
    assert "fen" in res_data
    # Expect 'b' in the FEN string
    assert res_data["fen"] == "8/8/8/8/8/8/8/8 b - - 0 1"
