import random
import blackjack.deck as dk
import blackjack.hand as hd
import blackjack.result as result
from blackjack.browser import SimpleBrowser


class Game:
    def __init__(self, deck, dealer, player):
        self.deck = deck
        self.dealer = dealer
        self.player = player
        self.browser = SimpleBrowser()
    
    def begin(self):
        random.shuffle(self.deck)
        for _ in range(2):
            self.player.hit()
            self.dealer.hit()
    
    def turn(self):
        self.player.hit_or_stand()
        if self.is_over():
            return
        self.dealer.hit_or_stand()

    def is_over(self):
        return (
            self.player.is_stand()
            or self.dealer.point >= result.BLACKJACK
            or self.player.point >= result.BLACKJACK
        )
    
    def show_result(self):
        res = result.judge_from_point(self.dealer.point, self.player.point)
        self.browser.show_result(res)
    
    def show_state(self, hole=1):
        self.browser.show_state(self.dealer, self.player, hole=hole)
