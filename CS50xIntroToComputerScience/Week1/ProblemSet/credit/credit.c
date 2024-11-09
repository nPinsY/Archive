#include <cs50.h>
#include <stdbool.h>
#include <stdio.h>

bool checksum(long card, int length);
void categorize(long card, int length);

int main(void)
{
    long card = get_long("Input card number:\n");
    long temp_card = card;

    int length = 0;
    while (temp_card)
    {
        temp_card /= 10;
        length++;
    }

    if (checksum(card, length))
    {
        categorize(card, length);
    }
    else
    {
        printf("INVALID\n");
    }
}

bool checksum(long card, int length)
{
    int sum = 0;

    for (int i = 1; i <= length; i++)
    {
        int digit = card % 10;
        card /= 10;

        if (i % 2 == 1)
        {
            sum += digit;
        }
        else
        {
            int doubled = digit * 2;
            sum += (doubled / 10) + (doubled % 10);
        }
    }
    return sum % 10 == 0;
}

void categorize(long card, int length)
{
    int first_two = 0;

    while (card >= 100)
    {
        card /= 10;
    }
    first_two = card;

    if ((length == 13 || length == 16) && (first_two / 10 == 4))
    {
        printf("VISA\n");
    }
    else if (length == 15 && (first_two == 34 || first_two == 37))
    {
        printf("AMEX\n");
    }
    else if (length == 16 && (first_two >= 51 && first_two <= 55))
    {
        printf("MASTERCARD\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
