l = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]  # List of Vowels(Global)


def main():
    x = input("Input: ")
    for c in x:
        if c in l:
            print("Output:", shorten(x))  # Calling FUnction
            return 1
    print("Output2:", x)  # Original Output


def shorten(y):
    for c in y:
        if c in l:  # Checking Vowels
            y = y.replace(c, "")  # Removing Vowels
    return y

if __name__ == "__main__":
    main()
