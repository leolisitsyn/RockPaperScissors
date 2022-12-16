from Players import You, ConstantPlayer, SmartOpponent


class Game():
    def __init__(self, player, opponent, turns):

        player.clear_moves()
        opponent.clear_moves()

        self.player = player
        self.opponent = opponent

        self.score = [0, 0, 0]
        self.turns = turns
        self.turn = 0
        self.dictionary = {0: 'rock', 1: 'scissors', 2: 'paper'}

    def change_score(self, move_1, move_2):
        if move_1 == move_2:
            self.score[1] += 1
        else:
            if move_1 == 0:
                if move_2 == 1:
                    self.score[0] += 1
                else:
                    self.score[2] += 1
            elif move_1 == 1:
                if move_2 == 0:
                    self.score[2] += 1
                else:
                    self.score[0] += 1
            elif move_1 == 2:
                if move_2 == 0:
                    self.score[0] += 1
                else:
                    self.score[2] += 1

    def who_won(self):
        score_string = '-'.join([str(num) for num in self.score])
        if self.turn < self.turns:
            print(f'current score is: {score_string}')
        else:
            print(f'final score is: {score_string}')
            if self.score[0] > self.score[2]:
                print('First player won')
            elif self.score[0] < self.score[2]:
                print('Second player won')
            else:
                print('Draw')

    def game_turn(self):
        move_1 = self.player.move()
        move_2 = self.opponent.move()
        print(f'{self.dictionary[move_1]} - {self.dictionary[move_2]}')
        self.change_score(move_1, move_2)
        self.who_won()

    def play_game(self):
        while self.turn < self.turns:
            self.turn += 1
            self.game_turn()


if __name__ == '__main__':
    turns = 100

    from sklearn.linear_model import LinearRegression

    model = LinearRegression()  # an example

    you = ConstantPlayer(0)
    smart = SmartOpponent(you, model)

    game = Game(you, smart, turns)
    game.play_game()
