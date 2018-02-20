from blackjack.models.game import Game
from blackjack.models.point import point
import blackjack.models.result as result
import blackjack.models.decision as dc


def run():
    game = Game()
    game.begin()
    while not game.game_is_over:
        show_state(game, hole=True)
        turn_player(game)
        if game.turn_is_over:
            break
        turn_dealer(game)
    show_state(game, hole=False)
    show_result(game)

def turn_dealer(game):
    if game.dealer.point < 17:
        game.dealer.hit()
    else:
        game.dealer.stand()

def turn_player(game):
    game.player.decide(_ask_hit_or_stand())
    game.player.hit_or_stand()

def show_state(game, hole):
    _show_name(game.player, hole=False)
    _show_hand(game.player, hole=False)
    _show_name(game.dealer, hole=hole)
    _show_hand(game.dealer, hole=hole)

def show_result(game):
    print(_get_result_message(game.game_result))

def _show_name(player, hole):
    if hole:
        print('{} (*):'.format(player.name))
    else:
        print('{} ({}):'.format(player.name, player.point))

def _show_hand(player, hole):
    for card in player.hand:
        if hole:
            print('* hole card *')
            hole = False
        else:
            print('{} ({})'.format(card, point(card.number)))
    
def _get_result_message(result_):
    if result_ == result.WIN:
        return 'You Win!'
    if result_ == result.LOSE:
        return 'You Lose...'
    return 'Draw'

def _ask_hit_or_stand():
    while True:
        print('Hit or Stand?')
        decision = input()
        if decision.startswith('h'):
            return dc.HIT
        if decision.startswith('s'):
            return dc.STAND
        print('Use h[it] or s[tand].')