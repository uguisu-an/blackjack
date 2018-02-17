from blackjack import Game, Deck, Dealer, Player


def main():
    deck = Deck()
    dealer = Dealer(deck, [])
    player = Player(deck, [])
    game = Game(deck, dealer, player)
    game.begin()
    while not game.is_over():
        game.show_state()
        game.turn()
    game.show_state(hole=False)
    game.show_result()


if __name__ == '__main__':
    main()