"""
qr_service.py

This module provides the service logic for generating QR codes
and returning them as base64 encoded strings.
"""

import qrcode
import io
import base64
from app.core.config import logger


def generate_qr_base64(url: str) -> str:
    """
    Generate a QR code from a given URL and return it as a base64 string.

    Args:
        url (str): The URL to be encoded into the QR code.

    Returns:
        str: A base64 encoded PNG image of the generated QR code,
             prefixed with the data URI scheme (data:image/png;base64,...).
    """
    logger.info(f"Generating QR code for URL: {url}")
    try:
        # Initialize the QRCode object with version, size, and border settings
        qr = qrcode.QRCode(version=1, box_size=10, border=5)

        # Add data (the URL) to the QR code
        qr.add_data(url)
        qr.make(fit=True)

        # Create the QR image (black QR on white background)
        img = qr.make_image(fill="black", back_color="white")
        logger.debug("QR image object created successfully.")

        # Save the QR image into a memory buffer (instead of saving to disk)
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        logger.debug("QR image saved to memory buffer.")

        # Encode the binary image data to base64
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        logger.debug("QR image encoded to base64 successfully.")

        logger.info("QR code generation completed successfully.")
        
        # Return the image as a data URI (usable directly in HTML <img src=...>)
        return f"data:image/png;base64,{img_str}"
    except Exception as e:
        # Log errors with traceback info
        logger.error(f"Error in generate_qr_base64 for URL {url}: {e}", exc_info=True)
        raise
