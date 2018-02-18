import random
import blackjack.models.result as result
from blackjack import Deck, Dealer, Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(self.deck, [])
        self.player = Player(self.deck, [])
        self.game_result = None
        self.game_is_over = False
        self.turn_is_over = False
    
    def begin(self):
        random.shuffle(self.deck)
        for _ in range(2):
            self.player.hit()
            self.dealer.hit()

    def update_result(self):
        self.turn_is_over = (
            self.dealer.point >= 21
            or self.player.point >= 21
        )
        self.game_is_over = (
            self.player.is_stand()
            or self.turn_is_over
        )
        if not self.game_is_over:
            return
        self.game_result = result.judge_from_point(
            self.dealer.point,
            self.player.point
        )
    