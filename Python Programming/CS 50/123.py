import datetime
import re
import sys
import inflect

def main():
    l= check(input("Date of Birth: ").strip())
    try:
        datetime.date(int(l[0]),int(l[1]),int(l[2])) < datetime.date.today()
        print(inflect.engine().number_to_words(int(datetime.timedelta.total_seconds(abs(datetime.date.today()-datetime.date(int(l[0]),int(l[1]),int(l[2]))))/60), andword="").capitalize(),"minutes")
    except ValueError:
        sys.exit("Invalid date")
def check(age):
    if time := re.search(r"^\d\d?\d?\d?-(\d?\d)-(\d?\d)$", age):
        return age.split("-")
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
