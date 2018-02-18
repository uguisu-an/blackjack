import blackjack.models.result as rs

  
def test_judge_from_point():
    assert rs.judge_from_point(20, 21) == rs.WIN
    assert rs.judge_from_point(21, 20) == rs.LOSE
    assert rs.judge_from_point(21, 21) == rs.DRAW

def test_judge_from_point_with_bust():
    assert rs.judge_from_point(20, 22) == rs.LOSE
    assert rs.judge_from_point(22, 20) == rs.WIN
    # 両者bustはシステム上ありえない
    # assert rs.judge_from_point(22, 22) == ?
