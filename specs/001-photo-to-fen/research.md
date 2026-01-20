# Research: Chess Puzzle Photo to FEN

## Technical Decisions

### Python Environment Management
- **Decision**: `venv` (Standard Library)
- **Rationale**: User explicitly requested `venv`. It is the standard, built-in way to manage environments in Python, requiring no external tools like Poetry or Pipenv for this scale.
- **Alternatives Considered**: 
    - Poetry: Good for dependency resolution but adds complexity.
    - Conda: Good for data science but heavier.
    - Pipenv: Workflow can be slower.

### Backend Framework
- **Decision**: FastAPI
- **Rationale**: High performance, easy async support (good for I/O bound image uploads), automatic OpenAPI documentation generation.
- **Alternatives Considered**: 
    - Flask: Simpler but manual async handling and doc generation.
    - Django: Too heavy for a simple stateless API.

### Image Processing
- **Decision**: OpenCV (`opencv-python`)
- **Rationale**: Industry standard for computer vision tasks like grid detection, edge detection, and perspective transformation.
- **Alternatives Considered**: 
    - PIL/Pillow: Good for basic manipulation but lacks advanced computer vision algorithms needed for board detection.
    - Scikit-image: More academic/heavy.

### Frontend Framework
- **Decision**: React + Vite + TypeScript
- **Rationale**: Modern, fast tooling (Vite), type safety (TS), and rich ecosystem (React). Matches current industry standards for web apps.

### Styling
- **Decision**: Tailwind CSS
- **Rationale**: Rapid development, consistent utility-first styling without leaving markup.

### Node.js Version
- **Decision**: Node.js 22
- **Rationale**: Explicit user request. Latest Long Term Support (LTS) version providing better performance and modern features.
- **Alternatives Considered**: 
    - Node.js 18/20: Older LTS versions, but user specifically requested 22.

## Unknowns & Clarifications

- **Chess Piece Recognition Model**: 
    - *Initial approach*: Heuristic/Color detection + Template matching or simple CNN if needed. For MVP, we might start with basic heuristics or a placeholder.
    - *Resolution*: Start with basic image processing (color/contours). If insufficient, explore `tensorflow` or `pytorch` with a pre-trained model later. For now, keep dependencies minimal.