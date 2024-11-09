#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

float count_letters(int length, string input_sentence);
float count_words(int length, string input_sentence);
float count_sentence(int length, string input_sentence);

int main(void)
{
    string input_sentence = get_string("Text: ");
    int length = strlen(input_sentence);
    float letters = count_letters(length, input_sentence);
    float words = count_words(length, input_sentence);
    float sentence = count_sentence(length, input_sentence);

    float average_words = (letters / words) * 100;
    float average_sentences = (sentence / words) * 100;
    int grade = round(0.0588 * average_words - 0.296 * average_sentences - 15.8);

    if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

float count_letters(int length, string input_sentence)
{
    int letters = 0;
    for (int i = 0; i < length; i++)
    {
        char c = input_sentence[i];
        if (isalpha(c))
        {
            letters++;
        }
    }
    return letters;
}

float count_words(int length, string input_sentence)
{
    int words = 1;
    for (int i = 0; i < length; i++)
    {
        char c = input_sentence[i];
        if (isspace(c))
        {
            words++;
        }
    }
    return words;
}

float count_sentence(int length, string input_sentence)
{
    int sentence = 0;
    for (int i = 0; i < length; i++)
    {
        char c = input_sentence[i];
        if ((c == '.') || (c == '!') || (c == '?'))
        {
            sentence++;
        }
    }
    return sentence;
}
