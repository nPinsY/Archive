# List
my_list = {

}

# Def main
def main():
    while True:
        try:
            item = input("").strip().upper()
        except EOFError:
            print("")
            for item, count in sorted(my_list.items()):
                print(f"{count} {item}")
            break

        if item in my_list:
            my_list[item] += 1

        else:
            my_list[item] = 1

# Call main
main()