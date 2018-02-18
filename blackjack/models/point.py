import tramp.number as nm
import blackjack.models.result as result


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


class Point:
    def __init__(self, numbers=[]):
        self._numbers = numbers

    def __eq__(self, other):
        return self.total == other
    
    def __add__(self, other):
        return Point([*self, *other])
    
    def __iter__(self):
        return iter(self._numbers)
    
    @property
    def total(self):
        s = 0
        for n in sorted(self._numbers, reverse=True):
            s += point(n)
            if n == 1 and s <= 11:
                s += 10
        return s
    