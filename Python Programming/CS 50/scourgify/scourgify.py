import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    try:
        with open(sys.argv[1], newline="") as file:
            row = csv.reader(file)
            t = next(row)
            t.insert(0, "first")
            t[1] = "last"
            with open(sys.argv[2], "w") as input:
                get = csv.writer(input)
                get.writerow(t)
                for i in row:
                    a = change(i[0])
                    p = [a[1], a[0], i[1]]
                    get.writerow(p)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def change(a):
    l = a.split(",")
    l[0] = l[0].strip()
    l[1] = l[1].strip()
    return l


if __name__ == "__main__":
    main()
