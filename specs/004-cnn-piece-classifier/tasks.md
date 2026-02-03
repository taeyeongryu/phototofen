# Tasks: CNN Piece Classifier & Improved Board Detection

**Feature**: `004-cnn-piece-classifier`
**Status**: Completed
**Generated**: 2026-02-03

## Dependencies
- Phase 1 (Setup) -> Phase 2 (Foundation)
- Phase 2 -> Phase 3 (US1: Classifier)
- Phase 2 -> Phase 4 (US2: Board Detection)
- Phase 3 & 4 -> Phase 5 (Polish)

## Phase 1: Setup (Project Initialization)
**Goal**: Prepare the environment and install necessary libraries.

- [x] T001 Install PyTorch and torchvision dependencies in `backend/requirements.txt`
- [x] T002 [P] Create `backend/scripts` directory for training scripts
- [x] T003 [P] Create `backend/app/assets` directory for model storage
- [x] T004 [P] Download/Place dummy or pre-trained model weights in `backend/app/assets/model.pth` (placeholder for dev)

## Phase 2: Foundational (Blocking Prerequisites)
**Goal**: Establish the model training and loading infrastructure.

- [x] T005 Create `PieceClass` enum in `backend/app/models/api_models.py` matching the 13 classes
- [x] T006 Implement `ClassifierConfig` class in `backend/app/core/config.py` to manage model paths and device settings
- [x] T007 Implement `train_model.py` in `backend/scripts/` to allow users to train MobileNetV2 on custom data
- [x] T008 [P] Add unit test for model loading failure handling in `backend/tests/test_classifier_loading.py`

## Phase 3: User Story 1 - Accurate Piece Classification (Priority: P1)
**Goal**: Implement the CNN-based classifier service.
**Independent Test**: `backend/tests/test_classifier_inference.py` passes with dummy images.

- [x] T009 [US1] Implement `load_model` function in `backend/app/services/classifier.py` using `torchvision.models.mobilenet_v2`
- [x] T010 [US1] Implement `preprocess_square` function in `backend/app/services/classifier.py` (Resize, ToTensor, Normalize)
- [x] T011 [US1] Implement `classify_square` function in `backend/app/services/classifier.py` to run inference
- [x] T012 [US1] [P] Create integration test `backend/tests/test_classifier_inference.py` to verify end-to-end classification flow
- [x] T013 [US1] Update `backend/app/api/routes.py` to use `classifier.classify_square` instead of the old heuristic
- [x] T014 [US1] Update `backend/app/services/fen_generator.py` to handle the new `PieceClass` enum input

## Phase 4: User Story 2 - Robust Board Detection & Cropping (Priority: P2)
**Goal**: Improve square extraction to include vertical padding.
**Independent Test**: `backend/tests/test_board_extraction.py` verifies output image dimensions.

- [x] T015 [US2] Modify `extract_squares` in `backend/app/services/board_detector.py` to accept `padding_top` parameter
- [x] T016 [US2] Implement logic in `extract_squares` to extend the crop region upwards by `padding_top` pixels (handling boundary checks)
- [x] T017 [US2] [P] Create unit test `backend/tests/test_board_extraction.py` to verify padded crop dimensions
- [x] T018 [US2] Update `backend/app/api/routes.py` to pass appropriate padding configuration (e.g., 20% of square height)

## Phase 5: Polish & Cross-Cutting Concerns
**Goal**: Final cleanup and error handling.

- [x] T019 Ensure `openapi.yaml` in `specs/004-cnn-piece-classifier/contracts/` matches the final implementation
- [x] T020 Add error handling for "Model Not Found" in `backend/app/main.py` startup event (optional) or lazy loading
- [x] T021 Run `ruff check .` and fix any linting errors in new files
- [x] T022 Verify all tests pass with `pytest`

## Implementation Strategy
- **MVP**: Complete Phase 1, 2, and 3. This gives a working CNN classifier.
- **Incremental**: Phase 4 can be shipped separately if needed, but is highly recommended to improve real-world accuracy.