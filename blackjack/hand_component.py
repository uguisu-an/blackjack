import blackjack.point as pt


# TODO: 実装上のアレでprintベタ書き
class HandComponent:
    def __init__(self, dispatcher=None, player=None, hole=True):
        if dispatcher:
            dispatcher.on('SHOW_HAND', self.render)
            dispatcher.on('GAMEOVER', self.render)
        self.player = player
        self.hole = hole

    def render(self, result=None):
        print(
            self._render_name(self.player, self.hole) +
            self._render_hand(self.player.hand, self.hole)
        )
    
    def _render_name(self, player, hole):
        if hole:
            return '{} (*):\n'.format(player.name)
        else:
            return '{} ({}):\n'.format(player.name, player.point)
    
    def _render_hand(self, hand, hole):
        if not hand:
            return ''
        if hole:
            return '* hole card *\n' + self._render_hand(hand[1:], False)
        else:
            return '{} ({})\n'.format(hand[0], pt.point(hand[0].number)) + self._render_hand(hand[1:], False)