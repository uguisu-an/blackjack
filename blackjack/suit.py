class Suit:
    def __init__(self, design):
        self.design = design
    
    def __str__(self):
        return self.design


Spade = Suit('♠︎')
Club = Suit('♣︎')
Diamond = Suit('♢')
Heart = Suit('♡')
All = [Spade, Club, Diamond, Heart]


