#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover corrupted_file\n");
        return 1;
    }

    FILE *inputFile = fopen(argv[1], "r");
    if (inputFile == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", argv[1]);
        return 2;
    }

    FILE *outputFile = NULL;
    unsigned char buffer[512];
    int fileCount = 0;
    char filename[50];

    while (fread(buffer, 1, 512, inputFile) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (outputFile != NULL)
            {
                fclose(outputFile);
            }

            sprintf(filename, "%03d.jpg", fileCount++);
            outputFile = fopen(filename, "w");
            if (outputFile == NULL)
            {
                fprintf(stderr, "Could not create %s.\n", filename);
                return 3;
            }
        }

        if (outputFile != NULL)
        {
            fwrite(buffer, 1, 512, outputFile);
        }
    }

    if (outputFile != NULL)
    {
        fclose(outputFile);
    }
    fclose(inputFile);

    return 0;
}
