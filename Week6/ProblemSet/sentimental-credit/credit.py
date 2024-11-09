import re


def main():
    pattern = r"^\d+$"
    cc = input("Number: ").strip()

    if not re.fullmatch(pattern, cc):
        print("INVALID\n")
        return

    length = len(cc)

    if checksum(cc, length):
        categorize(cc, length)
    else:
        print("INVALID\n")


def checksum(card, length):
    sum = 0
    card_number = [int(digit) for digit in card]

    for i in range(length):
        if (length - i) % 2 == 0:
            doubled = card_number[i] * 2
            sum += doubled // 10 + doubled % 10
        else:
            sum += card_number[i]

    return sum % 10 == 0


def categorize(card, length):
    first_digit = int(card[0])
    first_two_digits = int(card[:2])

    if (length == 13 or length == 16) and first_digit == 4:
        print("VISA\n")
    elif length == 15 and (first_two_digits == 34 or first_two_digits == 37):
        print("AMEX\n")
    elif length == 16 and 51 <= first_two_digits <= 55:
        print("MASTERCARD\n")
    else:
        print("INVALID\n")


if __name__ == "__main__":
    main()
