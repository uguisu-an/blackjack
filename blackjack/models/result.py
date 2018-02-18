BLACKJACK = 21
WIN = 1
DRAW = 0
LOSE = -1
BUSTED = -2


def judge_from_point(dealer_point, player_point):
    if player_point > BLACKJACK:
        return LOSE
    if dealer_point > BLACKJACK:
        return WIN
    if dealer_point > player_point:
        return LOSE
    if dealer_point < player_point:
        return WIN
    return DRAW