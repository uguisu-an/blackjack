import blackjack.point as pt


class HandComponent:
    def __init__(self, player, hole=True):
        self.player = player
        self.hole = hole

    def render(self):
        return (
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