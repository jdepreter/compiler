#include <stdio.h>

int main(){
    int y = 2;
    int z = 2;
    int x[10];
    x[2] = 0;
    x[z = 5, x[2]] = 1;
    printf("%d", x[0]);
    z= 2 , y= 9, x[2];
}
