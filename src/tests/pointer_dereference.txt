int main(){
int i = 5;
int* j = &i;
int** x = &j;
**x = 3;
printf(**x);
return 0;
}