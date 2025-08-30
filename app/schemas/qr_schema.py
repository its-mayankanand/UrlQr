"""
qr_schema.py

This module defines the request and response schemas for the QR code API.
It ensures data validation using Pydantic models.
"""

from pydantic import BaseModel, HttpUrl
from app.core.config import logger                 # using the global logger


class QRRequest(BaseModel):
    """
    Schema for incoming QR generation requests.

    Attributes:
        url (HttpUrl): The URL to be converted into a QR code.
    """
    url: HttpUrl

    def __init__(self, **data):
        # Call the parent constructor for validation
        super().__init__(**data)

        # Log debug info when a valid request object is created
        logger.debug(f"Validated QRRequest with url={self.url}")


class QRResponse(BaseModel):
    """
    Schema for outgoing QR generation responses.

    Attributes:
        qr_code_base64 (str): Base64 encoded string of the generated QR code.
    """
    qr_code_base64: str

    def __init__(self, **data):
        # Call the parent constructor
        super().__init__(**data)

        # Log debug info when a response object is successfully created
        logger.debug("QRResponse created successfully.")
