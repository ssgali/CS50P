def main():
    x = check()
    if(x >= 99):
        print("F")
    elif(x <= 1):
        print("E")
    else:
        print(f"{x}%")
def check():
    while(True):
        try:
            y = input("Fraction: ")
            y = y.rsplit("/")
            y[0] = int(y[0])
            y[1] = int(y[1])
            z = float(y[0]/y[1]*100)
            if(y[0] > y[1]):
                continue
            return round(z)

        except (ValueError, ZeroDivisionError):
            continue
main()
