#include <stdio.h>

int main()
{
    float x = 33;
    float d = -x;
    int* y = &x;
    int* a = &x + 'c';
    printf("%d", ++x);
}