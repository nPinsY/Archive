#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

const unsigned int N = 65536;
node *table[N];
unsigned int word_count = 0;

bool check(const char *word)
{
    int len = strlen(word);
    char copy[len + 1];
    for (int i = 0; i < len; i++)
    {
        copy[i] = tolower(word[i]);
    }
    copy[len] = '\0';

    unsigned int index = hash(copy);
    for (node *cursor = table[index]; cursor != NULL; cursor = cursor->next)
    {
        if (strcmp(copy, cursor->word) == 0)
        {
            return true;
        }
    }
    return false;
}

unsigned int hash(const char *word)
{
    unsigned int hash = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        hash += tolower(word[i]);
    }
    return hash % N;
}

bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    char buffer[LENGTH + 1];
    while (fscanf(file, "%s", buffer) != EOF)
    {
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            return false;
        }
        strcpy(new_node->word, buffer);
        unsigned int index = hash(buffer);
        new_node->next = table[index];
        table[index] = new_node;
        word_count++;
    }

    fclose(file);
    return true;
}

unsigned int size(void)
{
    return word_count;
}

bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}


// Tools I used.
// https://www.geeksforgeeks.org/hashing-data-structure/
// https://www.geeksforgeeks.org/data-structures/linked-list/
