import random

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass

def main():
    level = get_level()
    correct_answers = 0

    for _ in range(10):
        x, y = generate_integer(level)
        attempts = 0

        while attempts < 3:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == x + y:
                    correct_answers += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")

            attempts += 1

        if attempts == 3:
            print(f"Answer: {x + y}")

    print(f"Score: {correct_answers/10}")

if __name__ == "__main__":
    main()