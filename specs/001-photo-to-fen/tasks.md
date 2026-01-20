# Tasks: Chess Puzzle Photo to FEN

**Spec**: `specs/001-photo-to-fen/spec.md`
**Status**: Pending

## Phase 1: Setup
*Goal: Initialize project structure and dependencies.*

- [x] T001 Create backend project structure and `backend/requirements.txt` with FastAPI, OpenCV, Uvicorn in `backend/`
- [x] T002 Initialize frontend with Vite (React + TS) in `frontend/`
- [x] T003 Configure Tailwind CSS in `frontend/`
- [x] T004 [P] Setup basic FastAPI app in `backend/app/main.py` with CORS middleware
- [x] T005 [P] Setup basic Frontend App structure in `frontend/src/App.tsx`

## Phase 2: Foundational
*Goal: Establish shared data models and API client.*

- [ ] T006 Create Pydantic models for `AnalysisRequest` and `AnalysisResponse` in `backend/app/models/api_models.py`
- [ ] T007 Create API client wrapper in `frontend/src/api/client.ts`
- [ ] T008 Create basic UI Layout component in `frontend/src/components/Layout.tsx`

## Phase 3: User Story 1 - Upload and Convert Puzzle (P1)
*Goal: Users can upload an image and get a FEN string (basic detection).*
*Independent Test: Upload an image and verify a FEN string is returned and displayed.*

- [ ] T009 [US1] Create `ImageUpload` component in `frontend/src/components/ImageUpload.tsx`
- [ ] T010 [US1] Implement `POST /api/analyze` stub in `backend/app/api/routes.py`
- [ ] T011 [US1] Implement image loading and grayscale conversion service in `backend/app/services/image_processing.py`
- [ ] T012 [US1] Implement board detection logic (OpenCV) in `backend/app/services/board_detector.py`
- [ ] T013 [US1] Implement square extraction logic in `backend/app/services/board_detector.py`
- [ ] T014 [US1] Implement basic heuristic/mock piece classifier in `backend/app/services/piece_classifier.py`
- [ ] T015 [US1] Implement FEN string construction logic in `backend/app/services/fen_generator.py`
- [ ] T016 [US1] Integrate services into `POST /api/analyze` endpoint in `backend/app/api/routes.py`
- [ ] T017 [US1] Connect Frontend Upload component to API and display result in `frontend/src/pages/Home.tsx`

## Phase 4: User Story 2 - Specify Turn to Move (P1)
*Goal: Allow user to select White or Black to move.*
*Independent Test: Toggle turn selector and verify 'w' or 'b' in FEN output.*

- [ ] T018 [US2] Create `TurnSelector` component in `frontend/src/components/TurnSelector.tsx`
- [ ] T019 [US2] Update `AnalysisRequest` model in `backend/app/models/api_models.py` to include `active_color`
- [ ] T020 [US2] Update `fen_generator.py` to use provided `active_color` in `backend/app/services/fen_generator.py`
- [ ] T021 [US2] Integrate `TurnSelector` into `Home.tsx` and API call in `frontend/src/pages/Home.tsx`

## Phase 5: User Story 3 - Copy FEN to Clipboard (P2)
*Goal: Easy copy functionality for the result.*
*Independent Test: Click copy button and verify clipboard content.*

- [ ] T022 [US3] Create `FenDisplay` component with Copy button in `frontend/src/components/FenDisplay.tsx`
- [ ] T023 [US3] Implement clipboard copy logic in `frontend/src/components/FenDisplay.tsx`
- [ ] T024 [US3] Replace raw FEN display in `Home.tsx` with `FenDisplay` component in `frontend/src/pages/Home.tsx`

## Phase 6: Polish & Cross-Cutting
*Goal: Error handling, UI refinements, and final cleanup.*

- [ ] T025 Add loading spinner state to `Home.tsx` and `ImageUpload.tsx`
- [ ] T026 Implement error handling for failed uploads/conversions in `frontend/src/pages/Home.tsx`
- [ ] T027 Add error response handling in `backend/app/api/routes.py` (e.g. no board found)
- [ ] T028 Review and cleanup code (remove debug prints, format files)

## Dependencies

- **US1** requires Phase 1 & 2.
- **US2** extends US1 (can be built after T016).
- **US3** depends on US1 (needs FEN result to copy).

## Implementation Strategy

1. **MVP (US1)**: Focus on getting the pipeline working (Upload -> Backend -> Mock/Heuristic FEN -> Response).
2. **Refinement (US2)**: Add the turn logic.
3. **UX (US3)**: Add the copy button.
4. **Polish**: Handle edge cases like "no board found".