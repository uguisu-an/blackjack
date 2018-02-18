from blackjack.dispatcher import dispatcher
import blackjack.models.point as pt
import blackjack.actions as actions


class DealerComponent:
    def __init__(self):
        self._dealer = None
        self._dispatcher = dispatcher
        self._dispatcher.on(actions.CHANGE_STATE, self.update)
        self._dispatcher.on(actions.BEGIN_TURN, self._begin_turn)
        self._dispatcher.on(actions.END_GAME, self._end_game)

    def update(self, state={}):
        self._dealer = state.dealer

    def _begin_turn(self):
        self._show_name(hole=True)
        self._show_hand(hole=True)
        print()
    
    def _end_game(self):
        self._show_name(hole=False)
        self._show_hand(hole=False)
        print()
    
    def _show_name(self, hole):
        if hole:
            print('{} (*):'.format(self._dealer.name))
        else:
            print('{} ({}):'.format(self._dealer.name, self._dealer.point))

    def _show_hand(self, hole):
        for card in self._dealer.hand:
            if hole:
                print('* hole card *')
                hole = False
                continue
            print('{} ({})'.format(card, pt.point(card.number)))
    