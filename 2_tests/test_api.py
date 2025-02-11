from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_process_data():
    with open("test_data.csv", "rb") as file:
        response = client.post("/process", files={"file": file})
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]