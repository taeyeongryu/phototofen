# Tasks: Fix FEN Generation Logic

**Feature Branch**: `002-fix-fen-generation`
**Feature Status**: Completed

## Phase 1: Setup
*Goal: Prepare the environment for development and testing.*

- [x] T001 Copy failing image to `backend/tests/data/failing_board.jpg`
- [x] T002 Create regression test `backend/tests/test_fen_generation_fix.py` that loads `failing_board.jpg` and asserts correct FEN (not "8/8/8...").

## Phase 2: Foundational
*Goal: Implement robust board detection core logic (Blocking P1).*

- [x] T003 Implement `BoardDetectionError` in `backend/app/core/exceptions.py`.
- [x] T004 Modify `detect_board` in `backend/app/services/board_detector.py` to filter contours by `MIN_BOARD_AREA` (e.g., > 20,000 px).
- [x] T005 [P] Add flexible shape approximation (iterative epsilon or convex hull fallback) in `backend/app/services/board_detector.py`.
- [x] T006 [P] Add debug image saving logic (edges, contours, candidate) to `board_detector.py` when `DEBUG` mode is enabled.

## Phase 3: User Story 1 - Correct FEN for Chess Puzzle
*Goal: Ensure populated boards generate correct FEN strings (P1).*

- [x] T007 [US1] Update `backend/app/services/piece_classifier.py` if necessary to handle slightly different warped board sizes/perspectives. (No change needed for this fix)
- [x] T008 [US1] Run regression test `backend/tests/test_fen_generation_fix.py` and verify it passes.
- [x] T009 [US1] Verify API endpoint `/api/analyze` returns correct FEN for the failing image via `curl` or Postman. (Verified via TestClient)

## Final Phase: Polish
*Goal: Cleanup and code quality.*

- [x] T010 Remove temporary debug image saving or ensure it's flag-controlled.
- [x] T011 Run `ruff check .` and fix any linting errors.
- [x] T012 Run full test suite `pytest` to ensure no regressions.

## Dependencies

- Phase 2 (Board Detection) -> Phase 3 (US1 Verification)

## Implementation Strategy
1. **Reproduce**: Add the failing test case (Phase 1).
2. **Fix Core**: Update `board_detector.py` to ignore noise and find the real board (Phase 2).
3. **Verify**: Run the test to confirm the fix (Phase 3).
