import numpy as np


class Predictor():
    def __init__(self, player, opponent, model):
        self.player = player
        self.opponent = opponent
        self.model = model

    def process_moves(self):
        """creates matrix of players' moves X and matrix of winning response from second player"""
        pl_moves = self.player.moves.copy()

        length = len(pl_moves)

        X = np.zeros((length, 3))
        y = np.zeros((length - 1, 3))

        for i in range(length):
            X[i][pl_moves[i]] = 1

        for i in range(length - 1):
            if pl_moves[i] == 0:
                y[i][2] = 1
            elif pl_moves[i] == 1:
                y[i][0] = 1
            else:
                y[i][1] = 1
        return X, y

    def fit_predict(self):
        X, y = self.process_moves()

        self.model.fit(X[:-1], y)
        pred = self.model.predict([X[:-1]])

        return np.argmax(pred)
