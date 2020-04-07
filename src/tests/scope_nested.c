#include <stdio.h>

int main() {
    {
        int c = 1;
        {
            int c = 1;
            c = c + 1;
            printf("%d",c);
        }
        c = c + 2;
        printf("%d",c);
    }
    return 0;
}