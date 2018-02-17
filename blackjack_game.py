from blackjack import Game, Deck, Dealer, Player


def main():
    deck = Deck()
    dealer = Dealer(deck, [])
    player = Player(deck, [])
    game = Game(deck, dealer, player)
    game.begin()
    if not game.is_over():
        game.turn()
    game.end()


if __name__ == '__main__':
    main()