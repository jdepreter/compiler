#include <stdio.h>

void f(float* i) {
    *i = 85;
}

int main(){
    float x = 2;
    float * y = &x;
    f(x);
    printf("%d", *y);
}

