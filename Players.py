import numpy as np

from MovePredictor import Predictor


class Player():
    """Abstract player"""

    def __init__(self):
        self.moves = []

    def move(self, *args):
        pass

    def clear_moves(self):
        self.moves = []


class You(Player):
    """Player under your control"""

    def __init__(self):
        super().__init__()

    def move(self):
        print("Please make your move:")
        step = int(input("0 - rock, 1 - scissors, 2 - paper"))
        self.moves.append(step)
        return step


class YouPredefined(Player):
    """First player with a list of pre-chosen moves"""

    def __init__(self, choice_list: list[int]):
        super().__init__()
        self.step_n = 0
        self.choice_list = choice_list

    def move(self):
        step = self.choice_list[self.step_n]
        self.step_n += 1
        self.moves.append(step)
        return step


class RandomPlayer(Player):
    """Player making completely random moves"""

    def __init__(self):
        super().__init__()

    def move(self):
        step = np.random.randint(0, 3)
        self.moves.append(step)
        return step


class AlmostRandomPlayer(Player):
    """Player making moves with predefined probabilities"""

    def __init__(self, probabilities_of_move: list):
        """probabilities of moves: list of int, for example [33, 33, 33]"""
        super().__init__()
        self.num_list = [0 for _ in range(probabilities_of_move[0])] + \
                        [1 for _ in range(probabilities_of_move[1])] + \
                        [2 for _ in range(probabilities_of_move[2])]

    def move(self):
        choice = np.random.choice(self.num_list)
        self.moves.append(choice)
        return choice


class ConstantPlayer(Player):
    """Player making exactly the same move all the time"""

    def __init__(self, number: int):
        super().__init__()
        self.number = number

    def move(self):
        self.moves.append(self.number)
        return self.number


class SlidingPlayer(Player):
    """Player making moves in order: Rock-Paper-Scissors-Rock..."""

    def __init__(self, start_num: int):
        super().__init__()
        self.num = start_num - 1

    def move(self):
        self.num = (self.num + 1) % 3
        self.moves.append(self.num)
        return self.num


class QuadSlidingPlayer(Player):
    def __init__(self, start_num: int):
        super().__init__()
        self.num = start_num
        self.turn = 0
        self.round = 1
        self.length = self.round ** 2

    def move(self):
        if self.length > self.turn:
            self.turn += 1
        else:
            self.turn = 1
            self.round += 1
            self.length = self.round ** 2
            self.num = (self.num + 1) % 3

        self.moves.append(self.num)
        return self.num


class SmartOpponent(Player):
    """Player learning opponent's game stile"""
    def __init__(self, player, model):
        super().__init__()

        self.opponent = player
        self.predictor = Predictor(player, self, model)

    def move(self):
        if len(self.opponent.moves) < 3:
            step = np.random.randint(0, 3)
        else:
            step = self.predictor.fit_predict()

        self.moves.append(step)
        return step

    def change_opponent(self, new_opponent):
        self.opponent = new_opponent