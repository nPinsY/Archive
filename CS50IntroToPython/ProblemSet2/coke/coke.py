# Def main
def main():
    print("Amount Due: 50")
    calc()

# Def calc
def calc():
    coins = [5, 10, 25]
    due = 50

    while due > 0:
        m = int(input("Insert Coin: "))
        if m in coins:
            due = due - m
            if due <= 0:
                change(due)
            else:
                print("Amount Due:", due)

        elif m not in coins:
            print("Amount Due:", due)

# Def change
def change(i):
    if i == 0:
        print("Change Owed: 0")

    elif i < 0:
        c = 0 - i
        print("Change Owed:", c)


# Call main
main()