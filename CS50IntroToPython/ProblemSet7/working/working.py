import re

def main():
    print(match(input("Hours: ").upper().strip()))

def match(s):
    pattern = r"^(\d[0-2]?):?([0-5]?\d?) (AM|PM) TO (\d[0-2]?):?([0-5]?\d?) (AM|PM)$"
    if matches := re.fullmatch(pattern, s):
        from_time = convert(matches.group(1), matches.group(2), matches.group(3))
        to_time = convert(matches.group(4), matches.group(5), matches.group(6))
    else:
        raise ValueError

    return f"{from_time} to {to_time}"

def convert(hours, min, zone):
    if min == "":
        min = "00"

    if zone == "AM":
        if hours == "12":
            hours = "00"
        if len(hours) == 1:
            hours = f"0{hours}"
    else:
        if int(hours) in range(1, 11):
            hours = str(int(hours) + 12)

    return f"{hours}:{min}"

if __name__ == "__main__":
    main()