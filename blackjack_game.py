import random
from blackjack.game import Game
from blackjack.player import Dealer, Player
import blackjack.deck as dk

def main():
    deck, dealer, player = prepare_game()
    game = Game(deck, dealer, player)
    game.begin()
    if not game.is_over():
        game.turn()
    game.end()


def prepare_game():
    deck = dk.generate_deck()
    dealer = Dealer(deck, [])
    player = Player(deck, [])
    return deck, dealer, player


if __name__ == '__main__':
    main()