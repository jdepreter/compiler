#include <stdio.h>

void f();

int main(){
    f();
}

int x;

void f() {
    printf("%d", x);
}