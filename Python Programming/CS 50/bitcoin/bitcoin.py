import requests
import json
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        sys.argv[1] = float(sys.argv[1])
    except ValueError:
        sys.exit("Missing command-line argument")
    y = get_value(float(sys.argv[1]))
    print(f"${y:,.4f}")


def get_value(y):
    while True:
        try:
            file = requests.get(
                "https://api.coindesk.com/v1/bpi/currentprice.json"
            ).json()
            for name in file["bpi"]:
                if name == "USD":
                    return y * file["bpi"]["USD"]["rate_float"]
        except requests.RequestException:
            continue


main()
