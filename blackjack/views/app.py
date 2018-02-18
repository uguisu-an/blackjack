from blackjack.views import GameComponent, PlayerComponent, DealerComponent
from blackjack.stores import GameStore
from blackjack.runner import GameRunner


class App:
    def __init__(self):
        self._store = GameStore()
        self._runner = GameRunner()
        self._components = [
            GameComponent(),
            PlayerComponent(),
            DealerComponent(),
        ]
        self.update(self._store.get_state())
    
    def update(self, state):
        self._state = state
        for component in self._components:
            component.update(self._state)
    
    def run(self):
        self._runner.run()


def run():
    App().run()