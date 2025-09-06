def add(*args):
    return sum(args)


def test_add():
    result = add(2, 3)
    assert result == 5

    # result = add(2, 3, 4, 5)
    # assert result == 11
