import pytest
from pydantic import ValidationError
from app.schemas.qr_schema import QRRequest, QRResponse

def test_qrrequest_valid_url():
    qr = QRRequest(url="https://example.com")
    assert str(qr.url) == "https://example.com/"

def test_qrrequest_invalid_url():
    with pytest.raises(ValidationError):
        QRRequest(url="not-a-valid-url")

def test_qrresponse_schema():
    resp = QRResponse(qr_code_base64="data:image/png;base64,abcd")
    assert resp.qr_code_base64.startswith("data:image/png;base64,")


