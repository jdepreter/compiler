
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
%a3 = alloca i32 
%r4 = load i8 ,i8* %a2 
%r5 = zext i8 %r4 to i32
%r3 = add i32 %r5, 1
store i32 %r3, i32* %a3
%a4 = alloca i32 
%r7 = load i8 ,i8* %a1 
%r8 = zext i8 %r7 to i32
%r6 = sub i32 %r8, 1
store i32 %r6, i32* %a4
%r9 = load i8 ,i8* %a1 
call void (i8) @print_char(i8 %r9)
%r10 = load i8 ,i8* %a0 
call void (i8) @print_char(i8 %r10)
%r11 = load i32 ,i32* %a4 
call void (i32) @print_int(i32 %r11)
ret i32 0
}
