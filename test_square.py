from square import get_square

def test_sq():
    x = 5
    res = get_square(5)
    res == 25
    assert get_square(5) == 25