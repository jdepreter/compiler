target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"
@.str.0 = private unnamed_addr constant [3 x i8] c"%i\00", align 1
declare i32 @printf(i8 *, ...)
declare i32 @__isoc99_scanf(i8*, ...)
define i32 @main() {
%a0 = alloca float 
%r0 = fptrunc double 1.25 to float
store float %r0, float* %a0
%a1 = alloca i32 
%r4 = load float ,float* %a0 
%r5 = fptrunc double 1.25 to float
%r3 = fcmp oeq float %r4, %r5 
%r6 = zext i1 %r3 to i32
%r2 = or i32 1, %r6
%r1 = add i32 5, %r2
store i32 %r1, i32* %a1
%r7 = load i32 ,i32* %a1 
%r8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i32 %r7)
ret i32 0
ret i32 0
}
