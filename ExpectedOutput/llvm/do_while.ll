target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"
@.str.0 = private unnamed_addr constant [3 x i8] c"%d\00", align 1
declare i32 @printf(i8 *, ...)
declare i32 @__isoc99_scanf(i8*, ...)
define i32 @main() {
%a0 = alloca i32 
store i32 0, i32* %a0
br label %label1

label1:
%r1 = load i32 ,i32* %a0 
%r2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i32 %r1)
%r3 = load i32 ,i32* %a0 
%r4 = add i32 %r3, 1
store i32 %r4, i32* %a0
br label %label0

label0:
%r5 = icmp ne i32 0, 0
br i1 %r5, label %label1, label %label2

label2:
ret i32 0
ret i32 0
}
