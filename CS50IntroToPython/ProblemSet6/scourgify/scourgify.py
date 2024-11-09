import sys
import csv

if len(sys.argv) == 3:
    file_name = sys.argv[1]
    new_file = sys.argv[2]
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")

if new_file[-4:] != ".csv":
    sys.exit("Second argument not a CSV")

def main():
    try:
        with open(f"{file_name}") as file:
            name_home = csv.DictReader(file)

            with open(new_file, "w", newline="") as new_list:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(new_list, fieldnames=fieldnames)
                writer.writeheader()

                for row in name_home:
                    house = row.get("house")
                    name = row.get("name")
                    last, first = name.split(", ")

                    writer.writerow({"first": first, "last": last, "house": house})

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()