#include <stdio.h>

int main()
{
    int x = -0;
    int* y = &x;
    int******* z = &y;
    printf("%i\n", **z);
}