import sys
import random


def main():
    z = get_level()
    p = 0
    m = 0
    for _ in range(10):
        X = generate_integer(z)
        Y = generate_integer(z)
        for _ in range(3):
            print(X, "+", Y, "= ", end="")
            try:
                a = int(input())
            except ValueError:
                print("EEE")
                continue
            if X + Y == int(a):
                p += 1
                break
            print("EEE")
        if m == p:
            print(X, "+", Y, "=", X + Y)
        else:
            m = p

    print("Score:", p)


def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if (x < 1) or (3 < x):
                raise ValueError
            return x
        except ValueError:
            continue


def generate_integer(x):
    if x == 1:
        return random.randint(0, 9)
    if x == 2:
        return random.randint(10, 99)
    if x == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
