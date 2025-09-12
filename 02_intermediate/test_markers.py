import pytest


@pytest.mark.skip(reason="Not implemented yet")
def test_feature():
    assert False


@pytest.mark.xfail(reason="Known bug in version 1.0")
def test_known_issue():
    assert 1 / 0
