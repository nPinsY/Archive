# Def main
def main():
    fraction = input("Fraction: ").strip()

    try:
        percentage = convert(fraction)
        print(gauge(percentage))

    except (ValueError, ZeroDivisionError):
        main()

def convert(fraction):
    x, y = map(int, fraction.split("/"))

    if x > y:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    return int(round((x / y) * 100))

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()