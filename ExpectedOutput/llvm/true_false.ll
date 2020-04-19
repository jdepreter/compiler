target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"
@.str.0 = private unnamed_addr constant [3 x i8] c"%d\00", align 1
@.str.1 = private unnamed_addr constant [2 x i8] c"t\00", align 1
@.str.2 = private unnamed_addr constant [2 x i8] c"f\00", align 1
declare i32 @printf(i8 *, ...)
declare i32 @__isoc99_scanf(i8*, ...)
define i32 @main() {
%a0 = alloca i32 
store i32 0, i32* %a0
%a1 = alloca i32 
store i32 8, i32* %a1
%r1 = load i32 ,i32* %a1 
%r0 = icmp eq i32 %r1, 8 
%r2 = zext i1 %r0 to i32
%r3 = icmp ne i32 %r2, 0
br i1 %r3, label %label0, label %label1

label0:
%r4 = load i32 ,i32* %a1 
%r5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i32 %r4)
br label %label2

label1:
%r6 = load i32 ,i32* %a0 
%r7 = icmp ne i32 %r6, 0
br i1 %r7, label %label3, label %label4

label3:
%r8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.1, i32 0, i32 0))
br label %label5

label4:
%r9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.2, i32 0, i32 0))
br label %label5

label5:
%r10 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.2, i32 0, i32 0))
br label %label2

label2:
%r12 = load i32 ,i32* %a1 
%r11 = add i32 %r12, 1
%r13 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i32 %r11)
ret i32 0
ret i32 0
}
