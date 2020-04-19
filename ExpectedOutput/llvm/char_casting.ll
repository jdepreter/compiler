target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"
@.str.0 = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.str.1 = private unnamed_addr constant [3 x i8] c"%i\00", align 1
declare i32 @printf(i8 *, ...)
declare i32 @__isoc99_scanf(i8*, ...)
define i32 @main() {
%a0 = alloca i8 
store i8 99, i8* %a0
%a1 = alloca i8 
store i8 98, i8* %a1
%a2 = alloca i8 
%r1 = load i8 ,i8* %a1 
%r2 = load i8 ,i8* %a0 
%r0 = add i8 %r1, %r2
store i8 %r0, i8* %a2
%a3 = alloca i8 
%r4 = load i8 ,i8* %a1 
%r5 = zext i8 %r4 to i32
%r3 = add i32 %r5, 2
%r6 = trunc i32 %r3 to i8
store i8 %r6, i8* %a3
%a4 = alloca i32 
%r8 = load i8 ,i8* %a2 
%r9 = zext i8 %r8 to i32
%r7 = add i32 %r9, 1
store i32 %r7, i32* %a4
%a5 = alloca i32 
%r11 = load i8 ,i8* %a1 
%r12 = zext i8 %r11 to i32
%r10 = sub i32 %r12, 1
store i32 %r10, i32* %a5
%r13 = load i8 ,i8* %a1 
%r14 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i8 %r13)
%r15 = load i8 ,i8* %a0 
%r16 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i8 %r15)
%r17 = load i8 ,i8* %a3 
%r18 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i8 %r17)
%r19 = load i32 ,i32* %a5 
%r20 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.1, i32 0, i32 0),i32 %r19)
ret i32 0
ret i32 0
}
