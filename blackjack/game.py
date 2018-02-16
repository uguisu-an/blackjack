from blackjack.deck import Deck
from blackjack.player import Player
import blackjack.result as res
from blackjack.browser import SimpleBrowser


def hit_or_stand(player):
    if player.is_stand():
        return
    print('h[it] or s[tand]')
    choice = input()
    if 'h' in choice:
        player.hit()
    else:
        player.stand()
    
def auto_hit_or_stand(player):
    if player.is_stand():
        return
    if player.hand.sum_of_points() < 17:
        player.hit()
    else:
        player.stand()



class Game:
    browser = SimpleBrowser()

    def start(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Player(self.deck)
        self.player = Player(self.deck)
        for _ in range(2):
            self.player.hit()
            self.dealer.hit()
        
        print(self.player.hand.sum_of_points())
        print(self.dealer.hand.sum_of_points())

        if self.should_stop(self.dealer) or self.should_stop(self.player):
            self.stop()
            return
        
        while not self.player.is_stand():
            self.show_state()
            hit_or_stand(self.player)
            if self.should_stop(self.player):
                break
            auto_hit_or_stand(self.dealer)
            if self.should_stop(self.dealer):
                break
        self.stop()
    
    def stop(self):
        self.show_state(hole=0)
        self.show_result(self.finalResult())
    
    def should_stop(self, player):
        if player.is_blackjack() or player.is_busted():
            return True
        return False

    # TODO: 敗因もつける？
    def finalResult(self):
        if self.dealer.is_blackjack() and self.player.is_blackjack():
            return res.DRAW
        if self.player.is_blackjack():
            return res.WIN
        if self.player.is_busted():
            return res.LOSE
        if self.dealer.is_blackjack():
            return res.LOSE
        if self.dealer.is_busted():
            return res.WIN
        if self.dealer.hand > self.player.hand:
            return res.LOSE
        if self.dealer.hand < self.player.hand:
            return res.WIN
        return res.DRAW
    
    def show_result(self, result):
        self.browser.show_result(result)
    
    def show_state(self, hole=1):
        self.browser.show_state(self.dealer, self.player, hole=hole)
    