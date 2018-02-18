import blackjack.models.deck as dk
import blackjack.models.hand as hd


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
    
    def is_stand(self):
        return self._is_stand
    
    @property
    def point(self):
        return hd.point(self.hand)


class Player(AbstractPlayer):
    name = 'Player'


class Dealer(AbstractPlayer):
    name = 'Dealer'
