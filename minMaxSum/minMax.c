#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char** split_string(char*);

// Complete the miniMaxSum function below.
void miniMaxSum(int arr_count, int* arr) {
    int tot = 0;
    int max = 0;
    int min = 5;

    for (int i = 0; i < 5; ++i) {
        tot += arr[i];
        if (arr[i] > max) max = arr[i];
        if (arr[i] < min) min = arr[i];
    }
    printf("%d %d", tot-max, tot-min);
}

int main()
{

    int arr[5] = {1,2,3,4,5};

    int arr_count = 5;

    miniMaxSum(arr_count, arr);

    return 0;
}

