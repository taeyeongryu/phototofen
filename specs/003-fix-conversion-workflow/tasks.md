# Tasks: Fix Conversion Workflow and UI Bugs

**Input**: Design documents from `/specs/003-fix-conversion-workflow/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

## Phase 1: Foundational (Blocking Prerequisites)

**Purpose**: Verify backend readiness and setup basic frontend structure.

- [ ] T001 [P] Verify backend `active_color` handling in `backend/app/api/routes.py` and `backend/app/services/fen_generator.py`
- [ ] T002 Add a unit test in `backend/tests/test_api.py` to ensure `active_color` correctly affects the FEN output.
- [ ] T003 [P] Update `frontend/src/api/client.ts` if necessary to ensure `analyzeImage` correctly passes `active_color` as a form field.

---

## Phase 2: User Story 3 - Reliable Photo Re-upload (Priority: P2)

**Goal**: Fix the bug where the same photo cannot be uploaded twice.

**Independent Test**: Upload an image, remove it, and upload the same image again.

- [ ] T004 [P] Modify `frontend/src/components/ImageUpload.tsx` to clear the `input.value` when an image is removed.
- [ ] T005 [P] Add a `key` prop to `ImageUpload` in `frontend/src/pages/Home.tsx` based on a "reset" state or timestamp to force re-mount if needed.

---

## Phase 3: User Story 1 - Manual Conversion Workflow (Priority: P1) 🎯 MVP

**Goal**: decouple image upload from FEN generation.

**Independent Test**: Upload an image and verify no API call is made until "Convert" is clicked.

- [ ] T006 Lift `selectedFile` state from `ImageUpload.tsx` to `frontend/src/pages/Home.tsx`.
- [ ] T007 Modify `ImageUpload.tsx` to only handle file selection and preview, calling `onFileSelect` without triggering upload logic.
- [ ] T008 Add "Convert" button to `frontend/src/pages/Home.tsx`, enabled only when `selectedFile` is present.
- [ ] T009 Implement `handleConvert` in `frontend/src/pages/Home.tsx` to call the API with the stored `selectedFile`.

---

## Phase 4: User Story 2 - Explicit Side Selection (Priority: P1)

**Goal**: Ensure side selection is respected during conversion but doesn't trigger it.

**Independent Test**: Select "Black", then "Convert", and verify FEN ends with `b`. Change side and verify FEN does NOT change until "Convert" is clicked again.

- [ ] T010 Update `TurnSelector.tsx` usage in `Home.tsx` to ensure it only updates the `activeColor` state.
- [ ] T011 Ensure `handleConvert` uses the current `activeColor` state from `Home.tsx` when making the API call.
- [ ] T012 Verify that toggling `activeColor` after a result is shown does not automatically re-trigger or update the result.

---

## Phase 5: Polish & Verification

**Purpose**: Final cleanup and verification against success criteria.

- [ ] T013 [P] Remove any unused state or props from `ImageUpload.tsx` and `TurnSelector.tsx`.
- [ ] T014 [P] Ensure error handling in `Home.tsx` correctly clears the loading state and displays user-friendly messages.
- [ ] T015 Run validation of `quickstart.md` steps.

---

## Dependencies & Execution Order

1. **Phase 1 (Foundational)**: Must be done first to ensure the backend is solid.
2. **Phase 2 (US3)**: Can be done independently or in parallel with US1.
3. **Phase 3 & 4 (US1 & US2)**: Closely related, should be implemented together in `Home.tsx`.
4. **Phase 5 (Polish)**: Final step.
