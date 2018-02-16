class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    
    def __eq__(self, other):
        return (
            self.suit == other.suit
            and self.number == other.number
        )
    
    def __lt__(self, other):
        self.number < other.number
    
    def __gt__(self, other):
        self.number > other.number
    