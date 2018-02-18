from blackjack.dispatcher import dispatcher
import blackjack.models.point as pt


class PlayerComponent:
    def __init__(self):
        self._player = None
        self._dispatcher = dispatcher
        self._dispatcher.on('CHANGE_STATE', self.update)
        self._dispatcher.on('BEGIN_TURN', self._begin_turn)
        self._dispatcher.on('TURN_PLAYER', self._turn_player)
        self._dispatcher.on('END_GAME', self._end_game)
    
    def update(self, state={}):
        self._player = state.player
    
    def _begin_turn(self):
        self._show_name()
        self._show_hand()
        print()
    
    #TODO: beginと統合する？
    def _end_game(self):
        self._show_name()
        self._show_hand()
        print()

    def _turn_player(self):
        while True:
            print('Hit or Stand?')
            decision = input()
            if decision.startswith('h'):
                self._dispatcher.dispatch('HIT_OR_STAND',
                    player=self._player, decision='hit')
                break
            if decision.startswith('s'):
                self._dispatcher.dispatch('HIT_OR_STAND',
                    player=self._player, decision='stand')
                break
            print('Use h[it] or s[tand].')
    
    def _show_name(self):
        print('{} ({}):'.format(self._player.name, self._player.point))

    def _show_hand(self, hole=True):
        for card in self._player.hand:
            print('{} ({})'.format(card, pt.point(card.number)))
    