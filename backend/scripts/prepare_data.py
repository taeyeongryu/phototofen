import cv2
import os
import argparse
import random
import shutil
from pathlib import Path
from tqdm import tqdm
from app.services.image_processing import parse_fen_filename, split_board_image

def prepare_data(input_dir: str, output_dir: str, num_boards: int = 1000, split_ratio: float = 0.8):
    """
    Processes board images into individual piece images categorized by type.
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Define class names
    classes = [
        'white_pawn', 'white_knight', 'white_bishop', 'white_rook', 'white_queen', 'white_king',
        'black_pawn', 'black_knight', 'black_bishop', 'black_rook', 'black_queen', 'black_king',
        'empty'
    ]
    
    # Create directory structure
    for split in ['train', 'val']:
        for cls in classes:
            (output_path / split / cls).mkdir(parents=True, exist_ok=True)
            
    # Get all image files
    all_images = list(input_path.glob("*.jpeg")) + list(input_path.glob("*.jpg"))
    if not all_images:
        print(f"No images found in {input_dir}")
        return
        
    random.shuffle(all_images)
    all_images = all_images[:num_boards]
    
    # Process images
    print(f"Processing {len(all_images)} board images...")
    
    processed_count = 0
    error_count = 0
    
    for board_idx, board_file in enumerate(tqdm(all_images)):
        try:
            # Determine split
            split = 'train' if random.random() < split_ratio else 'val'
            
            # Load image
            img = cv2.imread(str(board_file))
            if img is None:
                raise ValueError(f"Could not read image: {board_file}")
                
            # Parse FEN and split image
            piece_labels = parse_fen_filename(board_file.name)
            squares = split_board_image(img, target_size=50)
            
            # Save individual pieces
            for i, (square, label) in enumerate(zip(squares, piece_labels)):
                piece_filename = f"{board_file.stem}_sq{i:02d}.jpg"
                save_path = output_path / split / label / piece_filename
                cv2.imwrite(str(save_path), square)
                
            processed_count += 1
            
        except Exception as e:
            # print(f"Error processing {board_file.name}: {e}")
            error_count += 1
            
    print(f"Preprocessing complete. Processed: {processed_count}, Errors: {error_count}")
    print(f"Results saved to: {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prepare dataset for training piece classifier.")
    parser.add_argument("--input-dir", type=str, required=True, help="Directory containing raw board images.")
    parser.add_argument("--output-dir", type=str, required=True, help="Directory to save processed piece images.")
    parser.add_argument("--num-boards", type=int, default=1000, help="Number of board images to process.")
    parser.add_argument("--split-ratio", type=float, default=0.8, help="Ratio of images for training (0 to 1).")
    args = parser.parse_args()
    
    prepare_data(args.input_dir, args.output_dir, args.num_boards, args.split_ratio)
