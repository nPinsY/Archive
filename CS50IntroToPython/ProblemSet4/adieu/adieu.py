import inflect

p = inflect.engine()

names = [

]

def main():
    while True:
        try:
            name = input("Names: ").strip().title()
        except EOFError:
            print("Adieu, adieu, to", p.join(names))
            break

        names.append(name)

if __name__ == "__main__":
    main()