import random

def main():
    while True:
        try:
            level = int(input("Level: "))
            break
        except ValueError:
            pass
    if 101 > level < 1:
        return main()

    winner = random.randint(1, level)
    the_game(winner, level)

def the_game(winner, level):
    while True:
        try:
            guess = int(input("Guess: "))

            if guess == winner:
                print("Just right!")
                break
            elif guess > winner:
                print("Too large!")
            elif guess < winner:
                print("Too small!")

        except ValueError:
            pass

if __name__ == "__main__":
    main()