def main():
    money = value(input("Greeting: "))
    print(f"${money}")

def value(greeting):

    adjusted = greeting.lower().strip()

    if adjusted.startswith("hello"):
        return 0
    elif adjusted[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()