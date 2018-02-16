from random import shuffle


def createDeck(deck=[]):
    for x in range(4):
        for y in range(13):
            deck = [(x, y), *deck]
    return deck

def point(card):
    _, n = card
    if n == 0:
        return (1, 11)
    if n > 8:
        return (10, 10)
    return (n+1, n+1)

def sum_of(hand):
    s = 0
    for c in sorted(hand, reverse=True):
        p = point(c)
        if s + p[1] > 21:
            s += p[0]
        else:
            s += p[1]
    return s

def is_blackjack(hand):
    return sum_of(hand) == 21

def deal(deck, to):
    return [deck.pop(), *to]

def showHand(hand, hole=0):
    for c in hand:
        if hole:
            print('* hole *')
            hole -= 1
            continue
        print(suit(c), c[1] + 1, '->', point(c)[0])

def suit(c):
    t, _ = c
    return ['♠︎', '♣︎', '♡', '♢'][t]

def hit_or_stand(deck, hand, player_is_stand):
    if player_is_stand:
        return stand(deck, hand)
    print('h[it] or s[tand]')
    choice = input()
    if 'h' in choice:
        return hit(deck, hand)
    else:
        return stand(deck, hand)
    
def auto_hit_or_stand(deck, hand, player_is_stand):
    if player_is_stand:
        return stand(deck, hand)
    if sum_of(hand) > 16:
        return stand(deck, hand) 
    else:
        return hit(deck, hand)

def hit(deck, hand):
    return (deal(deck, to=hand), False)

def stand(deck, hand):
    return (hand, True)

def is_busted(hand):
    return sum_of(hand) > 21

def show(dealer, player, hole=1):
    print('dealer:')
    showHand(dealer, hole=hole)
    print('')
    print('player:')
    showHand(player)
    print('')
    
def main():
    deck = createDeck()
    shuffle(deck)
    dealer = []
    player = []
    for _ in range(2):
        player = deal(deck, to=player)
        dealer = deal(deck, to=dealer)

    show(dealer, player)

    if is_blackjack(dealer) and is_blackjack(player):
        print('Draw. (Natural Blackjack)')
        return
    elif is_blackjack(dealer):
        print('You lose... (Natural Blackjack)')
        return
    elif is_blackjack(player):
        print('You win! (Natural Blackjack)')
        return
    
    player_is_stand = False
    dealer_is_stand = False
    
    while not player_is_stand:
        show(dealer, player)
        player, player_is_stand = hit_or_stand(deck, player, player_is_stand)
        if is_blackjack(player):
            print('You win! (Blackjack)')
            return
        if is_busted(player):
            print('You lose... (Bust)')
            return
        dealer, dealer_is_stand = auto_hit_or_stand(deck, dealer, dealer_is_stand)
        if is_blackjack(dealer):
            print('You lose... (Blackjack)')
            return
        if is_busted(dealer):
            print('You win! (Bust)')
            return
    
    show(dealer, player, hole=0)
    if sum_of(dealer) > sum_of(player):
        print('You lose...')
        return
    if sum_of(dealer) < sum_of(player):
        print('You win!')
        return
    print('Draw.')


if __name__ == '__main__':
    main()