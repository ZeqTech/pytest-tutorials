import pytest
from typing import Any


@pytest.fixture
def sample_data() -> dict[str, Any]:
    return {"username": "alice", "id": 1}
