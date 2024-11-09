# Def main
def main():
    x, y, z = input("Expression: ").strip().split(" ")
    x, z = int(x), int(z)
    a = symbol(x, y, z)
    print(a)

# Def Symbol
def symbol(x, y, z):
    if y == "+":
        return float(x + z)
    elif y == "-":
        return float(x - z)
    elif y == "*":
        return float(x * z)
    elif y == "/":
        return float(x / z)
    else:
        return "ERROR"

# Call main
main()