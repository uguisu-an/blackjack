import tramp
import blackjack.models.point as pt


class Card(tramp.Card):
    @property
    def point(self):
        return pt.point(self.number)