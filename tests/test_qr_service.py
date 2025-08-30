import base64
from app.services.qr_service import generate_qr_base64

def test_generate_qr_base64_returns_valid_base64():
    url = "https://example.com"
    qr_b64 = generate_qr_base64(url)

    assert qr_b64.startswith("data:image/png;base64,")
    # ensure it's decodable
    b64_data = qr_b64.split(",")[1]
    decoded = base64.b64decode(b64_data)
    assert isinstance(decoded, bytes)
    assert len(decoded) > 0
