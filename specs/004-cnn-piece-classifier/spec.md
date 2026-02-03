# Feature Specification: CNN Piece Classifier & Improved Board Detection

**Feature Branch**: `004-cnn-piece-classifier`  
**Created**: 2026-01-25  
**Status**: Draft  
**Input**: User description: "Replace heuristic classifier with CNN model and improve board detection"

## User Scenarios & Testing

### User Story 1 - Accurate Piece Classification (Priority: P1)

As a user, I want the system to accurately identify the piece type (King, Queen, Rook, Bishop, Knight, Pawn) and color (White, Black) or identify the square as empty, so that the generated FEN string correctly represents the physical board state.

**Why this priority**: The core value of the application is converting photos to FEN. The current heuristic approach fails frequently, making the app unusable for real games.

**Independent Test**: Can be tested by feeding a set of individual square images to the classifier service and verifying the predicted class matches the actual piece.

**Acceptance Scenarios**:

1.  **Given** an image of a black knight, **When** processed by the classifier, **Then** it is identified as "Black Knight" (bn).
2.  **Given** an image of an empty square with complex wood grain, **When** processed, **Then** it is identified as "Empty" (1).
3.  **Given** an image of a white pawn in partial shadow, **When** processed, **Then** it is identified as "White Pawn" (WP).

---

### User Story 2 - Robust Board Detection & Cropping (Priority: P2)

As a user, I want the board detection to correctly isolate the chessboard and crop squares with sufficient padding, so that tall pieces (like Kings and Queens) are not cut off and can be correctly recognized by the classifier.

**Why this priority**: Even a perfect classifier will fail if the input image (the cropped square) is missing the head of the piece due to tight cropping.

**Independent Test**: Can be tested by providing full board images and inspecting the 64 output cropped images to ensure pieces are centered and fully visible.

**Acceptance Scenarios**:

1.  **Given** a photo of a board taken from an angle, **When** the board is detected, **Then** the perspective transform accurately flattens the board.
2.  **Given** the flattened board image, **When** splitting into squares, **Then** the cropping region includes vertical padding to capture piece heads extending above the square boundary.

---

### Edge Cases

-   **Model Loading Failure**: What happens if the model weights file is missing or corrupt? The system should raise a clear error or fallback to a safe state (e.g., error response) rather than crashing.
-   **Extreme Angles**: If the camera angle is too low, pieces will occlude each other. The system should attempt best-effort or warn the user.
-   **Non-Standard Pieces**: If the chess set is non-standard (e.g., themed set), the model may fail. This is acceptable but should be noted as a limitation.

## Requirements

### Functional Requirements

-   **FR-001**: The system MUST utilize a Convolutional Neural Network (CNN) architecture (e.g., MobileNetV2 or ResNet18) for image classification.
-   **FR-002**: The classifier MUST support 13 distinct classes: Empty, White Pawn, White Knight, White Bishop, White Rook, White Queen, White King, Black Pawn, Black Knight, Black Bishop, Black Rook, Black Queen, Black King.
-   **FR-003**: The board detector service MUST implement a perspective transformation that corrects the board to a top-down view.
-   **FR-004**: The square extraction logic MUST allow for configurable padding/margins (especially vertical) to include parts of pieces that extend beyond the square's logical grid.
-   **FR-005**: The backend MUST include necessary dependencies (`torch`, `torchvision` or `onnxruntime`) to run inference.
-   **FR-006**: The system MUST provide a mechanism to load model weights from a file at startup.

### Key Entities

-   **ClassifierModel**: Represents the loaded neural network model used for inference.
-   **SquareImage**: A processed image patch representing a single square on the chessboard, prepared for the classifier.

## Success Criteria

### Measurable Outcomes

-   **SC-001**: Piece classification accuracy exceeds 90% on a valid validation set of standard Staunton pieces.
-   **SC-002**: The system correctly generates the FEN string for a standard "starting position" board image with 100% accuracy.
-   **SC-003**: Inference time for a full board (64 squares) takes less than 5 seconds on a standard CPU backend.
-   **SC-004**: Users report (or tests verify) that Kings and Queens are correctly identified in >85% of cases where they were previously misidentified as Pawns or Empty due to cropping.