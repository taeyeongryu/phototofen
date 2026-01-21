# Feature Specification: Fix FEN Generation Logic

**Feature Branch**: `002-fix-fen-generation`  
**Created**: 2026-01-21  
**Status**: Draft  
**Input**: User description: "지금 001-photo-to-fen을 개발하고 있는데 phase3까지 진행했는데 fen이 제대로 나오지 않아서 디버깅 및 에러픽스를 진행하고 싶어. 체스 퍼즐을 넣어도 항상 '8/8/8/8/8/8/8/8 w - - 0 1' 이렇게 나와."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Generate Correct FEN for Chess Puzzle (Priority: P1)

As a user, I want the system to generate the correct FEN string when I upload a chess puzzle image, so that I can use the position for analysis or gameplay. Currently, it incorrectly returns an empty board FEN.

**Why this priority**: This is the core functionality of the application. If FEN generation fails, the application does not fulfill its primary purpose.

**Independent Test**: Can be tested by uploading known chess puzzle images and verifying the output FEN string against the expected FEN.

**Acceptance Scenarios**:

1. **Given** a chess puzzle image with a non-empty board configuration, **When** the image is processed by the system, **Then** the output FEN string must match the actual pieces and positions on the board (NOT "8/8/8/8/8/8/8/8 w - - 0 1").
2. **Given** the specific image that was causing the "8/8/8/8/8/8/8/8 w - - 0 1" error, **When** it is processed, **Then** the correct FEN is returned.

### Edge Cases

- What happens when the image quality is poor or the board is partially obscured?
- How does the system handle images that are not chessboards? (Ideally, it should fail gracefully, but for this fix, we focus on valid inputs returning incorrect outputs).
- What if the board is actually empty? (It should correctly return "8/8/8/8/8/8/8/8 w - - 0 1" or similar, but with appropriate active color/castling rights if applicable).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST correctly identify the presence and type of chess pieces on the board squares.
- **FR-002**: System MUST correctly translate the detected board state into a valid FEN string.
- **FR-003**: System MUST NOT default to an empty board FEN ("8/8/8/8/8/8/8/8 w - - 0 1") when pieces are detected.
- **FR-004**: The FEN generation logic MUST handle standard chess piece representations (pawn, knight, bishop, rook, queen, king) for both colors (white, black).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The specific bug returning "8/8/8/8/8/8/8/8 w - - 0 1" for populated boards is eliminated.
- **SC-002**: FEN generation is accurate for at least 3 distinct test cases of chess puzzles.