target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"
@.str.0 = private unnamed_addr constant [3 x i8] c"%d\00", align 1
declare i32 @printf(i8 *, ...)
declare i32 @__isoc99_scanf(i8*, ...)
define i32 @main() {
%a0 = alloca i32 
store i32 1, i32* %a0
br label %label0

label0:
%r2 = load i32 ,i32* %a0 
%r1 = icmp slt i32 %r2, 10 
%r3 = zext i1 %r1 to i32
%r4 = icmp ne i32 %r3, 0
br i1 %r4, label %label1, label %label3

label2:
%r5 = load i32 ,i32* %a0 
%r6 = add i32 %r5, 1
store i32 %r6, i32* %a0
br label %label0

label1:
%a1 = alloca i32 
store i32 1, i32* %a1
br label %label4

label4:
%r9 = load i32 ,i32* %a1 
%r10 = load i32 ,i32* %a0 
%r8 = icmp slt i32 %r9, %r10 
%r11 = zext i1 %r8 to i32
%r12 = icmp ne i32 %r11, 0
br i1 %r12, label %label5, label %label7

label6:
%r13 = load i32 ,i32* %a1 
%r14 = add i32 %r13, 1
store i32 %r14, i32* %a1
br label %label4

label5:
%r16 = load i32 ,i32* %a1 
%r15 = icmp sgt i32 %r16, 3 
%r17 = zext i1 %r15 to i32
%r18 = icmp ne i32 %r17, 0
br i1 %r18, label %label8, label %label9

label8:
br label %label7

label9:
%r19 = load i32 ,i32* %a1 
%r20 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i32 %r19)
br label %label6

label7:
br label %label2

label3:
ret i32 0
ret i32 0
}
