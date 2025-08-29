import logging
from fastapi import APIRouter
from app.schemas.qr_schema import QRRequest, QRResponse
from app.services.qr_service import generate_qr_base64

# Configure logger for this module
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/", response_model=QRResponse)
async def create_qr(request: QRRequest):
    logger.info(f"Received QR generation request for URL: {request.url}")
    try:
        qr_code_b64 = generate_qr_base64(str(request.url))
        logger.info("QR code generated successfully.")
        return QRResponse(url=str(request.url), qr_code_base64=qr_code_b64)
    except Exception as e:
        logger.error(
            f"Error generating QR code for URL {request.url}: {e}", exc_info=True
        )
        raise
