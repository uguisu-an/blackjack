from blackjack.deck import Deck
import blackjack.player as Player
import blackjack.result as res
from blackjack.browser import SimpleBrowser


def hit(deck, hand):
    return (deck.deal(hand), False)

def stand(deck, hand):
    return (hand, True)

def hit_or_stand(deck, hand, player_is_stand):
    if player_is_stand:
        return stand(deck, hand)
    print('h[it] or s[tand]')
    choice = input()
    if 'h' in choice:
        return hit(deck, hand)
    else:
        return stand(deck, hand)
    
def auto_hit_or_stand(deck, hand, player_is_stand):
    if player_is_stand:
        return stand(deck, hand)
    if Player.sum_of(hand) > 16:
        return stand(deck, hand) 
    else:
        return hit(deck, hand)



class Game:
    dealer = []
    player = []
    browser = SimpleBrowser()

    def start(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = []
        self.player = []
        for _ in range(2):
            self.player = self.deck.deal(self.player)
            self.dealer = self.deck.deal(self.dealer)

        if self.should_stop(self.dealer) or self.should_stop(self.player):
            self.stop()
            return
        
        player_is_stand = False
        dealer_is_stand = False
        
        while not player_is_stand:
            self.show_state()
            self.player, player_is_stand = hit_or_stand(self.deck, self.player, player_is_stand)
            if self.should_stop(self.player):
                break
            self.dealer, dealer_is_stand = auto_hit_or_stand(self.deck, self.dealer, dealer_is_stand)
            if self.should_stop(self.dealer):
                break
        self.stop()
    
    def stop(self):
        self.show_state(hole=0)
        self.show_result(self.finalResult())
    
    def should_stop(self, player):
        if Player.is_blackjack(player) or Player.is_busted(player):
            return True
        return False

    # TODO: 敗因もつける？
    def finalResult(self):
        if Player.is_blackjack(self.dealer) and Player.is_blackjack(self.player):
            return res.DRAW
        if Player.is_blackjack(self.dealer):
            return res.LOSE
        if Player.is_busted(self.dealer):
            return res.WIN
        if Player.is_blackjack(self.player):
            return res.WIN
        if Player.is_busted(self.player):
            return res.LOSE
        if Player.sum_of(self.dealer) > Player.sum_of(self.player):
            return res.LOSE
        if Player.sum_of(self.dealer) < Player.sum_of(self.player):
            return res.WIN
        return res.DRAW
    
    def show_result(self, result):
        self.browser.show_result(result)
    
    def show_state(self, hole=1):
        self.browser.show_state(self.dealer, self.player, hole=hole)
    