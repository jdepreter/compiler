#include <stdio.h>

int main() {
    float x = 0.2;
    int a = 1;
    int v = !(a==2&&!(x==3||!(5>3)));
    printf("%d",v);
    return 0;
}