import datetime
import re
import sys
from inflect import engine


def main():
    age = input("Date of Birth: ").strip()
    l = check(age)
    try:
        Date = datetime.date(int(l[0]), int(l[1]), int(l[2]))
    except ValueError:
        sys.exit("Invalid date")
    Date < datetime.date.today()
    x = abs(datetime.date.today() - Date)
    y = int(datetime.timedelta.total_seconds(x) / 60)
    y = engine().number_to_words(y, andword="")
    print(y.capitalize(), "minutes")


def check(age):
    if time := re.search(r"^\d\d?\d?\d?-(\d?\d)-(\d?\d)$", age):
        return age.split("-")
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
