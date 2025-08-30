import pytest
from pydantic import ValidationError
from app.schemas.qr_schema import QRRequest, QRResponse


# Test: QRRequest should accept and normalize a valid URL
def test_qrrequest_valid_url():
    qr = QRRequest(url="https://example.com")
    # Pydantic appends a trailing slash to normalize the URL
    assert str(qr.url) == "https://example.com/"


# Test: QRRequest should raise a ValidationError for invalid URLs
def test_qrrequest_invalid_url():
    with pytest.raises(ValidationError):
        QRRequest(url="not-a-valid-url")


# Test: QRResponse should correctly store a base64-encoded QR image
def test_qrresponse_schema():
    resp = QRResponse(qr_code_base64="data:image/png;base64,abcd")
    # Ensure the base64 string begins with the expected prefix
    assert resp.qr_code_base64.startswith("data:image/png;base64,")
