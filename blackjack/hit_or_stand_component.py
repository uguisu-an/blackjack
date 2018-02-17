from blackjack.actions import hit, stand


# TODO: 実装上のアレでprintベタ書き
class HitOrStandComponent:
    def __init__(self, dispatcher=None):
        if dispatcher:
            dispatcher.on('ASK_HIT_OR_STAND', self.render)

    def render(self):
        print('Hit or Stand?')
        hit_or_stand = input()
        if hit_or_stand == 'h':
            return hit()
        if hit_or_stand == 's':
            return stand()
        print('Input Error: input h or s.')
        self.render()

        # 本当はこういう風にしたい
        # プレースホルダーに入力されたらイベントが発火されるとか
        # return (
        #     'Hit or Stand?\n'
        #     '> {hit_or_stand}'
        # )

