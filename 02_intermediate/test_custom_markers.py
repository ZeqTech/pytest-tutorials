import pytest


@pytest.mark.slow
def test_big_computation():
    assert sum(range(10**6)) > 0
