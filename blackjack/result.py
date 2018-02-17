BLACKJACK = 21
WIN = 1
DRAW = 0
LOSE = -1
BUSTED = -2


def is_blackjack(point):
    return point == BLACKJACK

def is_busted(point):
    return point > BLACKJACK
