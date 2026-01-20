# Research & Technical Decisions

## Technology Stack

### Frontend
- **Framework**: React (via Vite)
  - **Rationale**: Fast development, excellent TypeScript support, lightweight.
- **Language**: TypeScript
  - **Rationale**: Type safety for FEN strings and API responses.
- **Styling**: Tailwind CSS
  - **Rationale**: Rapid UI development, responsive out of the box.
- **State Management**: React Context / Hooks
  - **Rationale**: Simple application state (upload -> select -> result), no need for Redux.

### Backend
- **Framework**: FastAPI
  - **Rationale**: High performance, native async support (good for I/O bound ML tasks), automatic OpenAPI docs.
- **Language**: Python 3.10+
  - **Rationale**: Ecosystem dominance in AI/ML (OpenCV, PyTorch/TensorFlow).

### Core Engine (Image to FEN)
- **Board Detection**: OpenCV (`opencv-python-headless`)
  - **Approach**: Canny edge detection + Hough Line Transform or `findChessboardCorners` to locate the grid.
- **Piece Classification**: PyTorch (`torch`, `torchvision`)
  - **Rationale**: Lightweight inference, easy to load pre-trained models.
  - **Implementation Strategy**:
    1. **Pre-processing**: Crop image to board, slice into 64 squares.
    2. **Inference**: Pass each square through a CNN classifier (e.g., a simple ResNet or custom CNN).
    3. **Note**: Since we cannot train a model in this session, the implementation will provide the **inference pipeline** and a script/instruction to download or train a basic model. *For the prototype, we will include a mock/heuristic mode or a simple template matcher if weights are unavailable.*

## Unknowns Resolution

### [NEEDS CLARIFICATION: Optimal Tool for Recognition]
- **Decision**: Custom Pipeline (OpenCV + CNN).
- **Why**: "All-in-one" libraries are often outdated (Python 2.7 era) or unmaintained. Building a modular pipeline allows swapping the classifier (e.g., from template matching to YOLOv8) without rewriting the app.
- **Alternative**: `tensorflow-chessbot` (TensorFlow 1.x, hard to run). `python-chess` (only handles logic, not vision).

### [NEEDS CLARIFICATION: Board Orientation]
- **Decision**: User input required (as per spec "specify turn").
- **Assumption**: We will assume the board is oriented from the perspective of the player whose turn it is, OR we will default to "White at bottom" and provide a "Flip Board" button in the UI if the FEN is upside down. *Refinement*: The Spec mentions asking for "Turn", but strictly speaking, "Turn" (White to move) is different from "Orientation" (White at bottom).
- **Refined Requirement**: We will assume standard diagram orientation (White at bottom) for the image processing. If the user implies "Black's perspective", the FEN logic might need to rotate the board. For MVP, we stick to "White at bottom" assumption for visual processing.

## Architecture

- **Client**: Uploads Image -> Checks Preview -> Selects Turn -> POST /analyze -> Displays FEN.
- **Server**:
  - `POST /api/analyze`: Accepts `file` and `turn`.
  - `ImageProcessor`: Decodes image -> Finds Board -> Extracts 64 Squares.
  - `FenGenerator`: Classifies squares -> Constructs FEN -> Appends active color.
