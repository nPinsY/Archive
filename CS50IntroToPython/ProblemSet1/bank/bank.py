# Def Main
def main():
    greeting(input("Insert Greeting - " ).casefold().strip())

# Def Greeting
def greeting(g):
    Valid_H = ("hi", "howdy", "how are you?", "how's it going", "how goes it",
        "hail", "hi-ya", "howdy-do", "howdy do", "hats off", "hoorays", "high-fives",
        "high fives", "how do you do", "how's life", "how's your day", "how's everything",
        "how've you been", "hey there", "heya", "hi there", "how's it hanging", "heyo",
        "hola", "hullo", "how are things", "how are you doing", "how are you keeping",
        "how are you feeling", "hows it going", "how are you doing?","how are you", "how you doing?")

    if "hello" in g:
        print("$0")
    elif g in Valid_H:
        print("$20")
    else:
        print("$100")

# Main
main()