# Def main
def main():
    x, y = get_fraction()
    calculate(x, y)

# Def get_fraction
def get_fraction():
    while True:
        try:
            x, y = map(int, input("Fraction: ").strip().split("/"))
            return x, y
        except ValueError:
            pass

# Def calculate
def calculate(x, y):

    if x > y:
        get_fraction()
        return calculate(x, y)

    try:
        p = round((x / y) * 100)
    except ZeroDivisionError:
        get_fraction()
        return calculate(x, y)

    if 2 <= p <= 98:
        print(f"{p}%")
    elif p >= 99:
        print("F")
    elif p <= 1:
        print("E")

# Call main
main()