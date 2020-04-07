#include <stdio.h>

int main(){

for (int x = 1; x < 10; x++) {
    printf("%d", x);
    if (x == 4) break;
}

int x = 1;
while (x < 3) {
    printf("%d", x);
    ((x))++;
}
return 0;
}