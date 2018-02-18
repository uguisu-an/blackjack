import blackjack.models.result as result
import blackjack.actions as actions
from blackjack.dispatcher import dispatcher


class GameComponent:
    def __init__(self):
        self._game_result = None
        self._dispatcher = dispatcher
        self._dispatcher.on(actions.CHANGE_STATE, self.update)
        self._dispatcher.on(actions.SHOW_RESULT, self._show_result)
    
    def update(self, state={}):
        self._game_result = state['game_result']
    
    def _show_result(self):
        print(self._get_result_message())
    
    #TODO: ロジックに移す
    def _get_result_message(self):
        if self._game_result == result.WIN:
            return 'You Win!'
        if self._game_result == result.LOSE:
            return 'You Lose...'
        return 'Draw'