import blackjack.deck as dk
import blackjack.hand as hd


class AbstractPlayer:
    def __init__(self, deck=[], hand=[]):
        self.deck = deck
        self.hand = hand
        self.is_stand = False
    
    def hit(self):
        self.deck, self.hand = dk.deal(self.deck, self.hand)
    
    def stand(self):
        self.is_stand = True
    
    def choice(self):
        if self.is_stand:
            self.stand()
        else:
            self.hit_or_stand()
    
    def hit_or_stand(self):
        raise NotImplementedError
    
    def is_blackjack(self):
        return hd.is_blackjack(self.hand)
    
    def is_busted(self):
        return hd.is_busted(self.hand)


class Player(AbstractPlayer):
    def hit_or_stand(self):
        print('hit or stand?')
        if 'h' in input():
            self.hit()
        else:
            self.stand()


class Dealer(AbstractPlayer):
    def hit_or_stand(self):
        if hd.sum_of(self.hand) < 17:
            self.hit()
        else:
            self.stand()
