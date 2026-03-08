from http import HTTPStatus

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

HTTP_OK = HTTPStatus.OK.value
HTTP_NOT_FOUND = HTTPStatus.NOT_FOUND.value


def test_root():
    response = client.get("/")
    assert response.status_code == HTTP_OK


def test_create_task():
    payload = {
        "title": "Learn AI DevX",
        "description": "Build a platform",
    }
    response = client.post("/tasks/", json=payload)
    assert response.status_code == HTTP_OK
    data = response.json()
    assert data["title"] == "Learn AI DevX"
    assert "id" in data


def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == HTTP_OK
    assert isinstance(response.json(), list)


def test_get_task_not_found():
    response = client.get("/tasks/00000000-0000-0000-0000-000000000000")
    assert response.status_code == HTTP_NOT_FOUND


def test_delete_task():
    create = client.post("/tasks/", json={"title": "Delete Me"})
    task_id = create.json()["id"]
    delete = client.delete(f"/tasks/{task_id}")
    assert delete.status_code == HTTP_OK
