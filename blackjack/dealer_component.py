from blackjack.dispatcher import dispatcher


class DealerComponent:
    def __init__(self):
        self._dealer = None
        self._dispatcher = dispatcher
        self._dispatcher.on('END_GAME', self._end_game)
        self._dispatcher.on('CHANGE_STATE', self._change_state)

    def update(self, game):
        dealer = game['dealer']
        if self._dealer:
            updated = len(dealer.hand) != len(self._dealer.hand)
        else:
            updated = False
        self._dealer = dealer
        return updated
    
    def _change_state(self, game):
        if self.update(game):
            print('{}: Hit'.format(self._dealer.name))
        else:
            print('{}: Stand'.format(self._dealer.name))
    
    def _end_game(self):
        print(self._dealer.name)
        print(self._dealer.point)
        print(self._dealer.hand)