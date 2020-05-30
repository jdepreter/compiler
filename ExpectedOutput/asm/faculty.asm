.data
  fp0: .float 3.0


  str.0: .asciiz "%d"
  str.1: .asciiz ""
  seg_fault: .asciiz "Segmentation Fault"

.text
seg: # 
  la $a0, seg_fault # 
  li $v0, 4 # 
  syscall # 
x_0: # 
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 1 # 
  sw $t0, 0($sp) # 
  addiu $sp, $sp, -4 # allocate space for instance of i
  lw $t0, 20($sp) # Put on top of stack load
  sw $t0, 0($sp) # Put on top of stack save
  lw $t0, 0($sp) # 
  lw $t1, 4($sp) # 
  seq $t0, $t1, $t0 # 
  addiu $sp, $sp, 4 # Deallocate right operand
  sw $t0, 0($sp) # Overwrite left operand
  lw $t0, 0($sp) # 
  addiu $sp, $sp, 4 # Deallocate space used for solve math
  beq $t0, $0, Else0 # 
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 1 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  addiu $sp, $sp, 4 # Deallocate space used for solve math
# Leaving Stack...
  addiu $sp, $sp, 0 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Leaving Stack...
  addiu $sp, $sp, 0 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  sw $t0, 0($sp) # 
jr $ra # 
Else0: # 
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  addiu $sp, $sp, -4 # allocate space for instance of i
  lw $t0, 20($sp) # Put on top of stack load
  sw $t0, 0($sp) # Put on top of stack save
  addiu $sp, $sp, -4 # Allocate space for $ra
  sw $ra, 0($sp) # 
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  addiu $sp, $sp, -4 # allocate space for instance of i
  lw $t0, 32($sp) # Put on top of stack load
  sw $t0, 0($sp) # Put on top of stack save
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 1 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  lw $t1, 4($sp) # 
  sub $t0, $t1, $t0 # 
  addiu $sp, $sp, 4 # Delete right operand
  sw $t0, 0($sp) # Overwrite left operand
  addiu $sp, $sp, -4 # allocate space for instance of y
  lwc1 $f0, 32($sp) # Put on top of stack load
  swc1 $f0, 0($sp) # Put on top of stack save
  addiu $sp, $sp, -4 # allocate space for instance of c
  lb $t0, 32($sp) # Put on top of stack load
  sb $t0, 0($sp) # Put on top of stack save
jal x_0 # 
  lw $t0, 0($sp) # load in the return value of the function
# Leaving Stack...
  addiu $sp, $sp, 12 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  lw $ra, 0($sp) # something with functions
  sw $t0, 0($sp) # something with functions
  lw $t0, 0($sp) # 
  lw $t1, 4($sp) # 
  mul $t0, $t1, $t0 # 
  addiu $sp, $sp, 4 # Delete right operand
  sw $t0, 0($sp) # Overwrite left operand
  lw $t0, 0($sp) # 
  addiu $sp, $sp, 4 # Deallocate space used for solve math
# Leaving Stack...
  addiu $sp, $sp, 0 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Leaving Stack...
  addiu $sp, $sp, 0 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  sw $t0, 0($sp) # 
jr $ra # 
.globl main # 
main: # 
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  addiu $sp, $sp, -4 # Allocate space for symbol: y
  addiu $sp, $sp, -4 # Allocate space for $ra
  sw $ra, 0($sp) # 
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 3 # 
  sw $t0, 0($sp) # 
  addiu $sp, $sp, -4 # Allocate space for rvalue
  l.s $f0 fp0 # 
  swc1 $f0, 0($sp) # 
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 99 # 
  sb $t0, 0($sp) # 
jal x_0 # 
  lw $t0, 0($sp) # load in the return value of the function
# Leaving Stack...
  addiu $sp, $sp, 12 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  lw $ra, 0($sp) # something with functions
  sw $t0, 0($sp) # something with functions
  lw $t0, 0($sp) # 
  sw $t0, 4($sp) # Assigning to y
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
  addiu $sp, $sp, -4 # allocate space for instance of y
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
  addiu $sp, $sp, 4 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  sw $t0, 0($sp) # 
  li $v0, 10 # 
  syscall # 

