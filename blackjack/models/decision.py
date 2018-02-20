class Hit:
    def change(self, player):
        card = player.deck.pop(0)
        player.hand.append(card)
    
    def did_stand(self):
        return False


class Stand:
    def change(self, player):
        pass
    
    def did_stand(self):
        return True


HIT = Hit()
STAND = Stand()