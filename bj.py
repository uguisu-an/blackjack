import random
#TODO: actionsにまとめる
from blackjack.dispatcher import dispatcher
from blackjack.game_store import GameStore
from blackjack.game_component import GameComponent
from blackjack.player_component import PlayerComponent
from blackjack.dealer_component import DealerComponent

from blackjack.deck import Deck
from blackjack.player import Dealer, Player


class App:
    def __init__(self):
        self._deck = Deck()
        self._dealer = Dealer(self._deck, [])
        self._player = Player(self._deck, [])
        #TODO: 中で初期化してもいい
        self._store = GameStore(self._deck, self._dealer, self._player)
        self._components = [
            GameComponent(),
            PlayerComponent(),
            DealerComponent(),
        ]
        self.update(self._store.get_state())
    
    def update(self, game):
        self._game = game
        for component in self._components:
            component.update(game)
    
    #TODO: ゲームの流れは誰が持つべきか？
    def run(self):
        dispatcher.dispatch('BEGIN_GAME')
        while not self._store.get_state()['game_is_over']:
            dispatcher.dispatch('BEGIN_TURN')
            dispatcher.dispatch('TURN_PLAYER')
            if not self._store.get_state()['turn_is_over']:
                dispatcher.dispatch('TURN_DEALER')
            dispatcher.dispatch('END_TURN')
        dispatcher.dispatch('END_GAME')


if __name__ == '__main__':
    app = App()
    app.run()