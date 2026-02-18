import kagglehub
import os
import argparse

def download_dataset():
    print("Downloading koryakinp/chess-positions dataset from Kaggle...")
    path = kagglehub.dataset_download('koryakinp/chess-positions')
    print(f"Dataset downloaded to: {path}")
    return path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download Kaggle chess positions dataset.")
    parser.add_argument("--output", type=str, help="Target directory (not strictly used by kagglehub which uses cache)")
    args = parser.parse_args()
    
    download_dataset()
