from fastapi.testclient import TestClient
from src.main import app
import pytest

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_create_task():
    response = client.post("/tasks/", json={"title": "Learn AI DevX", "description": "Build a platform"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Learn AI DevX"
    assert "id" in data

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_task_not_found():
    response = client.get("/tasks/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404

def test_delete_task():
    create = client.post("/tasks/", json={"title": "Delete Me"})
    task_id = create.json()["id"]
    delete = client.delete(f"/tasks/{task_id}")
    assert delete.status_code == 200
