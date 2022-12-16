import telebot

from Players import Player, SmartOpponent
from Game import Game


class TeleYou(Player):
    def __init__(self, bot):
        super().__init__()

    def move(self, inp):
        step = int(inp)
        self.moves.append(step)
        return step


class TeleGame(Game):
    def __init__(self, player, opponent, turns):
        super().__init__(player, opponent, turns)
        self.message_id = None
        self.bot = bot

    def game_turn(self, inp: int, chat_id):
        self.message_id = chat_id

        move_1 = self.player.move(inp)
        move_2 = self.opponent.move()
        self.bot.send_message(self.message_id, f'{self.dictionary[move_1]} - {self.dictionary[move_2]}')
        self.change_score(move_1, move_2)
        self.who_won()

    def who_won(self):
        score_string = '-'.join([str(num) for num in self.score])
        if self.turn < self.turns:
            self.bot.send_message(self.message_id, f'current score is: {score_string}')
        else:
            self.bot.send_message(self.message_id, f'final score is: {score_string}')
            if self.score[0] > self.score[2]:
                self.bot.send_message(self.message_id, 'First player won')
            elif self.score[0] < self.score[2]:
                self.bot.send_message(self.message_id, 'Second player won')
            else:
                self.bot.send_message(self.message_id, 'Draw')


if __name__ == '__main__':

    from sklearn.linear_model import LinearRegression

    model = LinearRegression()  # an example

    bot = telebot.TeleBot('Bot token from BotFather')

    you = TeleYou(bot)
    opponent = SmartOpponent(you, model)
    game = TeleGame(you, opponent, 20)


    @bot.message_handler(commands=['0', '1', '2', 'rock', 'paper', 'scissors', 'start'])
    def start_command(message):
        chat_id = message.chat.id
        if message.text == '/start':
            bot.send_message(chat_id, "Hello. Let's start the game")
            bot.send_message(chat_id, "0 - rock, 1 - paper, 2 - scissors")
            game.score = [0, 0, 0]

        elif message.text == "/0" or message.text == "/rock":
            game.game_turn(0, chat_id)
        elif message.text == "/1" or message.text == "/paper":
            game.game_turn(1, chat_id)
        elif message.text == "/2" or message.text == "/scissors":
            game.game_turn(2, chat_id)


    bot.polling()
