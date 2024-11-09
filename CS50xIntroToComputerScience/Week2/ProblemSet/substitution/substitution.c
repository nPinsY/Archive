#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

bool validate_cipher(int length, string key);
void cipher(string key, string plaintext, char *ciphertext);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./cypher key\n");
        return 1;
    }

    string key = argv[1];
    int length = strlen(key);

    if (validate_cipher(length, key))
    {
        string plaintext = get_string("plaintext: ");
        char ciphertext[strlen(plaintext) + 1];
        cipher(key, plaintext, ciphertext);
        printf("ciphertext: %s\n", ciphertext);
        return 0;
    }
    else
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
}

bool validate_cipher(int length, string key)
{
    if (length != 26)
    {
        return false;
    }

    int count[26] = {0};
    for (int i = 0; i < length; i++)
    {
        char c = tolower(key[i]);
        if (isalpha(c))
        {
            count[c - 'a']++;
        }
        else
        {
            return false;
        }
    }

    for (int i = 0; i < 26; i++)
    {
        if (count[i] != 1)
        {
            return false;
        }
    }
    return true;
}

void cipher(string key, string plaintext, char *ciphertext)
{
    int plength = strlen(plaintext);

    for (int i = 0; i < plength; i++)
    {
        char c = plaintext[i];
        if (isupper(c))
        {
            int index = (c - 'A');
            ciphertext[i] = toupper(key[index]);
        }
        else if (islower(c))
        {
            int index = (c - 'a');
            ciphertext[i] = tolower(key[index]);
        }
        else
        {
            ciphertext[i] = c;
        }
    }
    ciphertext[plength] = '\0';
}
