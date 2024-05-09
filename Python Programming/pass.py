import sys


def main():
    verification()


def verification():
    for _ in range(3):
        with open("my.txt") as file2:
            try:
                x = int(input("Enter PIN :"))
                for p in file2:
                    if x == int(p):
                        sys.exit("Found")
                print("Not Found")
            except ValueError:
                print("Not Found")
                continue


if __name__ == "__main__":
    main()
