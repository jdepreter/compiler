#include <stdio.h>

int main(){

for (int x = 0; x < 10; x++) {
    if (x<2) continue;
    printf("%d", x);
}


return 0;

}