#include <stdio.h>

int y = 2;
void f(int* x) {
    x = 1;
}

int main(){
    float a = 2.0;
    float* b = &a;
    f(b);
}

int x = 4;