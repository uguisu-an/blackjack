import blackjack.deck as dk
import blackjack.hand as hd


class AbstractPlayer:
    def __init__(self, deck=[], hand=[]):
        self.deck = deck
        self.hand = hand
        self._is_stand = False
    
    def hit(self):
        card = self.deck.pop(0)
        self.hand.append(card)
    
    def stand(self):
        self._is_stand = True
    
    def hit_or_stand(self):
        if self.is_stand():
            self.stand()
        else:
            self.choice()
    
    def choice(self):
        raise NotImplementedError
    
    def is_stand(self):
        return self._is_stand
    
    def is_blackjack(self):
        return hd.is_blackjack(self.hand)
    
    def is_busted(self):
        return hd.is_busted(self.hand)
    
    @property
    def point(self):
        return hd.sum_of(self.hand)


class Player(AbstractPlayer):
    name = 'Player'

    def choice(self):
        print('hit or stand?')
        if 'h' in input():
            self.hit()
        else:
            self.stand()


class Dealer(AbstractPlayer):
    name = 'Dealer'

    def choice(self):
        if hd.sum_of(self.hand) < 17:
            self.hit()
        else:
            self.stand()
