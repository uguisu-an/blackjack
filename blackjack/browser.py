import blackjack.result as res
import blackjack.hand as hd
import blackjack.point as pt


class SimpleBrowser:
    def show_result(self, result):
        print(self.result_message(result))
    
    def result_message(self, result):
        # if result == res.BLACKJACK:
        #     return 'Blackjack!!'
        if result == res.WIN:
            return 'You Win!'
        if result == res.LOSE:
            return 'You Lose...'
        return 'Draw'
    
    def show_state(self, dealer, player, hole=True):
        if hole:
            print('Dealer:')
        else:
            print('Dealer ({}):'.format(dealer.point))
        self.show_hand(dealer.hand, hole=hole)
        print()
        print('Player ({}):'.format(player.point))
        self.show_hand(player.hand, hole=False)
        print()

    def show_hand(self, hand, hole=True):
        if not hand:
            return
        if hole:
            print('* hole card *')
        else:
            print('{} ({})'.format(hand[0], pt.point(hand[0].number)))
        self.show_hand(hand[1:], False)
