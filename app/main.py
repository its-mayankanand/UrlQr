from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.v1 import qr

app = FastAPI(
    title="QR Generator from URL",
    version="1.0.0",
    description="Generate QR codes from URLs (v1 - no DB)"
)

# Include routers
app.include_router(qr.router, prefix="/api/v1/qr", tags=["QR"])

# Serve frontend
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.get("/")
def read_index():
    return FileResponse("frontend/index.html")


