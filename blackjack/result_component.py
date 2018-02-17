import blackjack.result as rs


class ResultComponent:
    def __init__(self, dispatcher):
        if dispatcher:
            dispatcher.on('GAMEOVER', self.render)

    def render(self, result=None):
        assert result is not None
        print(self.result_message(result))
    
    def result_message(self, result):
        if result == rs.WIN:
            return 'You Win!'
        if result == rs.LOSE:
            return 'You Lose...'
        return 'Draw'