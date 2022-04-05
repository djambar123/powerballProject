from player import player
from powerBall import powerBall
from whiteBalls import whiteBalls
from score import score

class main():
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
