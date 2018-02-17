BLACKJACK = 21
WIN = 1
DRAW = 0
LOSE = -1
BUSTED = -2


def is_blackjack(point):
    return point == BLACKJACK

def is_busted(point):
    return point > BLACKJACK

def judge_from_point(dealer_point, player_point):
    if is_busted(player_point):
        return LOSE
    if is_busted(dealer_point):
        return WIN
    if dealer_point > player_point:
        return LOSE
    if dealer_point < player_point:
        return WIN
    return DRAW