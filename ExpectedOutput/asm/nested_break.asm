.data


  str.0: .asciiz "%d"
  str.1: .asciiz ""
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
  addiu $sp, $sp, -4 # Allocate space for symbol: x
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 1 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  sw $t0, 4($sp) # Assigning to x
  addiu $sp, $sp, 4 # deallocate solve math
j for_condition0
 # 
for_condition0: # 
  addiu $sp, $sp, -4 # allocate space for instance of x
  lw $t0, 4($sp) # Put on top of stack load
  sw $t0, 0($sp) # Put on top of stack save
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 10 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  lw $t1, 4($sp) # 
  slt $t0, $t1, $t0 # 
  addiu $sp, $sp, 4 # Deallocate right operand
  sw $t0, 0($sp) # Overwrite left operand
  lw $t0, 0($sp) # 
  addiu $sp, $sp, 4 # Deallocate space used for solve math
  beq $t0, $0, for_end0 # 
j for_block0
 # 
for_update0: # 
  addiu $sp, $sp, -4 # allocate space for instance of x
  lw $t0, 4($sp) # Put on top of stack load
  sw $t0, 0($sp) # Put on top of stack save
  addi $t0, $t0, 1 # 
  sw $t0, 4($sp) # 
  lw $t0, 0($sp) # 
  addiu $sp, $sp, 4 # Deallocate space used for solve math
j for_condition0
 # 
for_block0: # 
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  addiu $sp, $sp, -4 # Allocate space for symbol: y
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 1 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  sw $t0, 4($sp) # Assigning to y
  addiu $sp, $sp, 4 # deallocate solve math
j for_condition1
 # 
for_condition1: # 
  addiu $sp, $sp, -4 # allocate space for instance of y
  lw $t0, 4($sp) # Put on top of stack load
  sw $t0, 0($sp) # Put on top of stack save
  addiu $sp, $sp, -4 # allocate space for instance of x
  lw $t0, 16($sp) # Put on top of stack load
  sw $t0, 0($sp) # Put on top of stack save
  lw $t0, 0($sp) # 
  lw $t1, 4($sp) # 
  slt $t0, $t1, $t0 # 
  addiu $sp, $sp, 4 # Deallocate right operand
  sw $t0, 0($sp) # Overwrite left operand
  lw $t0, 0($sp) # 
  addiu $sp, $sp, 4 # Deallocate space used for solve math
  beq $t0, $0, for_end1 # 
j for_block1
 # 
for_update1: # 
  addiu $sp, $sp, -4 # allocate space for instance of y
  lw $t0, 4($sp) # Put on top of stack load
  sw $t0, 0($sp) # Put on top of stack save
  addi $t0, $t0, 1 # 
  sw $t0, 4($sp) # 
  lw $t0, 0($sp) # 
  addiu $sp, $sp, 4 # Deallocate space used for solve math
j for_condition1
 # 
for_block1: # 
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  addiu $sp, $sp, -4 # allocate space for instance of y
  lw $t0, 8($sp) # Put on top of stack load
  sw $t0, 0($sp) # Put on top of stack save
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 3 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  lw $t1, 4($sp) # 
  sgt $t0, $t1, $t0 # 
  addiu $sp, $sp, 4 # Deallocate right operand
  sw $t0, 0($sp) # Overwrite left operand
  lw $t0, 0($sp) # 
  addiu $sp, $sp, 4 # Deallocate space used for solve math
  beq $t0, $0, Else2 # 
# Leaving Stack...
  addiu $sp, $sp, 0 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
j for_end1
 # 
Else2: # 
Endif2: # 
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
# Leaving Stack...
  addiu $sp, $sp, 0 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
j for_update1
 # 
for_end1: # 
# Leaving Stack...
  addiu $sp, $sp, 4 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
j for_update0
 # 
for_end0: # 
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

