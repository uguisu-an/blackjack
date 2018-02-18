import random
import blackjack.models.result as result
from blackjack import Deck, Dealer, Player


class Game:
    def __init__(self):
        self._deck = Deck()
        self._dealer = Dealer(self._deck, [])
        self._player = Player(self._deck, [])
        self._game_result = None
        self._game_is_over = False
        self._turn_is_over = False
    
    def begin(self):
        random.shuffle(self._deck)
        for _ in range(2):
            self._player.hit()
            self._dealer.hit()

    def update_result(self):
        self._turn_is_over = (
            self._dealer.point >= 21
            or self._player.point >= 21
        )
        self._game_is_over = (
            self._player.is_stand()
            or self._turn_is_over
        )
        if not self._game_is_over:
            return
        self._game_result = result.judge_from_point(
            self._dealer.point,
            self._player.point
        )
    