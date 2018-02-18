from blackjack.models.point import Point, point


def test_number_to_point():
    assert point(1) == 1
    assert point(2) == 2
    assert point(11) == 10

def test_zero_point():
    assert Point() == 0

def test_point_with_ace():
    assert Point([1]) == 11
    assert Point([1, 1]) == 12
    assert Point([12, 13, 1]) == 21
    assert Point([10, 11, 1, 1]) == 22

def test_adding_point():
    assert Point() + Point([1]) == 11
    assert Point([5]) + [11] == 15

def test_point_equality():
    assert Point([1]) == Point([5, 6])