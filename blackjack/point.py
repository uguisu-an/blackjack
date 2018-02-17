import tramp.number as nm
import blackjack.result as result


def point(number):
    assert number in nm.All
    if number > 10:
        return 10
    return number

def sum_of_point(numbers):
    s = 0
    for number in sorted(numbers, reverse=True):
        s += point(number)
        if number == 1 and not result.is_busted(s+10):
            s += 10
    return s