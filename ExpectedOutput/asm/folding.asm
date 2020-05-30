.data
  fp0: .float 12.999999999999998
  fp1: .float 12.999999999999998


  str.0: .asciiz "%d"
  str.1: .asciiz ""
  str.2: .asciiz "%f"
  seg_fault: .asciiz "Segmentation Fault"

.text
seg: # 
  la $a0, seg_fault # 
  li $v0, 4 # 
  syscall # 
.globl main # 
main: # 
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  addiu $sp, $sp, -4 # Allocate space for symbol: c
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 24 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  sw $t0, 4($sp) # Assigning to c
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for symbol: f
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 40 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  mtc1 $t0, $f0 # 
  cvt.s.w $f0, $f0 # 
  swc1 $f0, 4($sp) # Assigning to f
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for $ra
  sw $ra, 0($sp) # 
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  # Call printf
  addiu $sp, $sp, -4 # Allocate space for rvalue
  addiu $sp, $sp, -4 # allocate space for instance of c
  lw $t0, 20($sp) # Put on top of stack load
  sw $t0, 0($sp) # Put on top of stack save
  la $a0, str.1 # 
  li $v0, 4 # 
  syscall # 
  lw $t0, 0($sp) # Load int for printing
  move $a0, $t0 # 
  li $v0, 1 # 
  syscall # 
  la $a0, str.1 # 
  li $v0, 4 # 
  syscall # 
# Leaving Stack...
  addiu $sp, $sp, 8 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  # Exit printf
  addiu $sp, $sp, 4 # Deallocate space used for method call
  addiu $sp, $sp, -4 # Allocate space for $ra
  sw $ra, 0($sp) # 
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  # Call printf
  addiu $sp, $sp, -4 # Allocate space for rvalue
  addiu $sp, $sp, -4 # allocate space for instance of f
  lwc1 $f0, 16($sp) # Put on top of stack load
  swc1 $f0, 0($sp) # Put on top of stack save
  la $a0, str.1 # 
  li $v0, 4 # 
  syscall # 
  lwc1 $f12, 0($sp) # 
  li $v0, 2 # 
  syscall # 
  la $a0, str.1 # 
  li $v0, 4 # 
  syscall # 
# Leaving Stack...
  addiu $sp, $sp, 8 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  # Exit printf
  addiu $sp, $sp, 4 # Deallocate space used for method call
  addiu $sp, $sp, -4 # Allocate space for rvalue
  l.s $f0 fp0 # 
  swc1 $f0, 0($sp) # 
  lwc1 $f0, 0($sp) # 
  swc1 $f0, 4($sp) # Assigning to f
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for symbol: i
  addiu $sp, $sp, -4 # Allocate space for rvalue
  l.s $f0 fp1 # 
  swc1 $f0, 0($sp) # 
  lwc1 $f0, 0($sp) # 
  cvt.w.s $f0, $f0 # 
  mfc1 $t0, $f0 # 
  sw $t0, 4($sp) # Assigning to i
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for $ra
  sw $ra, 0($sp) # 
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  # Call printf
  addiu $sp, $sp, -4 # Allocate space for rvalue
  addiu $sp, $sp, -4 # allocate space for instance of f
  lwc1 $f0, 20($sp) # Put on top of stack load
  swc1 $f0, 0($sp) # Put on top of stack save
  la $a0, str.1 # 
  li $v0, 4 # 
  syscall # 
  lwc1 $f12, 0($sp) # 
  li $v0, 2 # 
  syscall # 
  la $a0, str.1 # 
  li $v0, 4 # 
  syscall # 
# Leaving Stack...
  addiu $sp, $sp, 8 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  # Exit printf
  addiu $sp, $sp, 4 # Deallocate space used for method call
  addiu $sp, $sp, -4 # Allocate space for $ra
  sw $ra, 0($sp) # 
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  # Call printf
  addiu $sp, $sp, -4 # Allocate space for rvalue
  addiu $sp, $sp, -4 # allocate space for instance of i
  lw $t0, 16($sp) # Put on top of stack load
  sw $t0, 0($sp) # Put on top of stack save
  la $a0, str.1 # 
  li $v0, 4 # 
  syscall # 
  lw $t0, 0($sp) # Load int for printing
  move $a0, $t0 # 
  li $v0, 1 # 
  syscall # 
  la $a0, str.1 # 
  li $v0, 4 # 
  syscall # 
# Leaving Stack...
  addiu $sp, $sp, 8 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  # Exit printf
  addiu $sp, $sp, 4 # Deallocate space used for method call
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 0 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  addiu $sp, $sp, 4 # Deallocate space used for solve math
# Leaving Stack...
  addiu $sp, $sp, 12 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  sw $t0, 0($sp) # 
  li $v0, 10 # 
  syscall # 

