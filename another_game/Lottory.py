from Game import Game
import random
import colorama
from colorama import Style
colorama.init()

class Lottory(Game):
    def __init__(self, name):
        super().__init__(name)

# this function give you the first 5 numbers
    def winning_num(self):
        white_ball = []
        for i in range(0, 5):
            num = random.randint(1, 20)
            while num in white_ball:
                num = random.randint(1, 20)
            white_ball.append(num)
        b = sorted(white_ball, reverse=False)
        return b

    def player_num(self):
        white_ball = []
        for i in range(0, 5):
            num = random.randint(1, 20)
            while num in white_ball:
                num = random.randint(1, 20)
            white_ball.append(num)
        B = sorted(white_ball, reverse=False)
        return B

# this function give you the last number (powerball)
    def powerBall(self):
        powerball = 0
        for i in range(1):
            powerball = random.randint(1, 10)
        return powerball


# function that print in color
    def color(self,a, b):
        print(colorama.Fore.MAGENTA, a, colorama.Fore.YELLOW, b, Style.RESET_ALL)





    #
    # def __str__(self):
    #     a = str(self.winning_num())
    #     b = str(self.powerBall())
    #     c = str(self.player_num())
    #     d = str(self.powerBall())
    #     return a+" "+b +"\n"+c+" "+d



