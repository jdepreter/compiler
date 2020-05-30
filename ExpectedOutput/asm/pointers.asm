.data
  fp0: .float 6.0


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
  li $t0, 5 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  sw $t0, 4($sp) # Assigning to x
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for symbol: y
  addiu $sp, $sp, -4 # Allocate space for rvalue
  la $t0, 8($sp) # Load address of x
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  sw $t0, 4($sp) # Assigning to y
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for symbol: a
  addiu $sp, $sp, -4 # Allocate space for rvalue
  l.s $f0 fp0 # 
  swc1 $f0, 0($sp) # 
  lwc1 $f0, 0($sp) # 
  swc1 $f0, 4($sp) # Assigning to a
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for symbol: b
  addiu $sp, $sp, -4 # Allocate space for rvalue
  la $t0, 8($sp) # Load address of a
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  sw $t0, 4($sp) # Assigning to b
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for symbol: c
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 32 # 
  sb $t0, 0($sp) # 
  lb $t0, 0($sp) # 
  sb $t0, 4($sp) # Assigning to c
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for symbol: d
  addiu $sp, $sp, -4 # Allocate space for rvalue
  la $t0, 8($sp) # Load address of c
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  sw $t0, 4($sp) # Assigning to d
  addiu $sp, $sp, 4 # deallocate solve math
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

