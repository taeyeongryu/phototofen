# Feature Specification: Fix Conversion Workflow and UI Bugs

**Feature Branch**: `003-fix-conversion-workflow`
**Created**: 2026-01-24
**Status**: Draft
**Input**: User description: "일단 1차 개발이 완료됐는데 몇가지 수정을 해야될거같아. 1. 흑, 백 선택하는 버튼이 있는데 사진이 올라간 후, fen이 출력이 된 후에는 적용이 안되는문제 2. 사진을 한번 올리고 지운다음 사진을 다시 올리면 사진이 올라가지 않는 문제 3. 그리고 변환이라는 버튼을 클릭해서 그 때 변환이 되도록 로직 수정했으면 좋겠어."

## User Scenarios & Testing

### User Story 1 - Manual Conversion Workflow (Priority: P1)

Users should be able to upload a photo and strictly control when the FEN generation happens, preventing unnecessary processing or premature results.

**Why this priority**: Core workflow change requested by the user to improve control.

**Independent Test**: Can be tested by uploading a photo and verifying that no FEN is generated until the "Convert" button is clicked.

**Acceptance Scenarios**:

1. **Given** a user is on the main page, **When** they upload a chessboard image, **Then** the image is displayed but NO FEN is generated/displayed.
2. **Given** an image is uploaded, **When** the user clicks the "Convert" button, **Then** the system processes the image and displays the resulting FEN.

---

### User Story 2 - Explicit Side Selection (Priority: P1)

Users can select the "side to move" (White/Black) before converting, and this selection is applied ONLY when the conversion is triggered.

**Why this priority**: Ensures deterministic behavior where the user explicitly controls the output parameters.

**Independent Test**:
1. Select "Black" -> Click "Convert" -> Verify FEN ends with `b`.
2. Select "White" -> Click "Convert" -> Verify FEN ends with `w`.
3. (With FEN displayed) Toggle side -> Verify FEN does NOT change until "Convert" is clicked again.

**Acceptance Scenarios**:

1. **Given** an image is uploaded, **When** the user selects "Black" and clicks "Convert", **Then** the generated FEN MUST indicate black to move (`b`).
2. **Given** a FEN has already been generated, **When** the user changes the side selection, **Then** the displayed FEN remains unchanged until the "Convert" button is clicked again.

---

### User Story 3 - Reliable Photo Re-upload (Priority: P2)

Users should be able to remove an uploaded photo and upload a new one (or the same one) without refreshing the page.

**Why this priority**: Fixes a reported bug that prevents standard usage flow.

**Independent Test**: Can be tested by uploading, deleting, and re-uploading an image in the same session.

**Acceptance Scenarios**:

1. **Given** a user has uploaded an image, **When** they delete/clear the image, **Then** the image preview and previous FEN results are cleared.
2. **Given** a user has cleared a previous image, **When** they attempt to upload an image again, **Then** the upload succeeds and the new image is displayed.

### Edge Cases

- **No Image Selected**: The "Convert" button should be disabled or show a clear error if clicked without an image.
- **Conversion Failure**: If the backend fails to process the image, a user-friendly error message must be displayed, and the system should remain in a state allowing retry or new upload.
- **Rapid Toggling**: Rapidly switching the side selector should not cause race conditions; the final state must match the user's last selection.

## Requirements

### Functional Requirements

- **FR-001**: The system MUST allow users to upload an image file.
- **FR-002**: The system MUST NOT automatically trigger FEN generation immediately upon file selection/upload.
- **FR-003**: The system MUST provide a prominent "Convert" button that is enabled only when an image is selected.
- **FR-004**: Clicking the "Convert" button MUST trigger the FEN generation process.
- **FR-005**: The system MUST allow the user to select the active color (White or Black) as a parameter for the conversion.
- **FR-006**: Changing the active color selection MUST NOT update the displayed FEN string automatically.
- **FR-007**: The generated FEN MUST strictly reflect the active color that was selected at the moment the "Convert" button was clicked.
- **FR-008**: The system MUST provide a way to clear or remove the currently uploaded image.
- **FR-009**: After clearing an image, the system MUST allow a subsequent upload action to function correctly without requiring a page reload.
- **FR-010**: Clearing an image MUST also clear any displayed FEN result from the previous conversion.

### Key Entities

- **Chessboard Image**: The raw image file provided by the user.
- **FEN String**: The text representation of the board state (Forsyth–Edwards Notation).
- **Active Color**: The state indicating which player's turn it is (White/Black).

## Success Criteria

### Measurable Outcomes

- **SC-001**: FEN generation occurs 0% of the time before the "Convert" button is clicked.
- **SC-002**: Users can successfully complete a cycle of Upload -> Delete -> Re-upload 100% of the time without errors.