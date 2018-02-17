from blackjack import Deck, Dealer, Player
from blackjack.game2 import Game
from blackjack.hand_component import HandComponent
from blackjack.hit_or_stand_component import HitOrStandComponent
from blackjack.result_component import ResultComponent
from blackjack.dispatcher import dispatcher


def main():
    deck = Deck()
    dealer = Dealer(deck, [])
    player = Player(deck, [])

    # TODO: 雑多すぎる
    dhc = HandComponent(dispatcher, dealer, hole=True)
    phc = HandComponent(dispatcher, player, hole=False)
    hsc = HitOrStandComponent(dispatcher)
    rsc = ResultComponent(dispatcher)

    game = Game(deck, dealer, player)
    game.begin()
    while not game.is_over():
        game.turn()
    dhc.hole = False
    game.end()


if __name__ == '__main__':
    main()