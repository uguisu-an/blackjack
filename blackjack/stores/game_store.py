import random
import blackjack.models.result as result
from blackjack import Deck, Dealer, Player
from blackjack.dispatcher import dispatcher
import blackjack.actions as actions


class GameStore:
    def __init__(self):
        self._deck = Deck()
        self._dealer = Dealer(self._deck, [])
        self._player = Player(self._deck, [])
        self._game_result = None
        self._game_is_over = False
        self._turn_is_over = False
        self._dispatcher = dispatcher
        self._dispatcher.on(actions.BEGIN_GAME, self._begin_game)
        self._dispatcher.on(actions.TURN_DEALER, self._turn_dealer)
        self._dispatcher.on(actions.HIT_OR_STAND, self._hit_or_stand)

    def get_state(self):
        #TODO: namedtupleでもいい
        #TODO: Gameでもいい
        return {
            'deck': self._deck,
            'dealer': self._dealer,
            'player': self._player,
            'game_result': self._game_result,
            'game_is_over': self._game_is_over,
            'turn_is_over': self._turn_is_over,
        }
    
    def _begin_game(self):
        #TODO: Gameに任せてもいい
        random.shuffle(self._deck)
        for _ in range(2):
            self._player.hit()
            self._dealer.hit()
        self._set_result()
        self._dispatcher.dispatch(actions.CHANGE_STATE, state=self.get_state())
    
    #TODO: BEGIN_TURNで決定してTURN_PLAYERで変更してもいいかも
    def _hit_or_stand(self, player=None, decision=None):
        if decision == 'hit':
            player.hit()
        else:
            player.stand()
        self._set_result()
        self._dispatcher.dispatch(actions.CHANGE_STATE, state=self.get_state())
    
    #TODO: 決定する処理はdealerに持たせる？
    def _turn_dealer(self):
        if self._dealer.point < 17:
            self._dealer.hit()
        else:
            self._dealer.stand()
        self._set_result()
        self._dispatcher.dispatch(actions.CHANGE_STATE, state=self.get_state())

    #TODO: Gameに任せてもいい
    def _set_result(self):
        self._turn_is_over = (
            self._dealer.point >= 21
            or self._player.point >= 21
        )
        self._game_is_over = (
            self._player.is_stand()
            or self._turn_is_over
        )
        if not self._game_is_over:
            return
        self._game_result = result.judge_from_point(
            self._dealer.point,
            self._player.point
        )
    