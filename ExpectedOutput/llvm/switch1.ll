target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"
@.str.0 = private unnamed_addr constant [7 x i8] c"Niet 2\00", align 1
@.str.1 = private unnamed_addr constant [3 x i8] c"%d\00", align 1
@.str.2 = private unnamed_addr constant [8 x i8] c"Default\00", align 1
declare i32 @printf(i8 *, ...)
declare i32 @__isoc99_scanf(i8*, ...)
define i32 @main() {
%a0 = alloca i32 
store i32 3, i32* %a0
%r0 = load i32 ,i32* %a0 
switch i32 %r0, label %label4 [i32 1, label %label0
i32 2, label %label1
i32 3, label %label2
i32 4, label %label3
]
br label %label0

label0:
br label %label1

label1:
%r1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.str.0, i32 0, i32 0))
br label %label2

label2:
br label %label3

label3:
%r2 = load i32 ,i32* %a0 
%r3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.1, i32 0, i32 0),i32 %r2)
br label %label5
br label %label4

label4:
%r4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.2, i32 0, i32 0))
br label %label5

label5:
ret i32 0
ret i32 0
}
