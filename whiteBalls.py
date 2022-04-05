import random

class whiteBalls():
    def winning_num():
        white_ball = []
        for i in range(0, 5):
            num = random.randint(1, 20)
            while num in white_ball:
                num = random.randint(1, 20)
            white_ball.append(num)
        b = sorted(white_ball, reverse=False)
        return b

print(whiteBalls.winning_num())