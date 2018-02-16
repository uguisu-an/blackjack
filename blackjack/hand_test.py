from blackjack.hand import point, sum_of_point, is_blackjack, is_busted


def test_point():
    assert point(10) == 10
    assert point(11) == 10

def test_sum_of_point():
    assert sum_of_point([2, 3, 4, 5, 6, 7, 8, 9]) == 44

def test_sum_of_point_with_one():
    assert sum_of_point([1, 10]) == 21
    assert sum_of_point([1, 10, 10]) == 21

def test_sum_of_point_with_picture_card():
    assert sum_of_point([11, 12, 13]) == 30

def test_sum_of_point_without_card():
    assert sum_of_point([]) == 0

def test_blackjack():
    assert not is_blackjack(20)
    assert is_blackjack(21)

def test_bust():
    assert not is_busted(21)
    assert is_busted(22)