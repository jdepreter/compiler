
declare i32 @printf(i8*, ...)
@format = private constant [4 x i8] c"%d\0A\00"
@format_float = private constant [4 x i8] c"%f\0A\00"
@format_char = private constant [4 x i8] c"%c\0A\00"

define void @print_int(i32 %a){
  %p = call i32 (i8*, ...)
       @printf(i8* getelementptr inbounds ([4 x i8],
                                           [4 x i8]* @format,
                                           i32 0, i32 0),
               i32 %a)
  ret void
}

define void @print_float(float %a){
  %a_1 = fpext float %a to double
  %p = call i32 (i8*, ...)
       @printf(i8* getelementptr inbounds ([4 x i8],
                                           [4 x i8]* @format_float,
                                           i32 0, i32 0),
               double %a_1)
  ret void
}

define void @print_char(i8 %a){
  %p = call i32 (i8*, ...)
       @printf(i8* getelementptr inbounds ([4 x i8],
                                           [4 x i8]* @format_char,
                                           i32 0, i32 0),
               i8 %a)
  ret void
}
define i32 @main() {
start:
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
call void (i8) @print_char(i8 %r13)
%r14 = load i8 ,i8* %a0 
call void (i8) @print_char(i8 %r14)
%r15 = load i8 ,i8* %a3 
call void (i8) @print_char(i8 %r15)
%r16 = load i32 ,i32* %a5 
call void (i32) @print_int(i32 %r16)
ret i32 0
}
