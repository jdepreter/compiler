.data


  str.0: .asciiz "%c"
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
  addiu $sp, $sp, -4 # Allocate space for symbol: c
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 100 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  sb $t0, 4($sp) # Assigning to c
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
  lb $t0, 16($sp) # Put on top of stack load
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

