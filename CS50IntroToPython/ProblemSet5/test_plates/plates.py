# Def main
def main():
    plate = input("Plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Def is_valid
def is_valid(plate):
    return first_two_and_max_character(plate)  and number(plate) and punctuation(plate)

# Def first_two_and_max_character
def first_two_and_max_character(plate):
    num = len(plate)
    if 2 < num < 7:
        first_two = plate[:2]
        return first_two.isalpha()
    else:
        return False

def number(plate):
    index = 0
    first_number = None
    end = ""
    for i in plate:
        if i.isdigit():
            end = plate[index:]
            first_number = end[0]
            break
        index += 1

    if first_number == "0":
        return False
    else:
        return all(i.isdigit() for i in end)

def punctuation(plate):
    return plate.isalnum()

if __name__ == "__main__":
    main()