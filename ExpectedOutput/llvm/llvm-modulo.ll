
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
%r0 = srem i32 15, 10
store i32 %r0, i32* %a0
%a1 = alloca i32 
%r2 = load i32 ,i32* %a0 
%r3 = fptrunc double 6.2 to float
%r4 = sitofp i32 %r2 to float
%r1 = fadd float %r4, %r3
%r5 = fptosi float %r1 to i32
store i32 %r5, i32* %a1
%a2 = alloca i32 
%r7 = load i32 ,i32* %a1 
%r8 = load i32 ,i32* %a0 
%r6 = srem i32 %r7, %r8
store i32 %r6, i32* %a2
%r9 = load i32 ,i32* %a2 
call void (i32) @print_int(i32 %r9)
ret i32 0
}
