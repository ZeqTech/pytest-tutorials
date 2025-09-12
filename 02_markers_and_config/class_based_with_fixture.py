import pytest


@pytest.fixture
def numbers():
    return [1, 2, 3]


class TestNumbers:
    def test_length(self, numbers):
        assert len(numbers) == 3

    def test_sum(self, numbers):
        assert sum(numbers) == 6
