import qrcode
import io
import base64
from app.core.config import logger


def generate_qr_base64(url: str) -> str:
    logger.info(f"Generating QR code for URL: {url}")
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")
        logger.debug("QR image object created successfully.")

        # Save to memory
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        logger.debug("QR image saved to memory buffer.")

        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        logger.debug("QR image encoded to base64 successfully.")

        logger.info("QR code generation completed successfully.")
        return f"data:image/png;base64,{img_str}"
    except Exception as e:
        logger.error(f"Error in generate_qr_base64 for URL {url}: {e}", exc_info=True)
        raise
