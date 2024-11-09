from PIL import Image, ImageOps
import sys

file_type = ["jpeg", "png", "jpg"]

if len(sys.argv) == 3:
    background = sys.argv[1]
    output = sys.argv[2]
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")

file_type1 = background.split('.')[-1].lower()
file_type2 = output.split('.')[-1].lower()
if file_type1 != file_type2:
    sys.exit("File type dont match")
if file_type1 not in file_type:
    sys.exit("File type unrecognized")

def main():
    background = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")

    photo = ImageOps.fit(background, shirt.size)
    photo.paste(shirt, mask=shirt)

    photo.save(sys.argv[2])

if __name__ == "__main__":
    main()