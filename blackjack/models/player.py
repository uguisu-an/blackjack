from blackjack.models.point import Point
import blackjack.models.decision as decision_


class Player:
    """プレイヤーの情報を持つ."""

    def __init__(self, name='no name', deck=[], hand=[]):
        self.name = name
        self.deck = deck
        self.hand = hand
        self._decision = decision_.HIT
    
    @property
    def point(self):
        return Point(self._numbers)
    
    @property
    def _numbers(self):
        return [c.number for c in self.hand]
    
    def frozen(self):
        return self._decision.frozen()
    
    def decide(self, decision):
        self._decision = decision
    
    def run(self):
        self._decision.change(self)

    def hit(self):
        self.decide(decision_.HIT)
        self.run()
    
    def stand(self):
        self.decide(decision_.STAND)
        self.run()

    