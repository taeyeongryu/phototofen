# Data Model: Fix Conversion Workflow

**Feature**: 003-fix-conversion-workflow

## Entities

### Analysis Request (Multipart/Form-Data)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `file` | Binary (Image) | Yes | The chessboard image to analyze. |
| `active_color` | String | Yes | 'w' for White, 'b' for Black. Defaults to 'w'. |

### Analysis Response (JSON)

| Field | Type | Description |
|-------|------|-------------|
| `fen` | String | The generated Forsyth–Edwards Notation string. |
| `confidence` | Float | Confidence score of the detection (0.0 - 1.0). |

## State Transitions (Frontend)

1. **Idle**: No file selected. "Convert" disabled.
2. **File Selected**: Image preview shown. "Convert" enabled. `activeColor` can be toggled.
3. **Processing**: "Convert" disabled. Loading spinner shown.
4. **Result**: FEN displayed below image. User can clear to return to Idle.
