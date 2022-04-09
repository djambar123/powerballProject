from Caculate import Caculate


print("**WELLCOME TO THE POWER BALL GAME**")
print("------------------------------------\n")
play = input("Would you like to try your luck!?(y - to play/ n - to exit\n ")
c = 0
while c < 1: # function to run the progrem
    if play == 'y':
        Caculate("daniel")
        play = input("Would you like to try again?(y - to play/ any key - to exit\n ")
    elif play == 'n':
        print("Bey Nigga\n Thanks for the money")
        c+=1
    else:
        print("Stupid!! only use (y/n) ")
        play = input("Would you like to try ?(y - to play/ n - to exit ")



