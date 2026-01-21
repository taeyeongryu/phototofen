import pytest
import os
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Path relative to the execution root (usually project root)
FAILING_IMAGE_PATH = "backend/tests/data/failing_board.jpg"

# TODO: Update this with the actual expected FEN from the user
# For now, we mainly want to ensure it's NOT the empty board if it's supposed to be populated.
EMPTY_BOARD_FEN = "8/8/8/8/8/8/8/8 w - - 0 1"

@pytest.mark.skipif(not os.path.exists(FAILING_IMAGE_PATH), reason="Failing image not found")
def test_failing_image_fen_generation():
    """
    Regression test for the issue where populated boards return an empty board FEN.
    """
    with open(FAILING_IMAGE_PATH, "rb") as f:
        response = client.post("/api/analyze", files={"file": ("failing_board.jpg", f, "image/jpeg")})
    
    assert response.status_code == 200
    data = response.json()
    assert "fen" in data
    
    generated_fen = data["fen"]
    print(f"Generated FEN: {generated_fen}")
    
    # The core issue is that it returns an empty board for a populated one.
    # So the first assertion is that it is NOT an empty board.
    assert generated_fen != EMPTY_BOARD_FEN, "Generated FEN should not be an empty board for the failing test case."
    
    # Once we have the expected FEN, we can add a stricter assertion:
    # assert generated_fen == EXPECTED_FEN
