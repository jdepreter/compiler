
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
%r1 = sub i32 0, 3
%r2 = sub i32 0, %r1
%r3 = sub i32 0, %r2
%r4 = sub i32 0, %r3
%r5 = sub i32 0, %r4
%r6 = sub i32 0, %r5
%r0 = add i32 5, %r6
store i32 %r0, i32* %a0
%r9 = load i32 ,i32* %a0 
%r8 = add i32 %r9, 1
%r7 = and i32 %r8, -1
call void (i32) @print_int(i32 %r7)
ret i32 0
}
