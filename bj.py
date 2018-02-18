import random
#TODO: actionsにまとめる
from blackjack.dispatcher import dispatcher
from blackjack.game_store import GameStore
from blackjack.game_runner import GameRunner
from blackjack.game_component import GameComponent
from blackjack.player_component import PlayerComponent
from blackjack.dealer_component import DealerComponent

from blackjack.deck import Deck
from blackjack.player import Dealer, Player


class App:
    def __init__(self, store):
        self._store = store
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
    

if __name__ == '__main__':
    deck = Deck()
    dealer = Dealer(deck, [])
    player = Player(deck, [])
    store = GameStore(deck, dealer, player)
    app = App(store)
    app.run()