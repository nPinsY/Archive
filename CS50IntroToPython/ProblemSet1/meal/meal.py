# Def Function
def main():
    t = input("What time is it? ")
    t = convert(t)

    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time):
    h, min = time.split(":")
    h, min = float(h), float(min)
    return h + min / 60


if __name__ == "__main__":
    main()