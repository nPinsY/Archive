def main():
    input_sentence = input("Text: ").strip()
    letters = count_letters(input_sentence)
    words = count_words(input_sentence)
    sentence = count_sentence(input_sentence)

    average_words = float(letters / words) * 100
    average_sentences = float(sentence / words) * 100
    grade = round(0.0588 * average_words - 0.296 * average_sentences - 15.8)

    if grade > 16:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")


def count_letters(s):
    letters = 0
    for i in s:
        if i.isalpha():
            letters += 1

    return letters


def count_words(s):
    words = 1
    for i in s:
        if i == " ":
            words += 1

    return words


def count_sentence(s):
    sentence = 0
    for i in s:
        if i in [".", "!", "?"]:
            sentence += 1

    return sentence


if __name__ == "__main__":
    main()
