import sys

if len(sys.argv) == 2:
    file_name = sys.argv[1]
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")

def main():
    if file_name[-3:] != ".py":
        sys.exit("Not a Python file")
    try:
        with open(f"{file_name}", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    lines_of_code = counter(lines)
    print(f"{lines_of_code}")


def counter(lines):
    no_line = 0
    yes_line = 0

    for row in lines:
        if row.strip().startswith("#"):
            no_line += 1
        elif row.strip() == "":
            no_line += 1
        else:
            yes_line +=1

    return yes_line

if __name__ == "__main__":
    main()