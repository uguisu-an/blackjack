import tramp


class Card(tramp.Card):
    def point(self):
        if self.number == 0:
            return (1, 11)
        if self.number > 9:
            return (10, 10)
        return (self.number, self.number)
    