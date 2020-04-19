target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"
@.str.0 = private unnamed_addr constant [3 x i8] c"%d\00", align 1
declare i32 @printf(i8 *, ...)
declare i32 @__isoc99_scanf(i8*, ...)
define i32 @x_0(i32,float,i8) {
%a0 = alloca i32 
store i32 %0, i32* %a0
%a1 = alloca float 
store float %1, float* %a1
%a2 = alloca i8 
store i8 %2, i8* %a2
%r1 = load i32 ,i32* %a0 
%r0 = icmp eq i32 1, %r1 
%r2 = zext i1 %r0 to i32
%r3 = icmp ne i32 %r2, 0
br i1 %r3, label %label0, label %label1

label0:
ret i32 1

label1:
%r5 = load i32 ,i32* %a0 
%r7 = load i32 ,i32* %a0 
%r6 = sub i32 %r7, 1
%r8 = load float ,float* %a1 
%r9 = load i8 ,i8* %a2 
%r10 = call i32 (i32,float,i8) @x_0(i32 %r6,float %r8,i8 %r9)
%r4 = mul i32 %r5, %r10
ret i32 %r4
ret i32 0
}
define i32 @main() {
%a3 = alloca i32 
%r0 = fptrunc double 3.0 to float
%r1 = call i32 (i32,float,i8) @x_0(i32 3,float %r0,i8 99)
store i32 %r1, i32* %a3
%r2 = load i32 ,i32* %a3 
%r3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i32 %r2)
ret i32 0
ret i32 0
}
