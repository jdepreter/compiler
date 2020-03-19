
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
%a0 = alloca i32 
store i32 1, i32* %a0
%a1 = alloca i32 
store i32 1, i32* %a1
%r1 = load i32 ,i32* %a1 
%r0 = add i32 %r1, 1
store i32 %r0, i32* %a1
%r2 = load i32 ,i32* %a1 
call void (i32) @print_int(i32 %r2)
%r4 = load i32 ,i32* %a0 
%r3 = add i32 %r4, 2
store i32 %r3, i32* %a0
%r5 = load i32 ,i32* %a0 
call void (i32) @print_int(i32 %r5)
ret i32 0
}
