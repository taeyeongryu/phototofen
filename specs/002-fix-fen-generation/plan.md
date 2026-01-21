# Implementation Plan: Fix FEN Generation

**Branch**: `002-fix-fen-generation` | **Date**: 2026-01-21 | **Spec**: `specs/002-fix-fen-generation/spec.md`
**Input**: Feature specification from `specs/002-fix-fen-generation/spec.md`

## Summary

The current FEN generation fails for populated boards, returning an empty board FEN ("8/8/8/8/8/8/8/8...").
Logs indicate `board_detector.py` is selecting a very small noise contour (area ~1100 px) instead of the actual chessboard.
This plan focuses on making `detect_board` robust by enforcing minimum area thresholds and improving contour approximation/selection logic.

## Technical Context

**Language/Version**: Python 3.10+, TypeScript 5+, Node.js 22
**Primary Dependencies**: FastAPI, OpenCV (backend), React, Vite (frontend)
**Storage**: N/A (Stateless)
**Testing**: pytest
**Target Platform**: Web
**Project Type**: Web application
**Performance Goals**: Processing < 2s
**Constraints**: Must handle standard chess puzzle images.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Principle 1**: N/A (Fix)
- **Principle 2**: N/A
- **Principle 3**: Test-First. Will add a test case with the failing image context (or mock).

## Project Structure

### Documentation (this feature)

```text
specs/002-fix-fen-generation/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── openapi.yaml
└── tasks.md
```

### Source Code (repository root)

```text
backend/
├── app/
│   └── services/
│       ├── board_detector.py  # Primary changes here
│       └── piece_classifier.py
└── tests/
    └── test_api.py            # Add regression test
```

**Structure Decision**: Standard Backend/Frontend structure.

## Complexity Tracking

N/A