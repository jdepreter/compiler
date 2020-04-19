target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"
@.str.0 = private unnamed_addr constant [3 x i8] c"%d\00", align 1
declare i32 @printf(i8 *, ...)
declare i32 @__isoc99_scanf(i8*, ...)
define i32 @main() {
%a0 = alloca i32 
store i32 6, i32* %a0
%r0 = load i32 ,i32* %a0 
%r1 = add i32 %r0, 1
store i32 %r1, i32* %a0
%r2 = load i32 ,i32* %a0 
%r3 = add i32 %r2, 1
store i32 %r3, i32* %a0
%r4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i32 %r2)
%r5 = load i32 ,i32* %a0 
%r6 = add i32 %r5, 1
store i32 %r6, i32* %a0
%r7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i32 %r6)
%r8 = load i32 ,i32* %a0 
%r9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i32 %r8)
ret i32 0
ret i32 0
}
