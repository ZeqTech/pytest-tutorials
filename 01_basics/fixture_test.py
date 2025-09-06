import pytest
from typing import Any


@pytest.fixture
def sample_data() -> dict[str, Any]:
    return {"username": "alice", "id": 1}


def test_sample_data(sample_data: dict[str, Any]):
    assert sample_data["username"] == "alice"
    assert sample_data["id"] == 1
