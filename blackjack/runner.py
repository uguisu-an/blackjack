from blackjack.dispatcher import dispatcher
import blackjack.actions as actions


class GameRunner:
    def __init__(self):
        self._game_is_over = False
        self._turn_is_over = False
        self._dispatcher = dispatcher
        self._dispatcher.on(actions.CHANGE_STATE, self.update)

    def run(self):
        self._dispatcher.dispatch(actions.BEGIN_GAME)
        while not self._game_is_over:
            self._dispatcher.dispatch(actions.BEGIN_TURN)
            self._dispatcher.dispatch(actions.TURN_PLAYER)
            if not self._turn_is_over:
                self._dispatcher.dispatch(actions.TURN_DEALER)
            self._dispatcher.dispatch(actions.END_TURN)
        self._dispatcher.dispatch(actions.END_GAME)
        self._dispatcher.dispatch(actions.SHOW_RESULT)
    
    def update(self, state={}):
        self._game_is_over = state.game_is_over
        self._turn_is_over = state.turn_is_over