from pyfiglet import Figlet

figlet = Figlet()
y = figlet.getFonts()
import random
import sys


def main():
    if len(sys.argv) == 1:          #Default Case
        default()

    elif len(sys.argv) == 3:        #User's Choice
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":      #Checking Command lines
            if sys.argv[2] in y:
                convert()

    sys.exit("Invalid usage")       #if wrong command lines


def convert():
    j = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print("Output: \n", figlet.renderText(j))
    sys.exit()


def default():
    j = input("Input: ")
    figlet.setFont(font=random.choice(y))
    print("Output: \n", figlet.renderText(j))
    sys.exit()


main()
