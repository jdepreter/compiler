target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"
@.str.0 = private unnamed_addr constant [3 x i8] c"%d\00", align 1
declare i32 @printf(i8 *, ...)
declare i32 @__isoc99_scanf(i8*, ...)
define i32 @main() {
%a0 = alloca i32 
store i32 5, i32* %a0
%a1 = alloca i32* 
store i32* %a0, i32** %a1
%a2 = alloca i32** 
store i32** %a1, i32*** %a2
%r0 = load i32** ,i32*** %a2 
%r1 = load i32* ,i32** %r0 
store i32 3, i32* %r1
%r2 = load i32** ,i32*** %a2 
%r3 = load i32* ,i32** %r2 
%r4 = load i32 ,i32* %r3 
%r5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0),i32 %r4)
ret i32 0
ret i32 0
}
