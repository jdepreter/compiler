declare i32 @printf(i8*, ...)
; @format = private constant [8 x i8] c"d = %d\0A\00"
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
  %p = call i32 (i8*, ...)
       @printf(i8* getelementptr inbounds ([4 x i8],
                                           [4 x i8]* @format_float,
                                           i32 0, i32 0),
               float %a)
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
        store i8 97, i8* %a0
        %a1 = alloca i8
        store i8 2, i8* %a1
        %a2 = alloca i8
        %r1 = load i8, i8* %a1
        %r2 = load i8, i8* %a0
        %r0 = add i8 %r1, %r2
        store i8 %r0, i8* %a2
        call void (i32) @print_int(i32 %r0)
        ret i32 0
}


