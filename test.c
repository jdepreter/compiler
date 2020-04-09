#include <stdio.h>

int main() {
    int* x[5];
    int y = 6;
    x[0] = &y;
    *x[0] = 4;
    printf("%d", y);
}