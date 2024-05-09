import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if get := re.findall(r"\b[\W]?um\b[\W]?", s, re.IGNORECASE):
        return len(get)
    else:
        return 0


if __name__ == "__main__":
    main()
