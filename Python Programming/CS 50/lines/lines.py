import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif False == (".py" in sys.argv[1]):
        sys.exit("Not a Python file")
    try:
        z = 0
        with open(sys.argv[1]) as file:
            for row in file:
                l = row.strip()
                if l.startswith("#") or row.isspace():
                    continue
                z = z + 1
            print(z)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
