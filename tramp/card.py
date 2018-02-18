class Card:
    """カードの情報を持つ."""
    
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    
    def __repr__(self):
        return '<Card {}>'.format(self)
    
    def __str__(self):
        return '{} {}'.format(self.suit, self.number)
    
    def __eq__(self, other):
        return (
            self.suit == other.suit
            and self.number == other.number
        )
    
    def __lt__(self, other):
        return self.number < other.number
    
    def __gt__(self, other):
        return self.number > other.number
