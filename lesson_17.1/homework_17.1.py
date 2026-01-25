import requests
from pathlib import Path


BASE_URL = "http://127.0.0.1:8080"  
SCRIPT_DIR = Path(__file__).parent   
FILE_TO_UPLOAD = SCRIPT_DIR / "test_image.jpg"  


with open(FILE_TO_UPLOAD, "rb") as f:
    files = {"image": f}
    response = requests.post(f"{BASE_URL}/upload", files=files)

if response.status_code == 201:
    data = response.json()
    uploaded_url = data.get("image_url")
    print(f"Файл завантажено: {uploaded_url}")
else:
    raise Exception(f"Помилка завантаження: {response.status_code}")


filename = Path(uploaded_url).name


get_response = requests.get(
    f"{BASE_URL}/image/{filename}",
    headers={"Content-Type": "text"}
)

if get_response.status_code == 200:
    data = get_response.json()
    print(f"Отриманий URL через GET: {data.get('image_url')}")
else:
    raise Exception(f"Помилка GET: {get_response.status_code}")


delete_response = requests.delete(f"{BASE_URL}/delete/{filename}")

if delete_response.status_code == 200:
    data = delete_response.json()
    print(f"Файл видалено: {data.get('message')}")
else:
    raise Exception(f"Помилка DELETE: {delete_response.status_code}")
