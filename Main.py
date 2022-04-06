from player import player
from powerBall import powerBall
from whiteBalls import whiteBalls
from score import score
from color import color

class main():
    print("WELLCOME TO THE POWERBALL GAME")
    a = input("Would you like to try your luck?(y - to play/n - to exit):\n")
    c = 0 # Stop the game loop if you do not want to play again
    while c < 1:
        if a == "y":
            com_power = powerBall.powerBall()
            com_balls = whiteBalls.winning_num()
            print("the winning numbers are :")
            color(com_balls,com_power)
            player_num = player.player_num()
            player_power = powerBall.powerBall()
            print("your numbers are :")
            color(player_num,player_power)
            print ("###############")
            res =  score.score(com_balls,player_num,com_power,player_power)
            c+=1
            tryAgain = input("do you want to try again?(y - to play/any key to exit):\n")
            if tryAgain == 'y':
                c = 0
            else:
                print("bey nigga")
        elif a == 'n':
            print("chicken")
        else:
            print("invalid input ")
            a = input("you need to put(y - to play/n - to exit):\n")



