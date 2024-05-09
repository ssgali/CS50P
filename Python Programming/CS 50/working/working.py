import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...
    if get := re.search(
        r"(\d*(?::[012345]\d)? (?:AM|PM)) to (\d*(?::[012345]\d)? (?:AM|PM))", s
    ):
        z = split(get.group(1))
        q = split(get.group(2))
        return f"{z} to {q}"
    else:
        raise ValueError


...


def split(z):
    k = 12
    if "12" in z:
        k = 0
    if "PM" in z and ":" in z:
        z = z.replace("PM", "")
        t, r = z.split(":")
        return f"{(k + int(t)):02}:{r.strip()}"
    elif "PM" in z:
        z = z.replace("PM", "")
        z = f"{(int(z.strip()) + k):02}:00"
        return z
    elif "AM" in z and ":" in z:
        z = z.replace("AM", "")
        t, r = z.split(":")
        if int(t) == 12:
            t = 00
        return f"{int(t):02}:{r.strip()}"
    elif "AM" in z:
        z = z.replace("AM", "")
        z = int(z.strip())
        if z == 12:
            z = 00
        return f"{z:02}:00"


if __name__ == "__main__":
    main()
