import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_create_qr_success():
    """
    Test case: Valid URL request
    - Send a valid HTTPS URL
    - Expect HTTP 200
    - Expect a QR code base64 string in the response
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/qr/", json={"url": "https://example.com"})
    assert response.status_code == 200
    data = response.json()
    assert "qr_code_base64" in data
    assert data["qr_code_base64"].startswith("data:image/png;base64,")


@pytest.mark.asyncio
async def test_create_qr_invalid_url():
    """
    Test case: Invalid URL request
    - Send an invalid URL (not matching HttpUrl)
    - Expect HTTP 422 (Unprocessable Entity)
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/qr/", json={"url": "not-a-url"})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_create_qr_empty_url():
    """
    Test case: Empty URL request
    - Send empty string
    - Expect HTTP 422 because it's not a valid HttpUrl
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/qr/", json={"url": ""})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_create_qr_http_url():
    """
    Test case: Valid HTTP (not HTTPS) URL
    - Pydantic's HttpUrl accepts both http:// and https://
    - Expect HTTP 200 with valid QR code response
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/qr/", json={"url": "http://example.org"})
    assert response.status_code == 200
    data = response.json()
    assert "qr_code_base64" in data
    assert data["qr_code_base64"].startswith("data:image/png;base64,")
