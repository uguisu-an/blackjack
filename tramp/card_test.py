from tramp import Card, Heart, Spade


def testCardComparison():
    h5 = Card(Heart, 5)
    assert h5 == Card(Heart, 5)
    assert h5 != Card(Spade, 5)
    assert h5 > Card(Spade, 4)
    assert h5 < Card(Spade, 6)
