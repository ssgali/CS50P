def main():
        # Getting input
        x = input("Greetings: ")
        # Processing
        print("$",value(x.strip()),sep = "")

# Checking The condition using "in"
def value(y):
    y = y.casefold()
    if "h" in y:
        if "hello" in y:
            return 0
        elif y.startswith("h"):
            return 20
        else:
            return 100
    else:
        return 100
if __name__ == "__main__":
    main()