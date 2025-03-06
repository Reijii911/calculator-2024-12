from calculator.minimum import minimum


def test_minimum():
    assert minimum(5, 6) == 5
    assert minimum(1, 6) == 1
    assert minimum(2, 2) == 2
