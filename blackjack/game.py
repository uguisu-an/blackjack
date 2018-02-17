import random
import blackjack.result as result
import blackjack.actions as actions


# Stateを管理するGameStoreにするべきかも
# どこまでをロジックにするか
class Game:
    def __init__(self, deck, dealer, player):
        self.deck = deck
        self.dealer = dealer
        self.player = player
    
    def begin(self):
        random.shuffle(self.deck)
        for _ in range(2):
            self.player.hit()
            self.dealer.hit()
        
    def turn(self):
        actions.show_hand()
        # TODO: actionを経由する
        self.player.hit_or_stand()
        if self._should_end():
            return
        # TODO: actionを経由する
        self.dealer.hit_or_stand()
    
    def end(self):
        res = result.judge_from_point(self.dealer.point, self.player.point)
        actions.game_over(res)
    
    def _should_end(self):
        return (
            self.dealer.point >= result.BLACKJACK
            or self.player.point >= result.BLACKJACK
        )

    def is_over(self):
        return (
            self.player.is_stand()
            or self._should_end()
        )
    