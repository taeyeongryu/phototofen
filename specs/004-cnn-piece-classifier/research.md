# Research: CNN Piece Classifier & Improved Board Detection

## Model Architecture

### Decision: MobileNetV2 (Transfer Learning)
- **Choice**: MobileNetV2
- **Rationale**: 
  - Optimized for mobile/CPU inference (Low latency).
  - Sufficient depth for 13-class classification problem.
  - Pre-trained weights (ImageNet) available in `torchvision`, allowing for faster convergence with smaller datasets.
- **Alternatives Considered**: 
  - **ResNet18**: Standard choice, but slightly computationally heavier than MobileNetV2.
  - **Custom CNN**: Requires more data and hyperparameter tuning; transfer learning is more efficient.

## Inference Engine

### Decision: PyTorch (Native)
- **Choice**: `torch` and `torchvision`
- **Rationale**: 
  - Simplifies the stack (same lib for training and inference).
  - Performance on CPU is sufficient for the < 5s goal (batch inference of 64 squares is fast).
- **Alternatives Considered**: 
  - **ONNX Runtime**: Better performance potential, but requires an export step and managing a separate runtime dependency. Can be an optimization step later.

## Board Detection & Cropping

### Decision: Enhanced Contour + Padding
- **Choice**: Improve existing contour logic + Add vertical padding to square extraction.
- **Rationale**: 
  - The current detection logic is sound but brittle. Adding checks for aspect ratio and convexity will improve robustness.
  - The primary issue identified in User Story 2 is "tall pieces cut off". This is solved by `extract_squares` logic changes (expanding the sampling window upwards), not by changing the detection algorithm itself.
- **Alternatives Considered**: 
  - **Keypoint Regression (CNN)**: Overkill for this phase.
  - **Hough Lines**: Often noisy on complex boards.

## Data & Training

### Strategy: User-Provided Model / Training Script
- **Approach**: The system will expect a `.pth` model file. I will provide a `scripts/train_model.py` that users can run if they have a dataset (referencing common Kaggle datasets).
- **Rationale**: As an AI agent, I cannot "ship" a trained binary easily. Providing the tool to create it is the standard engineering approach.

## Clarifications Resolved
- **Dependencies**: `torch`, `torchvision`, `numpy`, `opencv-python-headless`.
- **Input Image**: The classifier expects square images, but `extract_squares` will yield slightly rectangular images (taller) due to padding. Resize/center crop will be handled in the `Dataset` transform or inference pipeline.
