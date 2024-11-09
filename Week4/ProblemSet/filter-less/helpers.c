#include "helpers.h"
#include <math.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float avg = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0;
            int new_scale = round(avg);

            image[i][j].rgbtRed = new_scale;
            image[i][j].rgbtGreen = new_scale;
            image[i][j].rgbtBlue = new_scale;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepiaRed = round((image[i][j].rgbtRed * 0.393) + (image[i][j].rgbtGreen * 0.769) + (image[i][j].rgbtBlue * 0.189));
            int sepiaGreen = round((image[i][j].rgbtRed * 0.349) + (image[i][j].rgbtGreen * 0.686) + (image[i][j].rgbtBlue * 0.168));
            int sepiaBlue = round((image[i][j].rgbtRed * 0.272) + (image[i][j].rgbtGreen * 0.534) + (image[i][j].rgbtBlue * 0.131));

            image[i][j].rgbtRed = fmin(sepiaRed, 255);
            image[i][j].rgbtGreen = fmin(sepiaGreen, 255);
            image[i][j].rgbtBlue = fmin(sepiaBlue, 255);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];

            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp_image[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sumRed = 0, sumGreen = 0, sumBlue = 0, count = 0;

            for (int dx = -1; dx <= 1; dx++)
            {
                for (int dy = -1; dy <= 1; dy++)
                {
                    int x = i + dx, y = j + dy;

                    if (x >= 0 && x < height && y >= 0 && y < width)
                    {
                        sumRed += image[x][y].rgbtRed;
                        sumGreen += image[x][y].rgbtGreen;
                        sumBlue += image[x][y].rgbtBlue;
                        count++;
                    }
                }
            }

            // Compute the average color for the pixel
            temp_image[i][j].rgbtRed = round((float) sumRed / count);
            temp_image[i][j].rgbtGreen = round((float) sumGreen / count);
            temp_image[i][j].rgbtBlue = round((float) sumBlue / count);
        }
    }

    // Copy the blurred values from the temporary image back to the original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp_image[i][j];
        }
    }
    return;
}
