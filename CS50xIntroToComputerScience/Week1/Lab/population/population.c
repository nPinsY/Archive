#include <cs50.h>
#include <stdio.h>

void get_size(int *start, int *end);
int calculate(int start, int end);

int main(void)
{
    int start_size, end_size;
    get_size(&start_size, &end_size);
    int years = calculate(start_size, end_size);
    printf("Years: %i\n", years);
}

void get_size(int *start, int *end)
{
    do
    {
        *start = get_int("What's the start size: ");
    }
    while (*start < 9);

    do
    {
        *end = get_int("What's the end size: ");
    }
    while (*end < *start);
}

int calculate(int start, int end)
{
    int years = 0;
    while (start < end)
    {
        start = start + (start / 3) - (start / 4);
        years++;
    }
    return years;
}