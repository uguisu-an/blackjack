import random
import blackjack.models.result as result
from blackjack import Deck, Player


class Game:
    """ゲームの情報を持つ."""

    def __init__(self):
        self.deck = Deck()
        self.dealer = Player('Dealer', self.deck, [])
        self.player = Player('Player', self.deck, [])
    
    #TODO: 読み取りだけに専念するべき？
    def begin(self):
        random.shuffle(self.deck)
        for _ in range(2):
            self.player.hit()
            self.dealer.hit()
    
    @property
    def turn_is_over(self):
        return (
            self.dealer.point >= result.BLACKJACK
            or self.player.point >= result.BLACKJACK
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
    