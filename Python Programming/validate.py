import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    for i in range(0,256):
        print(validate(str(i)))

def validate(ip):
    if re.search(r"",ip):
        return True
    else:
        print(ip)
        return False


...


if __name__ == "__main__":
    main()