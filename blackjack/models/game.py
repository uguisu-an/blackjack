import random
import blackjack.models.result as result
from blackjack import Deck, Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Player('Dealer', self.deck, [])
        self.player = Player('Player', self.deck, [])
    
    def begin(self):
        random.shuffle(self.deck)
        for _ in range(2):
            self.player.hit()
            self.dealer.hit()
    
    @property
    def turn_is_over(self):
        return (
            self.dealer.point >= 21
            or self.player.point >= 21
        )
    
    @property
    def game_is_over(self):
        return (
            self.player.is_stand()
            or self.turn_is_over
        )
    
    @property
    def game_result(self):
        if not self.game_is_over:
            return None
        return result.judge_from_point(
            self.dealer.point, self.player.point
        )
    