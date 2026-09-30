import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.app import app


def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.data == b"Hello from AWS DevOps Project"


def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
    