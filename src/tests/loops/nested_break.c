#include <stdio.h>

int main(){
for (int x = 1; x < 10; x++) {
    for (int y = 1; y < x; y++) {
        if (y > 3) break;
        printf("%d", y);
    }
}

return 0;
}