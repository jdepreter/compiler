#include <stdio.h>

int main()
{
    int x = 5;
    int* y = &x;
    int** z = &y;
    printf("%i\n", x);
}