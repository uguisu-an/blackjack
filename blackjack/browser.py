import blackjack.result as res
import blackjack.hand as hd
import blackjack.point as pt


class SimpleBrowser:
    def show_result(self, result):
        print(self.result_message(result))
    
    def result_message(self, result):
        if result == res.BLACKJACK:
            return 'Blackjack!!'
        if result == res.WIN:
            return 'You Win!'
        if result == res.LOSE:
            return 'You Lose...'
        return 'Draw'
    
    def show_state(self, dealer, player, hole=True):
        if hole:
            print('Dealer:')
        else:
            print('Dealer ({}):'.format(hd.sum_of(dealer.hand)))
        self.show_hand(dealer.hand, hole=hole)
        print()
        print('Player ({}):'.format(hd.sum_of(player.hand)))
        self.show_hand(player.hand, hole=False)
        print()

    def show_hand(self, hand, hole=True):
        for c in hand:
            if hole:
                print('* hole *')
                hole = False
                continue
            print('{} ({})'.format(c, pt.point(c.number)))
