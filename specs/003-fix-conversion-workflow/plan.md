# Implementation Plan: Fix Conversion Workflow and UI Bugs

**Branch**: `003-fix-conversion-workflow` | **Date**: 2026-01-24 | **Spec**: [specs/003-fix-conversion-workflow/spec.md](spec.md)
**Input**: Feature specification from `specs/003-fix-conversion-workflow/spec.md`

## Summary

The goal is to refactor the frontend workflow to require an explicit "Convert" action before generating the FEN, ensuring the user can select the side-to-move (White/Black) beforehand. Additionally, we will fix the image re-upload bug by properly resetting the file input state.

## Technical Context

**Language/Version**: Python 3.13+, TypeScript 5+, Node.js 22+
**Primary Dependencies**: FastAPI, OpenCV, React, Vite
**Storage**: N/A (Stateless)
**Testing**: `pytest` (Backend), Manual/Browser (Frontend)
**Target Platform**: Web (Browser + Backend API)
**Project Type**: Web application
**Performance Goals**: N/A
**Constraints**: N/A
**Scale/Scope**: Small feature fix

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Test-First**: Will ensure backend tests cover the `active_color` parameter (already likely covered, but will verify). Frontend tests are manual/UI based for this scope.
- **Simplicity**: Changes are focused on UI state management and workflow control.

## Project Structure

### Documentation (this feature)

```text
specs/003-fix-conversion-workflow/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
└── tasks.md             # Phase 2 output
```

### Source Code (repository root)

```text
backend/
├── app/
│   ├── api/
│   │   └── routes.py    # Verify active_color handling
│   └── services/
│       └── fen_generator.py # Verify active_color logic

frontend/
├── src/
│   ├── pages/
│   │   └── Home.tsx     # Main workflow logic changes
│   └── components/
│       ├── ImageUpload.tsx # Fix re-upload bug
│       └── TurnSelector.tsx # Ensure correct state lifting
```

**Structure Decision**: Standard full-stack web app structure.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | | |