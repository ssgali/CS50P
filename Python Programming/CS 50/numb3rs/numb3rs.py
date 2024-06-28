import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ips := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        for i in ips.groups():
            get = check(int(i))
            if get == False:
                return False
    else:
        return False
    return True


def check(p):
    if 0 <= p < 256:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
