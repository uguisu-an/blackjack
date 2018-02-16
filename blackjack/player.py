from blackjack.hand import Hand


class Player:
    def __init__(self, deck, hand=Hand()):
        self.deck = deck
        self.hand = hand
        self._is_stand = False

    def hit(self):
        self.hand = self.deck.deal(self.hand)

    def stand(self):
        self._is_stand = True
    
    def is_stand(self):
        return self._is_stand
    
    def is_blackjack(self):
        return self.hand.is_blackjack()

    def is_busted(self):
        return self.hand.is_busted()
