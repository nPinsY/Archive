# Def main
def main():
    convert(input("camelCase: ").strip())

# Def convert
def convert(camelCase):

    snake_case = ""

    for i in camelCase:
        if i.isupper():
            snake_case += "_"
        snake_case += i

    print("snake_case:", snake_case.lower())

# Call main
main()