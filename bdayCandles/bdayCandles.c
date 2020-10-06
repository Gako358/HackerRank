#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * Complete the 'birthdayCakeCandles' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY candles as parameter.
 */

int birthdayCakeCandles(int candles_count, int* candles) {
    int num, i, max = 0, max_count =0;
    for (i = 0; i < candles_count; i++){
        if (candles[i] > max)
            max = candles[i];

    }
    for (i = 0; i < candles_count; i++) {
        if (candles[i] == max)
            max_count++;
    }
    return max_count;

}

int main()
{
    

    return 0;
}
