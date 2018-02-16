import tramp.number as number
import blackjack.result as result


def point(number_):
    assert number_ in number.All
    if number_ > 10:
        return 10
    return number_

def sum_of_point(numbers):
    s = 0
    for n in sorted(numbers, reverse=True):
        s += point(n)
        if n == 1 and not is_busted(s+10):
            s += 10
    return s

def diff(a, b):
    return sum_of_point(a) - sum_of_point(b)

def is_blackjack(point_):
    return point_ == result.BLACKJACK

def is_busted(point_):
    return point_ > result.BLACKJACK