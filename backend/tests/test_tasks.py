import pytest


class TestTasksAPI:
    @pytest.fixture(autouse=True)
    def _setup(self, client):
        self.client = client

    def test_create_task(self):
        response = self.client.post("/tasks", json={"title": "Test task", "completed": False})
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Test task"
        assert data["completed"] is False
        assert "id" in data

    def test_get_tasks(self):
        response = self.client.get("/tasks")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_update_task(self):
        create = self.client.post("/tasks", json={"title": "Old title", "completed": False})
        task_id = create.json()["id"]
        response = self.client.put(f"/tasks/{task_id}", json={"title": "New title", "completed": True})
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "New title"
        assert data["completed"] is True

    def test_delete_task(self):
        create = self.client.post("/tasks", json={"title": "To delete", "completed": False})
        task_id = create.json()["id"]
        response = self.client.delete(f"/tasks/{task_id}")
        assert response.status_code == 200

    def test_delete_not_found(self):
        response = self.client.delete("/tasks/999999")
        assert response.status_code == 404
        assert response.json()['detail'] == "Task not found"
