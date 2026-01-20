# Data Model

## Entities

### AnalysisRequest
*Represents the user's input for processing.*
- **image**: `file` (Required) - The image file (JPG/PNG).
- **active_color**: `string` (Required) - 'w' for White to move, 'b' for Black to move.

### AnalysisResponse
*Represents the result of the conversion.*
- **fen**: `string` (Required) - The generated Forsyth-Edwards Notation string.
- **confidence**: `float` (Optional) - A 0-1 score indicating the model's certainty.
- **detected_board_image**: `string` (Optional) - Base64 encoded image of the detected board (for debug/verification).

## Value Objects

### FEN
- Format: `[piece_placement] [active_color] [castling] [en_passant] [halfmove] [fullmove]`
- Example: `rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1`
