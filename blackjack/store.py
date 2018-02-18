from blackjack.dispatcher import dispatcher


class Store:
    def __init__(self, reducer):
        self._dispatcher = dispatcher
        self._reducer = reducer
        self._state = self._reducer(action={'topic': None})
    
    def get_state(self):
        return self._state
    
    def update(self, action):
        self._state = self._reducer(self._state, action)
        self._dispatcher.dispatch('CHANGE_STATE', state=self.get_state())
    