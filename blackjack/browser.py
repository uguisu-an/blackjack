import blackjack.result as res
import blackjack.hand as hand

class SimpleBrowser:
    def show_result(self, result):
        if result == res.WIN:
            print('You Win!')
            return
        if result == res.LOSE:
            print('You Lose...')
            return
        print('Draw')
    
    def show_state(self, dealer, player, hole=1):
        print('Dealer:')
        self.show_hand(dealer, hole=hole)
        print()
        print('Player:')
        self.show_hand(player, hole=0)
        print()

    def show_hand(self, hand_, hole=1):
        for c in hand_:
            if hole:
                print('* hole *')
                hole -= 1
                continue
            print(c.suit, c.number, '({})'.format(hand.point(c.number)))


    