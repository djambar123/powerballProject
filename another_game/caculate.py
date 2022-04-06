from Lottory import *


class Caculate(Lottory):
    def __init__(self, a):
        super().__init__(self)
        self.com = Lottory.winning_num(self)
        self.com_p = Lottory.powerBall(self)
        self.color(self.com,self.com_p)
        self.player = Lottory.player_num(self)
        self.player_p = Lottory.powerBall(self)
        self.color(self.player,self.player_p)
        count = 0  # counter for the matches between the two lists
        count2 = 0  # counter for the matches power balls
        for i in self.com:
            for j in self.player:
                if i == j:
                    count += 1
        if self.com_p == self.player_p:
            count2 += 1
            print("*%*you got the power number*%*")
        resu = count + count2
        print("you have **", resu, "** number correct")
        if count == 5 and count2 == 1:
            print("#*#*#*#**#*#*#")
            print("Jackpot $324,000,000")
        elif count == 5 and count2 == 0:
            print("#*#*#*#**#*#*#")
            print("You just won $1,000,000 ")
        elif count == 4 and count2 == 1:
            print("#*#*#*#**#*#*#")
            print("You win $10,000 ")
        elif count == 4 and count2 == 0:
            print("#*#*#*#**#*#*#")
            print("You win $100 ")
        elif count == 3 and count2 == 1:
            print("#*#*#*#**#*#*#")
            print("You win $100 ")
        elif count == 3 and count2 == 0:
            print("#*#*#*#**#*#*#")
            print("You win $7 ")
        elif count == 2 and count2 == 1:
            print("#*#*#*#**#*#*#")
            print("You win $7 ")
        elif count == 1 and count2 == 1:
            print("#*#*#*#**#*#*#")
            print("You win $4 ")
        elif count == 0 and count2 == 1:
            print("#*#*#*#**#*#*#")
            print("You win $4 ")
        else:
            print("Better luck next time !")


