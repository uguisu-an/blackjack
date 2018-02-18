from blackjack.dispatcher import dispatcher


class PlayerComponent:
    def __init__(self):
        self._player = None
        self._dispatcher = dispatcher
        self._dispatcher.on('BEGIN_TURN', self._begin_turn)
        self._dispatcher.on('TURN_PLAYER', self._turn_player)
        self._dispatcher.on('END_GAME', self._end_game)
        self._dispatcher.on('CHANGE_STATE', self._change_state)
    
    def update(self, game):
        player = game['player']
        if self._player:
            updated = len(player.hand) != len(self._player.hand)
        else:
            updated = False
        self._player = player
        return updated
    
    def _begin_turn(self):
        print(self._player.name, self._player.point)
        print(self._player.hand)
    
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
    
    def _change_state(self, state={}):
        if self.update(state):
            print('{}: Hit'.format(self._player.name))
        else:
            print('{}: Stand'.format(self._player.name))
    
    def _end_game(self):
        print(self._player.name)
        print(self._player.point)
        print(self._player.hand)
