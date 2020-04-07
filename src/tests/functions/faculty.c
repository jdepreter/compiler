#include <stdio.h>

int x(int i, float y, char c){

    if (1==i){
        return 1;
    }
    else{
        return i*x(i-1, y , c);
    }

}

int main(){
    int y = x(3, 3.0, 'c');
    printf("%d", y);
    return 0;
}