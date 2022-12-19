import numpy as np


class Predictor():
    def __init__(self, player, opponent, model):
        self.player = player
        self.opponent = opponent
        self.model = model

    def process_moves(self):
        """creates matrix of players' moves X and matrix of winning response from second player"""
        pl_moves = self.player.moves.copy()

        ddict = {0: 2, 1: 0, 2: 1}
        y = [ddict[x] for x in pl_moves]
        return y

    def fit_predict(self):
        y = self.process_moves()
        if len(set(y))  <= 1:
            return y[0]
        else:
            move_nums = np.array(range(len(y))).reshape((-1, 1))

            self.model.fit(move_nums, y)
            pred = self.model.predict(np.array(len(y), ndmin=2))

            return int(pred)
