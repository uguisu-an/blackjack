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
        if self.player.is_stand():
            return
        self.show_state()
        self.player.hit_or_stand()
        if self.is_over():
            return
        self.dealer.hit_or_stand()
        if self.is_over():
            return
        self.turn()

    def end(self):
        self.show_state(hole=0)
        self.show_result()
    
    def is_over(self):
        a, b = self.dealer, self.player
        return (
            a.is_blackjack()
            or b.is_blackjack()
            or a.is_busted()
            or b.is_busted()
        )
    
    def show_result(self):
        res = judge(self.dealer, self.player)
        self.browser.show_result(res)
    
    def show_state(self, hole=1):
        self.browser.show_state(self.dealer, self.player, hole=hole)


def judge(dealer, player):
    return result.judge_from_point(dealer.point, player.point)
    