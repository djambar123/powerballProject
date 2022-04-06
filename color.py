import colorama
from colorama import Style
colorama.init()
# A function that colors the numbers in different colors
def color(a,b):
    print(colorama.Fore.MAGENTA,a,colorama.Fore.YELLOW,b,Style.RESET_ALL)
