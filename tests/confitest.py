import pytest

from fastapi.testclient import TestClient
from asyncio_examples.asyncio_example import app

@pytest.fixture()
def request():
    return TestClient(app)