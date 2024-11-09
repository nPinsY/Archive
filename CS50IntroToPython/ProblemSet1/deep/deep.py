# Def main
def main():
    meaning(input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").casefold().strip())

# Def meaning
def meaning(a):
    match a:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

# Call Main
main()