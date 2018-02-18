import random
from blackjack.dispatcher import dispatcher


class GameStore:
    def __init__(self, deck, dealer, player):
        #TODO: 隠す
        self.deck = deck
        self.dealer = dealer
        self.player = player
        self.game_is_over = False
        self.turn_is_over = False
        dispatcher.on('BEGIN_GAME', self._begin_game)
        dispatcher.on('TURN_DEALER', self._turn_dealer)
        dispatcher.on('HIT_OR_STAND', self._hit_or_stand)

    def get_state(self):
        #TODO: namedtupleでもいい
        #TODO: Gameでもいい
        return {
            'deck': self.deck,
            'dealer': self.dealer,
            'player': self.player,
            'game_is_over': self.game_is_over,
            'turn_is_over': self.turn_is_over,
        }
    
    def _begin_game(self):
        #TODO: Gameに任せてもいい
        random.shuffle(self.deck)
        for _ in range(2):
            self.player.hit()
            self.dealer.hit()
        self._set_result()
    
    def _hit_or_stand(self, player=None, decision=None):
        if decision == 'hit':
            player.hit()
        else:
            player.stand()
        self._set_result()
    
    #TODO: 決定する処理はdealerに持たせる？
    def _turn_dealer(self):
        if self.dealer.point < 17:
            self.dealer.hit()
        else:
            self.dealer.stand()
        self._set_result()

    #TODO: Gameに任せてもいい
    def _set_result(self):
        self.turn_is_over = (
            self.dealer.point >= 21
            or self.player.point >= 21
        )
        self.game_is_over = (
            self.player.is_stand()
            or self.turn_is_over
        )
    