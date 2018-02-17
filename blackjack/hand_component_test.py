from tramp import Card, Diamond, Heart
from blackjack.player import Dealer, Player
from blackjack.hand_component import HandComponent


def test_hand_component_with_hole_card():
    hand = [Card(Diamond, 13), Card(Heart, 1)]
    dealer = Dealer(hand=hand)
    com = HandComponent(dealer, hole=True)
    expected = """
Dealer (*):
* hole card *
♡ 1 (1)
    """
    assert com.render().strip() == expected.strip()

def test_hand_component_without_hole_card():
    hand = [Card(Diamond, 13), Card(Heart, 1)]
    player = Player(hand=hand)
    com = HandComponent(player, hole=False)
    expected = """
Player (21):
♢ 13 (10)
♡ 1 (1)
    """
    assert com.render().strip() == expected.strip()