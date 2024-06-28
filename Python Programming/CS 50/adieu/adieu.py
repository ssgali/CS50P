import sys
import inflect

p = inflect.engine()


def main():
    list = []
    while True:
        try:
            list.append(input("Name: "))        #Appending list at each itterations

        except EOFError:
            paste(list)
            sys.exit()


def paste(y):
    print("\nAdieu, adieu, to " + p.join(y, final_sep=",")) #Prinitng the List


main()
