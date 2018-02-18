import blackjack.models.deck as dk
import blackjack.models.hand as hd


class Player:
    def __init__(self, name='no name', deck=[], hand=[]):
        self.name = name
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
