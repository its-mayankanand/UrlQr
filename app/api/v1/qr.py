"""
qr.py

This module defines the QR code API endpoints (v1).
It provides:
- A POST endpoint to generate QR codes from given URLs.
- Logging for request handling, success, and error cases.
"""

import logging
from fastapi import APIRouter
from app.schemas.qr_schema import QRRequest, QRResponse
from app.services.qr_service import generate_qr_base64

# Configure logger for this module
logger = logging.getLogger(__name__)

# Create router instance for QR API endpoints
router = APIRouter()


@router.post("/", response_model=QRResponse)
async def create_qr(request: QRRequest):
    """
    POST endpoint to generate a QR code.

    Request Body:
        - url (str): A valid URL provided by the client.

    Returns:
        - QRResponse: Contains the original URL and a base64 encoded QR code.
    """
    # Log the incoming request
    logger.info(f"Received QR generation request for URL: {request.url}")
    try:
        # Convert the provided URL into a QR code (base64 encoded string)
        qr_code_b64 = generate_qr_base64(str(request.url))

        # Log success
        logger.info("QR code generated successfully.")

        # Return the response schema with the URL and QR code
        return QRResponse(url=str(request.url), qr_code_base64=qr_code_b64)

    except Exception as e:
        # Log error details (with stack trace for debugging)
        logger.error(
            f"Error generating QR code for URL {request.url}: {e}", exc_info=True
        )
        # Re-raise the exception to let FastAPI handle the error response
        raise
