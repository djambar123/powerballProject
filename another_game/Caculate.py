from Lottory import *

# function that check if the the two raws has the same numbers and print accordenly
class Caculate(Lottory):
    def __init__(self, name):
        super().__init__(self)
        self.com = Lottory.winning_num(self) #the first 5 numbers of the computer
        self.com_p = Lottory.powerBall(self) # power ball of the computer
        print(colorama.Fore.LIGHTBLUE_EX,"The winning numbers are:")
        self.color(self.com,self.com_p) # print the computer numbers
        print(colorama.Fore.BLUE,"********************")
        self.player = Lottory.player_num(self) #the first 5 numbers of the player
        self.player_p = Lottory.powerBall(self)# power ball of the player
        print(colorama.Fore.LIGHTBLUE_EX,"Your numbers are:")
        self.color(self.player,self.player_p)# print the player numbers
        print(colorama.Fore.BLUE,"#####################",Style.RESET_ALL)
        count = 0  # counter for the matches between the two lists
        count2 = 0  # counter for the matches power balls
        for i in self.com:
            for j in self.player:
                if i == j:
                    count += 1
        if self.com_p == self.player_p:
            count2 += 1
            print(colorama.Fore.LIGHTGREEN_EX,"*%*you got the power number*%*",Style.RESET_ALL)
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


