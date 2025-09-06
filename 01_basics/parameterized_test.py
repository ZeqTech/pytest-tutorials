import pytest


def add(*args):
    return sum(args)


@pytest.mark.parametrize("a,b,expected", [(2, 3, 5), (10, 5, 15), (0, 7, 7)])
def test_add_param(a, b, expected):
    assert add(a, b) == expected
