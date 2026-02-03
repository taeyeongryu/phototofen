from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.core.config import ClassifierConfig
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Chess Puzzle Photo to FEN")

# Configure CORS
origins = [
    "http://localhost:5173",  # Vite default port
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    model_path = ClassifierConfig.MODEL_PATH
    if not os.path.exists(model_path):
        logger.warning(f"Model file not found at {model_path}. Classification service will fail until a model is placed there.")
        logger.warning("Please train a model using 'backend/scripts/train_model.py' or place a pre-trained 'model.pth' in 'backend/app/assets/'.")
    else:
        logger.info(f"Model file found at {model_path}.")

@app.get("/")
def read_root():
    return {"message": "Welcome to Photo to FEN API"}
