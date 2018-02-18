from blackjack.dispatcher import dispatcher


class GameRunner:
    def __init__(self):
        self._game_is_over = False
        self._turn_is_over = False
        self._dispatcher = dispatcher
        self._dispatcher.on('CHANGE_STATE', self.update)

    def run(self):
        self._dispatcher.dispatch('BEGIN_GAME')
        while not self._game_is_over:
            self._dispatcher.dispatch('BEGIN_TURN')
            self._dispatcher.dispatch('TURN_PLAYER')
            if not self._turn_is_over:
                self._dispatcher.dispatch('TURN_DEALER')
            self._dispatcher.dispatch('END_TURN')
        self._dispatcher.dispatch('END_GAME')
        self._dispatcher.dispatch('SHOW_RESULT')
    
    def update(self, state={}):
        self._game_is_over = state['game_is_over']
        self._turn_is_over = state['turn_is_over']