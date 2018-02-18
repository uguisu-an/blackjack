import random
from blackjack.dispatcher import dispatcher


class GameStore:
    def __init__(self, deck, dealer, player):
        #TODO: 隠す
        self.deck = deck
        self.dealer = dealer
        self.player = player
        dispatcher.on('BEGIN_GAME', self._begin_game)
        dispatcher.on('TURN_DEALER', self._turn_dealer)
        dispatcher.on('HIT_OR_STAND', self._hit_or_stand)

    def get_state(self):
        #TODO: namedtupleでもいい
        return {
            'deck': self.deck,
            'dealer': self.dealer,
            'player': self.player,
        }
    
    def _begin_game(self):
        random.shuffle(self.deck)
        for _ in range(2):
            self.player.hit()
            self.dealer.hit()
    
    def _hit_or_stand(self, player=None, decision=None):
        if decision == 'hit':
            player.hit()
        else:
            player.stand()
    
    def _turn_dealer(self):
        self.dealer.hit()   #FAKE IT