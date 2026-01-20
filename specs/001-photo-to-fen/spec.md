# Feature Specification: Chess Puzzle Photo to FEN Converter

**Feature Branch**: `001-photo-to-fen`
**Created**: 2026-01-20
**Status**: Draft
**Input**: User description: "내가 만들고 싶은건 체스 퍼즐을 fen(Forsyth-Edwards Notation)으로 바꿔주는 프로그램을 만들고싶어. 이유는 책으로 체스 퍼즐을 푸는데 fen이 없어서 엔진에 퍼즐을 넣어보려면 리체스같은 온라인 체스 플랫폼에 직접 보드를 구성해야되거든. 체스퍼즐 사진을 찍어서 웹에 올리면 백/흑 차례를 물어보고 fen으로 바꾼다음 복사하기 편하게 해주는 프로그램을 만들고싶어."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Upload and Convert Puzzle (Priority: P1)

As a chess student, I want to upload a photo of a chess puzzle from a book so that I can get its FEN notation without manually setting up the board.

**Why this priority**: This is the core value proposition of the application. Without this, the problem of manual entry is not solved.

**Independent Test**: Can be tested by uploading a sample image of a chess board and verifying the output FEN matches the position.

**Acceptance Scenarios**:

1. **Given** the user is on the main page, **When** they upload an image file (JPG/PNG) of a chess puzzle, **Then** the system accepts the file and presents a preview.
2. **Given** an uploaded image, **When** the user confirms the upload, **Then** the system analyzes the image to detect pieces and their positions.

---

### User Story 2 - Specify Turn to Move (Priority: P1)

As a user, I want to specify whether it is White's or Black's turn to move, so that the generated FEN string correctly reflects the game state for analysis engines.

**Why this priority**: FEN requires the active color. Engines might give the wrong evaluation if the side to move is incorrect.

**Independent Test**: Can be tested by toggling the turn selector and observing the `w` or `b` change in the resulting FEN string.

**Acceptance Scenarios**:

1. **Given** an uploaded image, **When** the system asks for the side to move, **Then** the user can select "White" or "Black".
2. **Given** a selected side (e.g., Black), **When** the conversion completes, **Then** the FEN string includes the correct active color indicator (e.g., `... b ...`).

---

### User Story 3 - Copy FEN to Clipboard (Priority: P2)

As a user, I want to easily copy the generated FEN string, so that I can quickly paste it into Lichess or another chess engine.

**Why this priority**: Improves usability and speed, directly addressing the "convenience" part of the user request.

**Independent Test**: Can be tested by clicking the copy button and pasting into a text editor to verify the content.

**Acceptance Scenarios**:

1. **Given** a generated FEN string, **When** the user clicks the "Copy" button, **Then** the FEN string is copied to the system clipboard and a confirmation message (e.g., "Copied!") is shown.

### Edge Cases

- What happens when the uploaded image is not a chess board?
  - System should display an error message indicating no board was detected.
- What happens if the image is blurry or the lighting is poor?
  - System should attempt best-effort recognition and warn the user if confidence is low, or allow manual correction (out of scope for MVP, so maybe just an error/retry prompt).
- What happens if the board is partially occluded?
  - System should report an error.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a web interface for users to upload image files (supported formats: JPEG, PNG).
- **FR-002**: System MUST allow users to select the active turn (White or Black) before or during the conversion process.
- **FR-003**: System MUST analyze the uploaded image to identify the 8x8 grid and the chess pieces within it.
- **FR-004**: System MUST generate a valid Forsyth-Edwards Notation (FEN) string representing the detected board state and selected turn.
  - *Assumption*: Castling rights and en passant targets will default to "-" (none) as they cannot be determined solely from a static image of a puzzle.
  - *Assumption*: Halfmove clock and fullmove number will default to "0 1" or similar standard start values.
- **FR-005**: System MUST display the generated FEN string to the user.
- **FR-006**: System MUST provide a "Copy to Clipboard" functionality for the generated FEN.
- **FR-007**: System MUST be accessible via standard mobile and desktop web browsers.

### Key Entities

- **PuzzleImage**: The raw image file uploaded by the user.
- **BoardState**: Internal representation of the 8x8 grid and piece locations.
- **FEN**: The final string output (e.g., `rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1`).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can obtain a FEN string from a clear photo in under 10 seconds.
- **SC-002**: 90% of clear, well-lit book puzzle photos are correctly converted to FEN without error.
- **SC-003**: Users successfully copy the FEN to clipboard in 100% of successful conversions (measured by interaction with the copy button).