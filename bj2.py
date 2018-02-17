from blackjack import Deck, Dealer, Player
from blackjack.game2 import Game
from blackjack.hand_component import HandComponent
from blackjack.hit_or_stand_component import HitOrStandComponent
from blackjack.result_component import ResultComponent
from blackjack.dispatcher import dispatcher

import blackjack.actions as actions
import blackjack.result as result
import random


def main():
    deck = Deck()
    dealer = Dealer(deck, [])
    player = Player(deck, [])

    dhc = HandComponent(dispatcher, dealer, hole=True)
    phc = HandComponent(dispatcher, player, hole=False)
    rsc = ResultComponent(dispatcher)

    game = Game(deck, dealer, player)
    game.begin()

    while not game.is_over():
        game.turn()
        player.hit_or_stand()
        if game.is_over():
            dhc.hole = False
            return game.end()
        dealer.hit_or_stand()

    dhc.hole = False
    game.end()




if __name__ == '__main__':
    main()