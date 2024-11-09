#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    if (score1 == score2)
    {
        printf("Tie!\n");
    }
    else if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else
    {
        printf("Player 2 wins!\n");
    }
}

int compute_score(string word)
{
    int score = 0;
    int length = strlen(word);

    for (int i = 0; i < length; i++)
    {
        word[i] = toupper(word[i]);
    }

    for (int i = 0; i < length; i++)
    {
        char c = word[i];
        if (c >= 'A' && c <= 'Z')
        {
            score += POINTS[c - 'A'];
        }
    }
    return score;
}