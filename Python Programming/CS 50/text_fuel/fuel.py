def main():
    while True:
        try:
            y = input("Fraction: ")
            x = convert(y)
            if x >= 0:
                break
        except (ValueError, ZeroDivisionError):
            continue
    print(gauge(x))


def convert(y):
    y = y.rsplit("/")
    try:
        y[0] = int(y[0])
        y[1] = int(y[1])
    except (ValueError, IndexError):
        raise ValueError
    z = float(y[0] / y[1] * 100)
    if y[0] > y[1]:
        raise ValueError
    if y[1] == 0:
        raise ZeroDivisionError
    return round(z)


def gauge(x):
    if x >= 99:
        return "F"
    elif x <= 1:
        return "E"
    else:
        return f"{x}%"


if __name__ == "__main__":
    main()
