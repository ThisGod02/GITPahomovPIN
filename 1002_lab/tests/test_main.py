"""Тесты Todo API."""
from fastapi.testclient import TestClient
from src.main import app
client = TestClient(app)
def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["message"] == "Todo API v1.0.0"
def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"
def test_create_todo():
    r = client.post("/todos", json={"title": "Test Task", "description": "d", "category": "test"})
    assert r.status_code == 201
    assert r.json()["title"] == "Test Task"
def test_get_todos():
    client.post("/todos", json={"title": "Task 1"})
    r = client.get("/todos")
    assert r.status_code == 200
    assert len(r.json()) >= 1
def test_get_todo_not_found():
    r = client.get("/todos/non-existent-id")
    assert r.status_code == 404
