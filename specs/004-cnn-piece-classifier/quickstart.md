# Quickstart: CNN Piece Classifier

## Prerequisites

- Python 3.10+
- PyTorch (CPU version is sufficient for dev)
- OpenCV

## Installation

```bash
cd backend
pip install -r requirements.txt
# If torch is not in requirements yet:
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

## Setup Model

1. **Option A: Pre-trained Model**
   - Download the model weights `model_v1.pth` (link TBD).
   - Place it in `backend/app/assets/model.pth`.

2. **Option B: Train Your Own**
   - Download the "Chessman Image Dataset" from Kaggle.
   - Extract to `data/chessman`.
   - Run the training script:
     ```bash
     python scripts/train_model.py --data_dir data/chessman --epochs 10 --output backend/app/assets/model.pth
     ```

## Running the App

```bash
cd backend
uvicorn app.main:app --reload
```

## Verification

1. Use Postman or the Frontend.
2. Upload a clear image of a chessboard.
3. Check if the generated FEN is correct.
