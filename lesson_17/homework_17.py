import requests
from pathlib import Path

# 🔹 Папка, де лежить цей скрипт
SCRIPT_DIR = Path(__file__).resolve().parent

NASA_API_URL = "https://images-api.nasa.gov/search"
PARAMS = {
    "q": "mars",
    "media_type": "image"
}

response = requests.get(NASA_API_URL, params=PARAMS)
response.raise_for_status()

data = response.json()
items = data["collection"]["items"][:2]

nasa_ids = []
image_urls = []

for item in items:
    nasa_id = item["data"][0]["nasa_id"]
    image_url = item["links"][0]["href"]

    nasa_ids.append(nasa_id)
    image_urls.append(image_url)

print(f"NASA IDs: {nasa_ids}")
print(f"Image URLs: {image_urls}")

for index, url in enumerate(image_urls, start=1):
    img_response = requests.get(url)
    img_response.raise_for_status()

    file_path = SCRIPT_DIR / f"mars_photo{index}.jpg"

    with open(file_path, "wb") as file:
        file.write(img_response.content)

    print(f"Збережено: {file_path}")
