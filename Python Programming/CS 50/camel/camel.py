def main():
    #Getting Input
    x = input("camelCase: ")
    if (0 == x.islower()):
        convert(x)
    else:
        print("snake_case:", x)
def convert(y):
    print("snake_case:", end = "")
    for c in y:
        if c.islower():
            print(c, sep = "", end = "")#Print by character changes each character in each itteration
        else:
            c = c.swapcase()
            print("_",c, sep = "", end = "")
    print()
main()
