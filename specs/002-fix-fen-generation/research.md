# Research: Fix FEN Generation Logic

## Problem Analysis

**Symptom**:
The FEN generator returns "8/8/8/8/8/8/8/8 w - - 0 1" (empty board) for populated chess puzzles.

**Evidence (Debug Logs)**:
```text
[DEBUG] Board contour found. Area: 1097.5
[DEBUG] Square Mean=56.67, StdDev=3.52 -> Result='1'
... (all squares low deviation, result '1')
```

**Root Cause**:
The `board_detector.py` is selecting a tiny contour (Area ~1097 pixels) instead of the actual chessboard. 
- For a typical 400x400 image (160k pixels), 1100 pixels is < 0.7% of the image.
- Because the "board" is just a tiny patch of noise/background, splitting it into 64 squares results in homogenous 4x4 pixel blocks.
- These blocks have low standard deviation in pixel intensity, so `piece_classifier.py` classifies them as empty ('1').

**Why is the large board missed?**
The code sorts contours by area (`reverse=True`). If it skipped the large board and picked the tiny one, it means the large board's contour **did not satisfy the `len(approx) == 4` condition**.
- Chessboards in photos often have slight perspective distortion or noise that makes `approxPolyDP` return 5, 6, or more vertices, causing the strict "== 4" check to fail.

## Proposed Solution

### 1. Robust Board Detection
- **Minimum Area Threshold**: Ignore any contour smaller than `MIN_BOARD_AREA` (e.g., 20,000 pixels or 5% of image area).
- **Flexible Shape Approximation**:
  - If strict `approxPolyDP` fails, try iterating with different epsilon values.
  - Alternatively, find the **largest convex hull** that has an aspect ratio close to 1:1 (square).

### 2. Enhanced Debugging
- **Visual Debugging**: Save intermediate images to disk (in a debug folder) to allow visual inspection:
  - `debug_01_edges.jpg`: Canny edge output.
  - `debug_02_contours.jpg`: All detected contours drawn.
  - `debug_03_board_candidate.jpg`: The selected contour.
  - `debug_04_warped.jpg`: The final warped board.

### 3. Verification Strategy
- **Unit Test**: Create a test case with the problematic image (mocked or actual file).
- **Assert**: Ensure detected board area > `MIN_AREA`.

## Decision
- **Approach**: Modify `detect_board` in `board_detector.py`.
- **Logic**:
    1. Filter contours by `area > MIN_AREA`.
    2. Sort by area descending.
    3. Loop through candidates:
        a. Apply `approxPolyDP`.
        b. If `len == 4` and `is_convex`, accept.
        c. (Fallback) If no 4-vertex polygon found, try finding the largest square-ish convex hull.
    4. If no candidate found, raise clearer `BoardDetectionError`.
