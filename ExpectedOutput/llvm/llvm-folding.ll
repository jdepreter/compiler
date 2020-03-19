
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
store i32 24, i32* %a0
%a1 = alloca float 
%r0 = sitofp i32 40 to float
store float %r0, float* %a1
%r1 = load float ,float* %a1 
call void (float) @print_float(float %r1)
%r2 = fptrunc double 12.999999999999998 to float
store float %r2, float* %a1
%a2 = alloca i32 
%r3 = fptrunc double 12.999999999999998 to float
%r4 = fptosi float %r3 to i32
store i32 %r4, i32* %a2
%r5 = load float ,float* %a1 
call void (float) @print_float(float %r5)
ret i32 0
}
