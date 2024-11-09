import cs50


def main():
    height = 0

    while height < 1 or height > 8:
        height = cs50.get_int("Height: ")

    print(build(height))


def build(h):
    pyramid = ""

    for i in range(1, h + 1):
        spaces = " " * (h - i)
        hashes = "#" * i
        pyramid += f"{spaces}{hashes}  {hashes}\n"

    if pyramid:
        pyramid = pyramid.rstrip("\n")

    return pyramid


if __name__ == "__main__":
    main()
