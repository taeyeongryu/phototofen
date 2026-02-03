# Implementation Plan: CNN Piece Classifier & Improved Board Detection

**Branch**: `004-cnn-piece-classifier` | **Date**: 2026-02-03 | **Spec**: specs/004-cnn-piece-classifier/spec.md
**Input**: Feature specification from `/specs/004-cnn-piece-classifier/spec.md`

## Summary

Replace the current heuristic piece classifier with a CNN-based model (MobileNetV2) to achieve >90% accuracy. Improve board detection by adding configurable padding to square extraction to prevent cutting off piece heads.

## Technical Context

**Language/Version**: Python 3.10+
**Primary Dependencies**: FastAPI, OpenCV, PyTorch, torchvision
**Storage**: N/A (Stateless)
**Testing**: pytest
**Target Platform**: Local execution (Windows/Linux)
**Project Type**: Web Application
**Performance Goals**: < 5s for full board inference
**Constraints**: CPU inference support required
**Scale/Scope**: ~500 LOC change

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Test-First**: Mandatory.
- **Libraries**: Logic must be in `services/`, not directly in `api/`.

## Project Structure

### Documentation (this feature)

```text
specs/004-cnn-piece-classifier/
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
│   ├── services/
│   │   ├── classifier.py      # New service wrapping the model
│   │   ├── board_detector.py  # Updated with padding logic
│   │   └── ...
│   └── assets/
│       └── model.pth          # Model weights (ignored by git usually)
└── scripts/
    └── train_model.py         # Training script
```

**Structure Decision**: Standard FastAPI service pattern.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | | |