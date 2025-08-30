import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_create_qr_success():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/qr/", json={"url": "https://example.com"})
    assert response.status_code == 200
    assert "qr_code_base64" in response.json()


@pytest.mark.asyncio
async def test_create_qr_invalid_url():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/qr/", json={"url": "not-a-url"})
    assert response.status_code == 422
