from blackjack.dispatcher import dispatcher


def hit():
    dispatcher.dispatch('PLAYER_HIT')

def stand():
    dispatcher.dispatch('PLAYER_STAND')

def ask_hit_or_stand():
    dispatcher.dispatch('ASK_HIT_OR_STAND')

def show_hand():
    dispatcher.dispatch('SHOW_HAND')

def game_over(result):
    dispatcher.dispatch('GAMEOVER', result=result)