def main():
    x = int(50)
    while(True):
        print("Amount Due:", x)
        y = int(input("Insert Coin: "))         #Getting User Input
        if y in [5,10,25]:                      #Checking The Accepted Denomination
            if y >=x:
                print("Change Owed:", y-x)      #Last print
                break
            else:                               #Itterating again with decreased Amount Due
                x = x - y
                continue
        else:
            continue

main()