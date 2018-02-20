from tramp import Heart
from blackjack.models.game import Game
from blackjack.models.card import Card
from blackjack.models.result import WIN, LOSE


def test_initial_game_properties():
    game = Game()
    assert game.game_result is None
    assert not game.game_is_over
    assert not game.turn_is_over

def test_beginning_of_the_game():
    game = Game()
    deck_before_shuffle = game.deck[:]
    game.begin()
    assert game.deck != deck_before_shuffle
    assert len(game.dealer.hand) == 2
    assert len(game.player.hand) == 2

def test_game_after_player_standing():
    game = Game()
    game.player.stand()
    assert game.game_result is not None 
    assert game.game_is_over
    assert not game.turn_is_over

def test_game_after_blackjack():
    game = Game()
    game.player.hand = [Card(Heart, 1), Card(Heart, 13)]
    assert game.game_result == WIN
    assert game.game_is_over
    assert game.turn_is_over
    game.player.hand.append(Card(Heart, 1))
    assert game.game_result == LOSE
    assert game.game_is_over
    assert game.turn_is_over
