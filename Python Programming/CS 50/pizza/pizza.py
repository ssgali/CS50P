import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif False == (".csv" in sys.argv[1]):
        sys.exit("Not a CSV file")
    try:
        with open(sys.argv[1]) as file:
            row = csv.DictReader(file)
            for p in row:
                list_header = get_header(p)
                break
        with open(sys.argv[1], newline="") as file:
            read = csv.DictReader(file)
            list_1 = []
            for row in read:
                list_1.append(row.values())

            print(tabulate(list_1, headers=list_header, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


def get_header(row):
    list_2 = []
    for i in row:
        z = i
        list_2.append(z)
    return list_2


if __name__ == "__main__":
    main()
