# Quickstart: Fix Conversion Workflow

## Prerequisites
- Node.js 22+
- Python 3.13+

## Running Locally

1. **Start Backend**:
   ```bash
   cd backend
   source venv/bin/activate  # or created venv
   uvicorn app.main:app --reload
   ```

2. **Start Frontend**:
   ```bash
   cd frontend
   npm run dev
   ```

3. **Verify Feature**:
   - Open http://localhost:5173
   - Select "Black" side.
   - Upload an image.
   - Verify NO FEN is generated immediately.
   - Click "Convert".
   - Verify generated FEN ends with `b`.
   - Click "Clear" (or remove image).
   - Upload the SAME image again. Verify it works.
