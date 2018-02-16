from blackjack.deck import Deck
import blackjack.player as Player


def hit(deck, hand):
    return (deck.deal(hand), False)

def stand(deck, hand):
    return (hand, True)

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
    if Player.sum_of(hand) > 16:
        return stand(deck, hand) 
    else:
        return hit(deck, hand)

def show(dealer, player, hole=1):
    print('dealer:')
    showHand(dealer, hole=hole)
    print('')
    print('player:')
    showHand(player)
    print('')
    
def showHand(hand, hole=0):
    for c in hand:
        if hole:
            print('* hole *')
            hole -= 1
            continue
        print(c.suit, c.number, '>', c.point()[0])


def main():
    deck = Deck()
    deck.shuffle()
    dealer = []
    player = []
    for _ in range(2):
        player = deck.deal(player)
        dealer = deck.deal(dealer)

    show(dealer, player)

    if Player.is_blackjack(dealer) and Player.is_blackjack(player):
        print('Draw. (Natural Blackjack)')
        return
    elif Player.is_blackjack(dealer):
        print('You lose... (Natural Blackjack)')
        return
    elif Player.is_blackjack(player):
        print('You win! (Natural Blackjack)')
        return
    
    player_is_stand = False
    dealer_is_stand = False
    
    while not player_is_stand:
        show(dealer, player)
        player, player_is_stand = hit_or_stand(deck, player, player_is_stand)
        if Player.is_blackjack(player):
            print('You win! (Blackjack)')
            return
        if Player.is_busted(player):
            print('You lose... (Bust)')
            return
        dealer, dealer_is_stand = auto_hit_or_stand(deck, dealer, dealer_is_stand)
        if Player.is_blackjack(dealer):
            print('You lose... (Blackjack)')
            return
        if Player.is_busted(dealer):
            print('You win! (Bust)')
            return
    
    show(dealer, player, hole=0)
    if Player.sum_of(dealer) > Player.sum_of(player):
        print('You lose...')
        return
    if Player.sum_of(dealer) < Player.sum_of(player):
        print('You win!')
        return
    print('Draw.')


if __name__ == '__main__':
    main()