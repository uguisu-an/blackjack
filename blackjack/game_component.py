from blackjack.dispatcher import dispatcher


class GameComponent:
    def __init__(self):
        self._dispatcher = dispatcher
        self._dispatcher.on('BEGIN_GAME', self._begin_game)
        self._dispatcher.on('END_GAME', self._end_game)
    
    def update(self, state):
        pass
    
    def _begin_game(self):
        print('Begin the Game.')
    
    def _end_game(self):
        print('End the Game.')