target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"
@.str.0 = private unnamed_addr constant [3 x i8] c"%d\00", align 1
declare i32 @printf(i8 *, ...)
declare i32 @__isoc99_scanf(i8*, ...)
define i32 @main() {
%a0 = alloca i32 
%r0 = srem i32 15, 10
store i32 %r0, i32* %a0
%a1 = alloca i32 
%r2 = load i32 ,i32* %a0 
%r3 = fptrunc double 6.2 to float
%r4 = sitofp i32 %r2 to float
%r1 = fadd float %r4, %r3
%r5 = fptosi float %r1 to i32
store i32 %r5, i32* %a1
%a2 = alloca i32 
%r7 = load i32 ,i32* %a1 
%r8 = load i32 ,i32* %a0 
%r6 = srem i32 %r7, %r8
store i32 %r6, i32* %a2
%r9 = load i32 ,i32* %a2 
%r10 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i32 %r9)
ret i32 0
ret i32 0
}
