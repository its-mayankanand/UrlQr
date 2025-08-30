"""
main.py

This is the entry point of the FastAPI application.
It sets up:
- Application metadata (title, version, description)
- Lifespan event handling (startup/shutdown logging)
- API routers for QR code generation
- Static frontend serving
- Root endpoint (serves index.html from frontend)
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.v1 import qr
from app.core.config import logger  # optional if you want to use your logger


# Lifespan context manager for FastAPI
# Replaces deprecated @app.on_event("startup") / @app.on_event("shutdown")
# This ensures startup and shutdown tasks are logged properly
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup")   # Log when app starts
    yield                                # Control passes to the app while running
    logger.info("Application shutdown")  # Log when app shuts down


# Create FastAPI application instance with metadata
app = FastAPI(
    title="QR Generator from URL",             # Project title
    version="1.0.0",                           # Version info
    description="Generate QR codes from URLs (v1 - no DB)",  # Short description
    lifespan=lifespan                          # Use custom lifespan handler
)


# Register router for QR code generation APIs (all endpoints under /api/v1/qr)
app.include_router(qr.router, prefix="/api/v1/qr", tags=["QR"])


# Mount static frontend files (React/Vue/HTML assets etc.) under /frontend
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


# Default root endpoint -> serves index.html of frontend
@app.get("/")
def read_index():
    return FileResponse("frontend/index.html")
