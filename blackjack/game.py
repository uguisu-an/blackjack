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
        self.browser.show_result(judge(self.dealer, self.player))
    
    def show_state(self, hole=1):
        self.browser.show_state(self.dealer, self.player, hole=hole)


def judge(a, b):
    if a.is_blackjack() and b.is_blackjack():
        return result.DRAW
    if a.is_blackjack() or b.is_busted():
        return result.LOSE
    if b.is_blackjack():
        return result.BLACKJACK
    if a.is_busted():
        return result.WIN
    if a.defeats(b):
        return result.LOSE
    if b.defeats(a):
        return result.WIN
    return result.DRAW
