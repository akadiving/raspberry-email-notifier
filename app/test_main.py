from fastapi.testclient import TestClient
from tasks import celery, send_json
from main import app
import json

client = TestClient(app)


def test_invoke_task():
    data = json.load(open("app/fixtures/sample_data.json", "r"))
    response = send_json.delay(data=data, max=3)
    assert type(response) == celery.AsyncResult


def test_post_task():
    response = client.get("/")
    assert type(response.json()) == str
