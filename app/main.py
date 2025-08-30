from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.v1 import qr
from app.core.config import logger  # optional if you want to use your logger

# Lifespan context manager to replace deprecated @app.on_event
# these are new way to write FastAPI 
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup")
    yield
    logger.info("Application shutdown")

app = FastAPI(
    title="QR Generator from URL",
    version="1.0.0",
    description="Generate QR codes from URLs (v1 - no DB)",
    lifespan=lifespan
)

# Include routers
app.include_router(qr.router, prefix="/api/v1/qr", tags=["QR"])

# Serve frontend
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.get("/")
def read_index():
    return FileResponse("frontend/index.html")
