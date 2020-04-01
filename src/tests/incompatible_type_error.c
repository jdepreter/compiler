int main(){
float x = 4;
float* y = &x;
float* z = &x;
z = z + y;
return 0;
}