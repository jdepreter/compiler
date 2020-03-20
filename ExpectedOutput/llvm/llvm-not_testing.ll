
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
%a0 = alloca float 
%r0 = fptrunc double 0.2 to float
store float %r0, float* %a0
%a1 = alloca i32 
store i32 1, i32* %a1
%a2 = alloca i32 
%r3 = load i32 ,i32* %a1 
%r2 = icmp eq i32 %r3, 2 
%r4 = zext i1 %r2 to i32
%r7 = load float ,float* %a0 
%r8 = sitofp i32 3 to float
%r6 = fcmp oeq float %r7, %r8 
%r9 = zext i1 %r6 to i32
%r11 = trunc i32 1 to i1
%r10 = add i1 %r11, 1
%r12 = zext i1 %r10 to i32%r5 = or i32 %r9, %r12
%r14 = trunc i32 %r5 to i1
%r13 = add i1 %r14, 1
%r15 = zext i1 %r13 to i32%r1 = and i32 %r4, %r15
%r17 = trunc i32 %r1 to i1
%r16 = add i1 %r17, 1
%r18 = zext i1 %r16 to i32store i32 %r18, i32* %a2
ret i32 0
}
