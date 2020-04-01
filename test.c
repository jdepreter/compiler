#include <stdio.h>

void f(int x);

int main(){
    f();
}

int x;

void f(float x) {
    printf("%d", x);
}