from blackjack.dispatcher import dispatcher
from blackjack.models.game import Game
import blackjack.actions as actions


class GameStore:
    def __init__(self):
        self._game = Game()
        self._dispatcher = dispatcher
        self._dispatcher.on(actions.BEGIN_GAME, self._begin_game)
        self._dispatcher.on(actions.TURN_DEALER, self._turn_dealer)
        self._dispatcher.on(actions.HIT_OR_STAND, self._hit_or_stand)

    def get_state(self):
        return self._game
    
    def _begin_game(self):
        self._game.begin()
        self._dispatcher.dispatch(actions.CHANGE_STATE, state=self.get_state())
    
    #TODO: BEGIN_TURNで決定してTURN_PLAYERで変更してもいいかも
    def _hit_or_stand(self, player=None, decision=None):
        if decision == 'hit':
            player.hit()
        else:
            player.stand()
        self._dispatcher.dispatch(actions.CHANGE_STATE, state=self.get_state())
    
    #TODO: 決定する処理はdealerに持たせる？
    def _turn_dealer(self):
        if self._game.dealer.point < 17:
            self._game.dealer.hit()
        else:
            self._game.dealer.stand()
        self._dispatcher.dispatch(actions.CHANGE_STATE, state=self.get_state())
