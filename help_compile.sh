clang -ansi -pedantic -S -emit-llvm test.c -o test.ll
clang test.ll -o b.out
./b.out