import random
import blackjack.deck as deck
import blackjack.hand as hand
import blackjack.result as result
from blackjack.browser import SimpleBrowser


class Game:
    def __init__(self, deck_, dealer, player):
        self.deck = deck_
        self.dealer = dealer
        self.player = player
        self.browser = SimpleBrowser()
    
    def start(self):
        random.shuffle(self.deck)
        for _ in range(2):
            self.deck, self.player = deck.deal(self.deck, self.player)
            self.deck, self.dealer = deck.deal(self.deck, self.dealer)

    def stop(self):
        self.show_state(hole=0)
        self.show_result()
    
    def is_over(self):
        d = hand.sum_of_point([c.number for c in self.dealer])
        p = hand.sum_of_point([c.number for c in self.player])
        return (
            hand.is_blackjack(d)
            or hand.is_busted(d)
            or hand.is_blackjack(p)
            or hand.is_busted(p)
        )
    
    def is_double_blackjack(self):
        return (
            hand.is_blackjack(self.dealer)
            and hand.is_blackjack(self.player)
        )
    
    def show_result(self):
        self.browser.show_result(self.get_result())
    
    def show_state(self, hole=1):
        self.browser.show_state(self.dealer, self.player, hole=hole)
    
    # TODO: 敗因もつける？
    def get_result(self):
        d = hand.sum_of_point([c.number for c in self.dealer])
        p = hand.sum_of_point([c.number for c in self.player])
        if self.is_double_blackjack():
            return result.DRAW
        if hand.is_blackjack(d) or hand.is_busted(p):
            return result.LOSE
        if hand.is_blackjack(p) or hand.is_busted(d):
            return result.WIN
        if d > p:
            return result.LOSE
        if d < p:
            return result.WIN
        return result.DRAW