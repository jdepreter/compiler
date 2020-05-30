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
  addiu $sp, $sp, -4 # Allocate space for symbol: i
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 5 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  sw $t0, 4($sp) # Assigning to i
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for symbol: j
  addiu $sp, $sp, -4 # Allocate space for rvalue
  la $t0, 8($sp) # Load address of i
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  sw $t0, 4($sp) # Assigning to j
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for symbol: x
  addiu $sp, $sp, -4 # Allocate space for rvalue
  la $t0, 8($sp) # Load address of j
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  sw $t0, 4($sp) # Assigning to x
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Space for dereferenced value
  la $t0, 4($sp) # Dereference once
  lw $t0, 0($t0) # Dereference once
  lw $t0, 0($t0) # Dereference once
  move $t2, $t0 # $t0 will be overwritten be solve math
  addiu $sp, $sp, 4 # Deallocate space for dereferenced value
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 3 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  sw $t0, 0($t2) # Store value at dereferenced pointer
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
  addiu $sp, $sp, -4 # allocate space for instance of **x
  la $t0, 16($sp) # Dereference once
  lw $t0, 0($t0) # Dereference once
  lw $t0, 0($t0) # Dereference once
  sw $t0, 0($sp) # store reference value on top
  lw $t0, 0($sp) # Load value of pointer in $t0 1
  lw $t0, 0($t0) # Load value of pointer in $t0 2
  sw $t0, 0($sp) # Load value of pointer in $t0 2
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

