import blackjack.models.deck as dk


def test_generating_deck():
    deck = dk.generate_deck()
    assert len(deck) == 52
    assert [c.number for c in deck].count(1) == 4

def test_dealing_card():
    deck = dk.generate_deck()
    top_of_deck = deck[0]
    deck, hand = dk.deal(deck, [])
    assert len(deck) == 51
    assert top_of_deck in hand
