
class score():
    def score(com_balls, player_num, com_power, player_power):
        count = 0
        count2 = 0
        for i in com_balls:
            for j in player_num:
                if i == j:
                    count += 1
        if com_power == player_power:
            count2 += 1
            print("you got the power number")
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















