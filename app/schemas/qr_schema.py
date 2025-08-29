from pydantic import BaseModel, HttpUrl

class QRRequest(BaseModel):
    url: HttpUrl

class QRResponse(BaseModel):
    qr_code_base64: str
     



