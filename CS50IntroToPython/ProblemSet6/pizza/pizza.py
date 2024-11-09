import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 2:
    file_name = sys.argv[1]
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")

rows = []

def main():
    if file_name[-4:] != ".csv":
        sys.exit("Not a CSV file")

    try:
        with open(f"{file_name}", "r") as file:
            pizza_menu = csv.DictReader(file)
            for row in pizza_menu:
                rows.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(rows, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()