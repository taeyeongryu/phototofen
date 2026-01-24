# Research: Fix Conversion Workflow

**Feature**: 003-fix-conversion-workflow
**Date**: 2026-01-24

## Decisions & Rationale

### 1. Backend Readiness
**Decision**: No backend API changes required.
**Rationale**: 
- `backend/app/api/routes.py` already accepts `active_color` as a form parameter.
- `backend/app/services/fen_generator.py` correctly uses this parameter to append `w` or `b` to the FEN string.
- The existing logic `return f"{board_fen} {active_color} - - 0 1"` is sufficient.

### 2. Frontend State Management
**Decision**: Lift state to `Home.tsx` and control `ImageUpload` via keys or props.
**Rationale**:
- Currently, `ImageUpload` triggers upload immediately. This needs to be decoupled.
- `Home.tsx` will hold `selectedFile` state.
- `ImageUpload` will call `onFileSelect` but `Home` will just store it, not upload.
- A new "Convert" button in `Home` will trigger the API call using `selectedFile` and `activeColor`.

### 3. Re-upload Bug Fix
**Decision**: Reset file input value on clear.
**Rationale**:
- The bug "cannot upload same file again" is caused by the browser's file input not triggering `onChange` if the value (filename) is the same.
- Solution: When the clear button is clicked, explicitly set `fileInput.value = ''` in `ImageUpload.tsx`.
- Additionally, use a React `key` on the `ImageUpload` component in `Home.tsx` to force a complete re-mount when the user wants to "clear all", ensuring a clean state.

## Alternatives Considered

- **Using a controlled file input**: Harder to style and manage drag-and-drop. Uncontrolled with explicit reset is standard for file inputs.
- **Dynamic FEN update (Client-side)**: Initially requested, but rejected to keep logic simple and deterministic as per updated spec. FEN is only generated on "Convert".
