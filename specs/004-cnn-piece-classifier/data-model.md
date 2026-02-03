# Data Model: CNN Piece Classifier

## Entities

### ClassifierConfig
Configuration for the CNN model.
- **model_path**: `str` (Path to the .pth file)
- **input_size**: `int` (Size to resize input images to, e.g., 224)
- **device**: `str` (cpu or cuda)
- **confidence_threshold**: `float` (Minimum confidence to accept a prediction, else Empty?)

### PredictionResult
Result of classifying a single square.
- **class_id**: `int` (0-12)
- **label**: `PieceClass`
- **confidence**: `float` (0.0 - 1.0)

## Enums

### PieceClass
Mapping of model output indices to piece types.
- 0: Empty
- 1: White Pawn
- 2: White Knight
- 3: White Bishop
- 4: White Rook
- 5: White Queen
- 6: White King
- 7: Black Pawn
- 8: Black Knight
- 9: Black Bishop
- 10: Black Rook
- 11: Black Queen
- 12: Black King

## Transformations

### Image Preprocessing
Steps applied to a `SquareImage` before inference:
1. Resize to `input_size` x `input_size`
2. Convert to Tensor
3. Normalize (mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]) - Standard ImageNet stats
