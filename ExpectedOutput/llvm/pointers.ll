target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"
define i32 @main() {
%a0 = alloca i32 
store i32 5, i32* %a0
%a1 = alloca i32* 
store i32* %a0, i32** %a1
%a2 = alloca float 
%r0 = fptrunc double 6.0 to float
store float %r0, float* %a2
%a3 = alloca float* 
store float* %a2, float** %a3
%a4 = alloca i8 
store i8 32, i8* %a4
%a5 = alloca i8* 
store i8* %a4, i8** %a5
ret i32 0
ret i32 0
}
