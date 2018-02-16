BLACKJACK = 21

def is_blackjack(hand):
    return sum_of(hand) == BLACKJACK

def is_busted(hand):
    return sum_of(hand) > BLACKJACK

def sum_of(hand):
    s = 0
    for c in sorted(hand, reverse=True):
        p = c.point()
        if s + p[1] > 21:
            s += p[0]
        else:
            s += p[1]
    return s