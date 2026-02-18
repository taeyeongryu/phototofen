import pytest
import numpy as np
import cv2
import os
from pathlib import Path
from app.services.image_processing import parse_fen_filename, split_board_image
from scripts.prepare_data import prepare_data

def test_parse_fen_filename_valid():
    filename = "1b1B1b2-3r4-8-8-8-8-8-8.jpeg"
    expected_start = ['empty', 'black_bishop', 'empty', 'white_bishop', 'empty', 'black_bishop', 'empty', 'empty']
    expected_second_rank = ['empty', 'empty', 'empty', 'black_rook', 'empty', 'empty', 'empty', 'empty']
    
    board = parse_fen_filename(filename)
    assert len(board) == 64
    assert board[0:8] == expected_start
    assert board[8:16] == expected_second_rank
    assert board[16:64] == ['empty'] * 48

def test_parse_fen_filename_invalid():
    with pytest.raises(ValueError):
        parse_fen_filename("invalid-fen.jpeg")

def test_split_board_image():
    # Create a 400x400 dummy image
    image = np.zeros((400, 400, 3), dtype=np.uint8)
    cv2.rectangle(image, (0, 0), (49, 49), (255, 255, 255), -1)
    
    squares = split_board_image(image, target_size=50)
    assert len(squares) == 64
    assert squares[0].shape == (50, 50, 3)
    assert np.mean(squares[0]) > 0
    assert np.mean(squares[1]) == 0

def test_split_board_image_resize():
    # Create an 800x800 image
    image = np.zeros((800, 800, 3), dtype=np.uint8)
    squares = split_board_image(image, target_size=50)
    assert len(squares) == 64
    assert squares[0].shape == (50, 50, 3)

def test_full_preprocessing_flow(tmp_path):
    """
    Integration test for the full data preparation script.
    """
    # 1. Setup mock data
    input_dir = tmp_path / "raw"
    input_dir.mkdir()
    output_dir = tmp_path / "processed"
    
    # Create 2 mock board images with different FEN filenames
    filenames = [
        "8-8-8-8-8-8-8-P7.jpeg", # Last square is white pawn
        "k7-8-8-8-8-8-8-8.jpeg"  # First square is black king
    ]
    
    for filename in filenames:
        board_image = np.zeros((400, 400, 3), dtype=np.uint8)
        if 'P' in filename:
            # Draw white pawn in the last square (h1)
            cv2.rectangle(board_image, (350, 350), (399, 399), (255, 255, 255), -1)
        else:
            # Draw black king in the first square (a8)
            cv2.rectangle(board_image, (0, 0), (49, 49), (128, 128, 128), -1)
            
        cv2.imwrite(str(input_dir / filename), board_image)
    
    # 2. Run prepare_data with split_ratio=1.0 for training focus
    prepare_data(str(input_dir), str(output_dir), num_boards=2, split_ratio=1.0)
    
    # 3. Verify directory structure and content
    train_dir = output_dir / "train"
    assert (train_dir / "white_pawn").exists()
    assert (train_dir / "black_king").exists()
    assert (train_dir / "empty").exists()
    
    # Check counts
    white_pawn_images = list((train_dir / "white_pawn").glob("*.jpg"))
    black_king_images = list((train_dir / "black_king").glob("*.jpg"))
    empty_images = list((train_dir / "empty").glob("*.jpg"))
    
    assert len(white_pawn_images) == 1
    assert len(black_king_images) == 1
    assert len(empty_images) == 126 # (64-1) + (64-1) = 126
