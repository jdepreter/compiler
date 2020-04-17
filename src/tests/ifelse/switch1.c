#include <stdio.h>

// Should print 3
int main() {
    int x = 3;

    switch(x) {
        case 1:
        case 2:
            printf("Niet 2");
        case 3:
        case 4:
            printf("%d", x);
            break;
        default:
            printf("Default");

    }
    return 0;
}