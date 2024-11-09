import re

def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        set1, set2, set3, set4 = [int(x) for x in matches.groups()]
        if all(0 <= x <= 255 for x in [set1, set2, set3, set4]):
            return True
        else:
            return False
    return False

if __name__ == "__main__":
    main()