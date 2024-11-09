from datetime import date
import inflect
import sys
import operator

_in = inflect.engine()

def main():
    try:
        input_date = input("Date of Birth: ")
        difference = operator.sub(date.today(), date.fromisoformat(input_date))
        print(convert(difference.days))
    except ValueError:
        sys.exit("Invalid date")

def convert(time):
    minutes = time * 24 * 60
    return f"{(_in.number_to_words(minutes, andword='')).capitalize()} minutes"

if __name__ == "__main__":
    main()