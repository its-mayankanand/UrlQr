from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.v1 import qr
from app.core.config import logger  # use the central logger

app = FastAPI(
    title="QR Generator from URL",
    version="1.0.0",
    description="Generate QR codes from URLs (v1 - no DB)",
)

# Include routers
app.include_router(qr.router, prefix="/api/v1/qr", tags=["QR"])

# Serve frontend
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


@app.get("/")
def read_index():
    logger.info("Serving frontend index.html")
    return FileResponse("frontend/index.html")


# Log app startup and shutdown events
@app.on_event("startup")
async def startup_event():
    logger.info("FastAPI application has started successfully.")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("FastAPI application is shutting down.")
