import requests
import pytest
import logging
from pathlib import Path

BASE_URL = "http://127.0.0.1:8080"


log_file = Path("C:/Users/oleksii.yevplov/qa-automation-pyton/lesson_21/test_search.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file, mode='w', encoding='utf-8'),
        logging.StreamHandler() 
    ]
)

@pytest.fixture(scope="class")
def login():
    logging.info("Отримання токена доступу")
    r = requests.post(f"{BASE_URL}/auth", auth=("test_user", "test_pass"))
    r.raise_for_status()  
    token = r.json()["access_token"]
    logging.info("Токен отримано")
    return token


@pytest.mark.parametrize("sort_by, limit", [
    (None, None),
    ("price", 5),
    ("year", 10),
    ("engine_volume", 3),
    ("brand", 7)
])
def test_search_cars(login, sort_by, limit):
    params = {}
    if sort_by:
        params["sort_by"] = sort_by
    if limit:
        params["limit"] = limit

    logging.info(f"Виконуємо GET /cars з params={params}")
    r = requests.get(f"{BASE_URL}/cars", headers={"Authorization": f"Bearer {login}"}, params=params)
    
    logging.info(f"Статус код відповіді: {r.status_code}")
    assert r.status_code == 200

    data = r.json()
    logging.info(f"Отримано {len(data)} автомобілів")
    assert isinstance(data, list)

    if limit:
        assert len(data) <= limit

   
    if sort_by:
        for i in range(len(data) - 1):
            assert data[i][sort_by] <= data[i + 1][sort_by]
