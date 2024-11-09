#include <cs50.h>
#include <stdio.h>

void build(int h);
void get_height(int *height);

int main(void)
{
    int height;
    get_height(&height);
    build(height);
}

void build(int h)
{
    for (int i = 1; i <= h; i++)
    {
        // Print spaces
        for (int j = 0; j < h - i; j++)
        {
            printf(" ");
        }

        // Print hashes
        for (int j = 0; j < i; j++)
        {
            printf("#");
        }

        printf("\n");
    }
}

void get_height(int *height)
{
    do
    {
        *height = get_int("Height: ");
    }
    while (*height < 1 || *height > 8);
}