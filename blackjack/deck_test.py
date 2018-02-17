import blackjack.deck as dk


def test_generating_deck():
    deck = dk.generate_deck()
    assert len(deck) == 52
    assert [c.number for c in deck].count(1) == 4