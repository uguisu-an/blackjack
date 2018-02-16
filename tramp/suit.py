class Suit:
    def __init__(self, design):
        self._design = design
    
    def __str__(self):
        return self._design


class JokerSuit:
    def __str__(self):
        return ''


Joker = JokerSuit()
Spade = Suit('♠︎')
Club = Suit('♣︎')
Diamond = Suit('♢')
Heart = Suit('♡')
All = [Spade, Club, Diamond, Heart]
