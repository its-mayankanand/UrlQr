import requests
import validators

BASE_URL = "http://34.100.166.62"         # replace with your deployed URL

# List of test URLs
test_urls = [
    "https://google.com",
    "https://github.com",
    "https://openai.com",
    "https://example.org",
    "https://invalid-url",  # invalid example
    "not-a-url"             # another invalid example
]

for url in test_urls:
    try:
        response = requests.post(f"{BASE_URL}/api/v1/qr/", json={"url": url})
    except Exception as e:
        print(f"[ERROR] Could not reach API for URL {url}: {e}")
        continue

    # Check response status
    if response.status_code == 200:
        # Validate URL format
        if validators.url(url):
            data = response.json()
            if "qr_code_base64" in data and data["qr_code_base64"]:
                print(f"[PASS] QR generated correctly for: {url}")
            else:
                print(f"[FAIL] QR not generated for valid URL: {url}")
        else:
            print(f"[FAIL] Invalid URL should not generate QR: {url}")
    else:
        print(f"[FAIL] API returned {response.status_code} for: {url}")

