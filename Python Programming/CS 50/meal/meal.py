def main():

    #Getting Input

    x = input("What time is it? ")

    x = convert(x)

    #Checking Time

    if (7 <= x <= 8):
        print("breakfast time")
    elif (12 <= x <= 13):
        print("lunch time")
    elif (18 <= x <= 19):
        print("dinner time")
 # Converting Function
def convert(time):

    x,y = time.split(":")
    y = float(y)
    x = float(x)
    x = x + (y/60)
    return x


if __name__ == "__main__":
    main()