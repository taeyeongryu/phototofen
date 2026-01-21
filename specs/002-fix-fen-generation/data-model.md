# Data Model: Chess Puzzle Photo to FEN (Fix)

## Entities

### AnalysisRequest
*Represents the user's request to analyze an image.*

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `file` | File (Binary) | Yes | The uploaded image file (JPG/PNG). |
| `active_color` | String | Yes | 'w' (White) or 'b' (Black). Default 'w' if not specified. |

### AnalysisResponse
*The result of the analysis.*

| Field | Type | Description |
|-------|------|-------------|
| `fen` | String | The detected FEN string (e.g., `rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1`). |
| `confidence` | Float | (Optional) Confidence score of the detection (0.0 - 1.0). |
| `detected_board` | String (Base64/URL) | (Optional) Debug image showing the detected board/grid for verification. |

### BoardState (Internal)
*Internal representation during processing.*

| Field | Type | Description |
|-------|------|-------------|
| `squares` | List[List[Piece]] | 8x8 grid of Piece objects. |
| `active_color` | Enum | WHITE, BLACK. |

### Piece (Internal)
*Represents a piece on a square.*

| Field | Type | Description |
|-------|------|-------------|
| `type` | Enum | PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING, NONE. |
| `color` | Enum | WHITE, BLACK, NONE. |
