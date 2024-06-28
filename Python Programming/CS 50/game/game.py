from random import randint
import sys

while True:
    try:
        x = int(input("Level: "))
        if x < 0:
            continue
        y = randint(1, int(x))
        while True:
            try:
                g = int(input("Guess: "))
                if g > y:
                    print("Too large!")
                    continue
                elif g < y:
                    print("Too small!")
                    continue
                sys.exit("Just right!")
            except ValueError:
                continue
    except ValueError:
        continue
