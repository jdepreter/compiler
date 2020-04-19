target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"
@.str.0 = private unnamed_addr constant [3 x i8] c"%c\00", align 1
declare i32 @printf(i8 *, ...)
declare i32 @__isoc99_scanf(i8*, ...)
define i32 @main() {
%a0 = alloca i8 
%r0 = trunc i32 100 to i8
store i8 %r0, i8* %a0
%r1 = load i8 ,i8* %a0 
%r2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i8 %r1)
ret i32 0
ret i32 0
}
