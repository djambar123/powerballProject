from player import player
from powerBall import powerBall
from whiteBalls import whiteBalls
from score import score

class main():
    print("WELLCOME TO THE POWERBALL GAME")
    a = input("Would you like to try your luck?(y - to play/n - to exit):\n")
    c = 0
    while c < 1:
        if a == "y":
            com_power = powerBall.powerBall()
            com_balls = whiteBalls.winning_num()
            numbers = (com_balls,com_power)
            print("the winning numbers are :\n",numbers)
            player_num = player.player_num()
            player_power = powerBall.powerBall()
            ball_player = (player_num,player_power)
            print("your numbers are :\n",ball_player)
            print ("###############")
            res =  score.score(com_balls,player_num,com_power,player_power)
            c+=1
            tryAgain = input("do you want to try again?(y - to play/n - to exit):\n")
            if tryAgain == 'y':
                c = 0
            else:
                print("beyy nigga")
        elif a == 'n':
            print("chicken")
        else:
            print("invalid input ")
            a = input("you need to put(y - to play/n - to exit):\n")



