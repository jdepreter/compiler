#include <stdio.h>

int main() {
    int c = 1+2+3*(1+6-9/10*3*9/10);
    float f = 1*(1+9)*(5*9/10 - 9/10*3);
    printf("%f", f);
    f = 1*(1+9)*(5*9/10 - 9.0/10*3);
    int i = 1*(1+9)*(5*9/10 - 9.0/10*3);
    printf("%f",f);
    return 0;
}