#include <stdio.h>

int main() {
    int x = 15%10;
    int y = x+6.2;
    int z = y%x;
    printf("%d",z);
    return 0;
}