from blackjack.dispatcher import dispatcher
import blackjack.action as act


class GameRunner:
    """ゲームを進行する."""
    
    def __init__(self):
        self._game_is_over = False
        self._turn_is_over = False
        self._dispatcher = dispatcher
        self._dispatcher.on(act.CHANGE_STATE, self.update)

    def run(self):
        self._dispatcher.dispatch(act.BEGIN_GAME)
        while not self._game_is_over:
            self._dispatcher.dispatch(act.BEGIN_TURN)
            self._dispatcher.dispatch(act.TURN_PLAYER)
            if not self._turn_is_over:
                self._dispatcher.dispatch(act.TURN_DEALER)
            self._dispatcher.dispatch(act.END_TURN)
        self._dispatcher.dispatch(act.END_GAME)
        self._dispatcher.dispatch(act.SHOW_RESULT)
    
    def update(self, state={}):
        self._game_is_over = state.game_is_over
        self._turn_is_over = state.turn_is_over