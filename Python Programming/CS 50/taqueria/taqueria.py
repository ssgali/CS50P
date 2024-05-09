def main():
    y = int(0)
    while(True):
        try:
            x = input("Item: ")
            y = float(y + display(x))
        except EOFError:
            print()
            return 0
        except (ValueError,KeyError,TypeError):
            continue
        print(f"${y:.2f}")
def display(y):
    y = y.casefold().title()
    if(y in dict):
        return float(dict[y])
    else:
        return "0"





















dict = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
main()
