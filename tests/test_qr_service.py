import base64
from app.services.qr_service import generate_qr_base64


# Test: Ensure generate_qr_base64 returns a valid base64-encoded QR image
def test_generate_qr_base64_returns_valid_base64():
    url = "https://example.com"
    qr_b64 = generate_qr_base64(url)

    # The returned string should start with the correct data URL prefix
    assert qr_b64.startswith("data:image/png;base64,")

    # Extract the base64 part and verify it can be decoded into bytes
    b64_data = qr_b64.split(",")[1]
    decoded = base64.b64decode(b64_data)

    # Ensure decoded content is valid binary data (non-empty bytes)
    assert isinstance(decoded, bytes)
    assert len(decoded) > 0
