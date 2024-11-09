import requests
import sys

try:
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
date = response.json()
rate_float = float(date["bpi"]["USD"]["rate_float"])

def main():
    amount = rate_float * bitcoin
    print(f"${amount:,.4f}")

if __name__ == "__main__":
    main()