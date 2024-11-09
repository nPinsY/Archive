vowels = [
    "A", "E", "I", "O", "U", "a", "e", "i", "o", "u"
]

def main():
    final_name = shorten(input("Input: ").strip())
    print(f"Output: {final_name}")

def shorten(x_name):
    output = ""

    for i in x_name:
        if i not in vowels:
            output += i

    return output

if __name__ == "__main__":
    main()