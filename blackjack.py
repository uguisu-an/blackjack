import random
from blackjack.game import Game
from blackjack.deck import generate_deck

def main():
    deck = generate_deck()
    dealer = []
    player = []

    game = Game(deck, dealer, player)
    game.start()
    if game.is_over():
        game.stop()
        return

    dealer_is_stand = False
    player_is_stand = False
    while not player_is_stand:
        game.show_state()
        print('hit or stand?')
        # playerは任意でHit
        choice = lambda d: (d, True)
        player, player_is_stand = choice(player)
        if game.is_over():
            break
        # dealerは17点以上になるまで自動でHit
        choice = lambda d: (d, True)
        dealer, dealer_is_stand = choice(dealer)
        if game.is_over():
            break

    game.stop()


if __name__ == '__main__':
    main()