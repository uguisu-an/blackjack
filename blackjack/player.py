import blackjack.hand as hd


class Player:
    def __init__(self, deck, hand):
        self.deck = deck
        self.hand = hand

    def hit(self):
        self.hand = self.deck.deal(self.hand)

    def stand(self):
        return 

    def is_blackjack(self):
        return hd.is_blackjack(self.hand)

    def is_busted(self):
        return hd.is_busted(self.hand)
