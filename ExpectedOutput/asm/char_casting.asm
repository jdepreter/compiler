.data


  str.0: .asciiz "%c"
  str.1: .asciiz ""
  str.2: .asciiz "%i"
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
  li $t0, 99 # 
  sb $t0, 0($sp) # 
  lb $t0, 0($sp) # 
  sb $t0, 4($sp) # Assigning to c
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for symbol: b
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 98 # 
  sb $t0, 0($sp) # 
  lb $t0, 0($sp) # 
  sb $t0, 4($sp) # Assigning to b
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for symbol: a
  addiu $sp, $sp, -4 # allocate space for instance of b
  lb $t0, 8($sp) # Put on top of stack load
  sb $t0, 0($sp) # Put on top of stack save
  addiu $sp, $sp, -4 # allocate space for instance of c
  lb $t0, 16($sp) # Put on top of stack load
  sb $t0, 0($sp) # Put on top of stack save
  lb $t0, 0($sp) # 
  lb $t1, 4($sp) # 
  add $t0, $t1, $t0 # 
  addiu $sp, $sp, 4 # Delete right operand
  sb $t0, 0($sp) # Overwrite left operand
  lb $t0, 0($sp) # 
  sb $t0, 4($sp) # Assigning to a
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for symbol: d
  addiu $sp, $sp, -4 # allocate space for instance of b
  lb $t0, 12($sp) # Put on top of stack load
  sb $t0, 0($sp) # Put on top of stack save
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 2 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  lb $t1, 4($sp) # 
  add $t0, $t1, $t0 # 
  addiu $sp, $sp, 4 # Delete right operand
  sw $t0, 0($sp) # Overwrite left operand
  lw $t0, 0($sp) # 
  sb $t0, 4($sp) # Assigning to d
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for symbol: x
  addiu $sp, $sp, -4 # allocate space for instance of a
  lb $t0, 12($sp) # Put on top of stack load
  sb $t0, 0($sp) # Put on top of stack save
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 1 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  lb $t1, 4($sp) # 
  add $t0, $t1, $t0 # 
  addiu $sp, $sp, 4 # Delete right operand
  sw $t0, 0($sp) # Overwrite left operand
  lw $t0, 0($sp) # 
  sw $t0, 4($sp) # Assigning to x
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for symbol: y
  addiu $sp, $sp, -4 # allocate space for instance of b
  lb $t0, 20($sp) # Put on top of stack load
  sb $t0, 0($sp) # Put on top of stack save
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 1 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  lb $t1, 4($sp) # 
  sub $t0, $t1, $t0 # 
  addiu $sp, $sp, 4 # Delete right operand
  sw $t0, 0($sp) # Overwrite left operand
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
  addiu $sp, $sp, -4 # allocate space for instance of b
  lb $t0, 32($sp) # Put on top of stack load
  sb $t0, 0($sp) # Put on top of stack save
  la $a0, str.1 # 
  li $v0, 4 # 
  syscall # 
  lb $t0, 0($sp) # Load char for printing
  move $a0, $t0 # 
  li $v0, 11 # 
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
  addiu $sp, $sp, -4 # allocate space for instance of c
  lb $t0, 36($sp) # Put on top of stack load
  sb $t0, 0($sp) # Put on top of stack save
  la $a0, str.1 # 
  li $v0, 4 # 
  syscall # 
  lb $t0, 0($sp) # Load char for printing
  move $a0, $t0 # 
  li $v0, 11 # 
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
  addiu $sp, $sp, -4 # allocate space for instance of d
  lb $t0, 24($sp) # Put on top of stack load
  sb $t0, 0($sp) # Put on top of stack save
  la $a0, str.1 # 
  li $v0, 4 # 
  syscall # 
  lb $t0, 0($sp) # Load char for printing
  move $a0, $t0 # 
  li $v0, 11 # 
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
  addiu $sp, $sp, 24 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  sw $t0, 0($sp) # 
  li $v0, 10 # 
  syscall # 

