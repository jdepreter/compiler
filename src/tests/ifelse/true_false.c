#include <stdio.h>

int main(){
int y = 0;
int x = 8;
if (x == 8) {
    printf("%d", x);
}
else {
    if (y) {
        printf("t");
    }
    else {
        printf("f");
    }
    printf("f");
}
printf("%d", x+1);
return 0;
}