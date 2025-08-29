from fastapi import APIRouter
from app.schemas.qr_schema import QRRequest, QRResponse
from app.services.qr_service import generate_qr_base64

router = APIRouter()

@router.post("/", response_model=QRResponse)
async def create_qr(request: QRRequest):
    qr_code_b64 = generate_qr_base64(str(request.url))
    return QRResponse(url=(request.url), qr_code_base64=qr_code_b64)


