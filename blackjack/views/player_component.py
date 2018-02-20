from blackjack.dispatcher import dispatcher
import blackjack.models.point as pt
import blackjack.models.decision as dc
import blackjack.action as act

class PlayerComponent:
    """プレイヤーの情報を表示する."""
    
    def __init__(self):
        self._player = None
        self._dispatcher = dispatcher
        self._dispatcher.on(act.CHANGE_STATE, self.update)
        self._dispatcher.on(act.BEGIN_TURN, self._show_state)
        self._dispatcher.on(act.TURN_PLAYER, self._turn_player)
        self._dispatcher.on(act.END_GAME, self._show_state)
    
    def update(self, state={}):
        self._player = state.player
    
    def _turn_player(self):
        while True:
            print('Hit or Stand?')
            decision = input()
            if decision.startswith('h'):
                self._dispatcher.dispatch(act.HIT_OR_STAND,
                    player=self._player, decision=dc.HIT)
                break
            if decision.startswith('s'):
                self._dispatcher.dispatch(act.HIT_OR_STAND,
                    player=self._player, decision=dc.STAND)
                break
            print('Use h[it] or s[tand].')
    
    def _show_state(self):
        self._show_name()
        self._show_hand()
        print()
    
    def _show_name(self):
        print('{} ({}):'.format(self._player.name, self._player.point))

    def _show_hand(self):
        for card in self._player.hand:
            print('{} ({})'.format(card, pt.point(card.number)))
    