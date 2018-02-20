class Hit:
    def change(self, player):
        card = player.deck.pop(0)
        player.hand.append(card)
    
    def frozen(self):
        return False


class Stand:
    def change(self, player):
        pass
    
    def frozen(self):
        return True


HIT = Hit()
STAND = Stand()