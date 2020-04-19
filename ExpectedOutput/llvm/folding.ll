target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"
@.str.0 = private unnamed_addr constant [3 x i8] c"%d\00", align 1
@.str.1 = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare i32 @printf(i8 *, ...)
declare i32 @__isoc99_scanf(i8*, ...)
define i32 @main() {
%a0 = alloca i32 
store i32 24, i32* %a0
%a1 = alloca float 
%r0 = sitofp i32 40 to float
store float %r0, float* %a1
%r1 = load i32 ,i32* %a0 
%r2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i32 %r1)
%r3 = load float ,float* %a1 
%r4 = fpext float %r3 to double%r5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.1, i32 0, i32 0),double %r4)
%r6 = fptrunc double 12.999999999999998 to float
store float %r6, float* %a1
%a2 = alloca i32 
%r7 = fptrunc double 12.999999999999998 to float
%r8 = fptosi float %r7 to i32
store i32 %r8, i32* %a2
%r9 = load float ,float* %a1 
%r10 = fpext float %r9 to double%r11 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.1, i32 0, i32 0),double %r10)
%r12 = load i32 ,i32* %a2 
%r13 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i32 %r12)
ret i32 0
ret i32 0
}
