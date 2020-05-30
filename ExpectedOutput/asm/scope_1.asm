.data


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
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  addiu $sp, $sp, -4 # Allocate space for symbol: c
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 1 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  sw $t0, 4($sp) # Assigning to c
  addiu $sp, $sp, 4 # deallocate solve math
# Leaving Stack...
  addiu $sp, $sp, 4 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 0 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  addiu $sp, $sp, 4 # Deallocate space used for solve math
# Leaving Stack...
  addiu $sp, $sp, 0 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  sw $t0, 0($sp) # 
  li $v0, 10 # 
  syscall # 

