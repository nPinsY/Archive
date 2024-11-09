from pyfiglet import Figlet
import sys
import random

font_start = ["-f", "--font"]

figlet = Figlet()

if len(sys.argv) > 3:
    sys.exit()
elif len(sys.argv) == 3:
    start = sys.argv[1]
    font_choice = sys.argv[2]

    if start in font_start:
        if font_choice in figlet.getFonts():
            figlet.setFont(font=font_choice)
        else:
            sys.exit()
elif len(sys.argv) == 2:
    sys.exit()
else:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)

def main():
    text = input("Input: ")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()