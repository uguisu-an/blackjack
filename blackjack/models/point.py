import tramp.number as nm


def point(number):
    assert number in nm.All
    if number > 10:
        return 10
    return number


class Point:
    def __init__(self, numbers=[]):
        self._numbers = numbers

    def __eq__(self, other):
        return self.total == other
    
    def __lt__(self, other):
        return self.total < other
    
    def __le__(self, other):
        return self.total <= other
    
    def __gt__(self, other):
        return self.total > other
    
    def __ge__(self, other):
        return self.total >= other
    
    def __add__(self, other):
        return Point([*self, *other])
    
    def __str__(self):
        return str(self.total)
    
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
    