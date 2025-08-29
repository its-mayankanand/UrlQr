from pydantic import BaseModel, HttpUrl
from app.core.config import logger  # logging from global config


class QRRequest(BaseModel):
    url: HttpUrl

    def __init__(self, **data):
        super().__init__(**data)
        logger.debug(f"Validated QRRequest with url={self.url}")


class QRResponse(BaseModel):
    qr_code_base64: str

    def __init__(self, **data):
        super().__init__(**data)
        logger.debug("QRResponse created successfully.")
