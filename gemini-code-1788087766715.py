from fastapi import FastAPI
from app.core.logging import setup_logging
from app.api.v1.endpoints.health import router as health_router

setup_logging()

app = FastAPI(title="KOBİ ERP API", version="1.0.0")

app.include_router(health_router, prefix="/api/v1")