# Quickstart: Chess Puzzle Photo to FEN

## Prerequisites

- **Python**: 3.13+
- **Node.js**: 22
- **Git**

## Setup

### Backend (Python + venv)

1. Navigate to backend:
   ```bash
   cd backend
   ```

2. **Create and Activate venv**:
   *Windows (PowerShell)*:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
   *Linux/macOS*:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```
   Server will be at `http://localhost:8000`.

### Frontend (React + Vite)

1. Navigate to frontend:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the dev server:
   ```bash
   npm run dev
   ```
   Frontend will be at `http://localhost:5173`.

## Verification

1. Ensure Backend is running. Open `http://localhost:8000/docs`.
2. Ensure Frontend is running. Open `http://localhost:5173`.