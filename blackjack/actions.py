import blackjack.deck as dk
import blackjack.hand as hd


# カードを引く
def hit(deck, hand):
    _, h = dk.deal(deck, hand)
    return (h, False)

# 引くのをやめる
def stand(deck, hand):
    return (hand, True)

# playerは任意でHit
def player_hit_or_stand(deck, hand, is_stand):
    if is_stand:
        return stand(deck, hand)
    print('hit or stand?')
    if 'h' not in input():
        return stand(deck, hand)
    return hit(deck, hand)

# dealerは17点以上になるまでHit
def dealer_hit_or_stand(deck, hand, is_stand):
    if is_stand or hd.sum_of_point(hand) > 16:
        return stand(deck, hand)
    return hit(deck, hand)