#include <stdio.h>

int main()
{
    int x = -0;
    int* y = &x;
    int******* z = 1;
    z = z + y;
    printf("%i\n", **z);
}