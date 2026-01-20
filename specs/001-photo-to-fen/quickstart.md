# Quickstart: Photo to FEN

## Prerequisites
- Node.js 18+
- Python 3.10+
- `pip` and `npm`

## Setup

### Backend (Python)
1. Navigate to `backend/`.
2. Create venv: `python -m venv venv`
3. Activate: `.\venv\Scripts\Activate` (Windows)
4. Install: `pip install -r requirements.txt`
5. Run: `uvicorn main:app --reload`

### Frontend (React)
1. Navigate to `frontend/`.
2. Install: `npm install`
3. Run: `npm run dev`

## Development Flow
1. Start Backend (Port 8000).
2. Start Frontend (Port 5173).
3. Open `http://localhost:5173`.
4. Upload an image to test.
