from square import get_square

def test_sq():
    x = 5
    res = get_square(x)
    assert res == 25


def test_sq1():
    x = -3
    res1 = get_square(x)
    assert res1 == 9
