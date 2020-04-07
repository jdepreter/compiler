#include <stdio.h>

int f(int x);
int f(int x) {printf("%d", x); return x;}

int main() {
    int c = 2;
    f(c);
    return 0;
}