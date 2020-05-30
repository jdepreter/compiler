.data


  str.0: .asciiz "%d %d"
  str.1: .asciiz ""
  str.2: .asciiz " "
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
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 2 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  addiu $sp, $sp, 4 # Deallocate space used for solve math
  addiu $sp, $sp, -8 # Allocate array for symbol x
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 1 # 
  sw $t0, 0($sp) # 
  lw $t1, 0($sp) # Move value to temp register
  addiu $sp, $sp, 4 # Deallocate index
  addiu $sp, $sp, -4 # Allocate for x
  la $t0, 8($sp) # Put address on top of stack load
  sw $t0, 0($sp) # Put address on top of stack save
  li $t7, 1 # Check that memory is in bounds
  blt $t7, $t1, seg # Check that memory is in bounds
  sub $t0, $t0, $t1 # Load address of array[index]
  sub $t0, $t0, $t1 # Load address of array[index]
  sub $t0, $t0, $t1 # Load address of array[index]
  sub $t0, $t0, $t1 # Load address of array[index]
  sw $t0, 0($sp) # Store address on stack
  move $t2, $t0 # $t0 will be overwritten be solve math
  addiu $sp, $sp, 4 # Deallocate space for x pointer
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 12 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  sw $t0, 0($t2) # Store value at dereferenced pointer
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 0 # 
  sw $t0, 0($sp) # 
  lw $t1, 0($sp) # Move value to temp register
  addiu $sp, $sp, 4 # Deallocate index
  addiu $sp, $sp, -4 # Allocate for x
  la $t0, 8($sp) # Put address on top of stack load
  sw $t0, 0($sp) # Put address on top of stack save
  li $t7, 1 # Check that memory is in bounds
  blt $t7, $t1, seg # Check that memory is in bounds
  sub $t0, $t0, $t1 # Load address of array[index]
  sub $t0, $t0, $t1 # Load address of array[index]
  sub $t0, $t0, $t1 # Load address of array[index]
  sub $t0, $t0, $t1 # Load address of array[index]
  sw $t0, 0($sp) # Store address on stack
  move $t2, $t0 # $t0 will be overwritten be solve math
  addiu $sp, $sp, 4 # Deallocate space for x pointer
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 4 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  sw $t0, 0($t2) # Store value at dereferenced pointer
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 0 # 
  sw $t0, 0($sp) # 
  lw $t1, 0($sp) # Move value to temp register
  addiu $sp, $sp, 4 # Deallocate index
  addiu $sp, $sp, -4 # Allocate for x
  la $t0, 8($sp) # Put address on top of stack load
  sw $t0, 0($sp) # Put address on top of stack save
  li $t7, 1 # Check that memory is in bounds
  blt $t7, $t1, seg # Check that memory is in bounds
  sub $t0, $t0, $t1 # Load address of array[index]
  sub $t0, $t0, $t1 # Load address of array[index]
  sub $t0, $t0, $t1 # Load address of array[index]
  sub $t0, $t0, $t1 # Load address of array[index]
  sw $t0, 0($sp) # Store address on stack
  move $t2, $t0 # $t0 will be overwritten be solve math
  addiu $sp, $sp, 4 # Deallocate space for x pointer
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 14 # 
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
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 0 # 
  sw $t0, 0($sp) # 
  lw $t1, 0($sp) # Move value to temp register
  addiu $sp, $sp, 4 # Deallocate index
  addiu $sp, $sp, -4 # Allocate for x
  la $t0, 20($sp) # Put address on top of stack load
  sw $t0, 0($sp) # Put address on top of stack save
  li $t7, 1 # Check that memory is in bounds
  blt $t7, $t1, seg # Check that memory is in bounds
  sub $t0, $t0, $t1 # Load address of array[index]
  sub $t0, $t0, $t1 # Load address of array[index]
  sub $t0, $t0, $t1 # Load address of array[index]
  sub $t0, $t0, $t1 # Load address of array[index]
  sw $t0, 0($sp) # Store address on stack
  lw $t0, 0($sp) # Load value of pointer in $t0 1
  lw $t0, 0($t0) # Load value of pointer in $t0 2
  sw $t0, 0($sp) # Load value of pointer in $t0 2
  addiu $sp, $sp, -4 # Allocate space for rvalue
  li $t0, 1 # 
  sw $t0, 0($sp) # 
  lw $t1, 0($sp) # Move value to temp register
  addiu $sp, $sp, 4 # Deallocate index
  addiu $sp, $sp, -4 # Allocate for x
  la $t0, 24($sp) # Put address on top of stack load
  sw $t0, 0($sp) # Put address on top of stack save
  li $t7, 1 # Check that memory is in bounds
  blt $t7, $t1, seg # Check that memory is in bounds
  sub $t0, $t0, $t1 # Load address of array[index]
  sub $t0, $t0, $t1 # Load address of array[index]
  sub $t0, $t0, $t1 # Load address of array[index]
  sub $t0, $t0, $t1 # Load address of array[index]
  sw $t0, 0($sp) # Store address on stack
  lw $t0, 0($sp) # Load value of pointer in $t0 1
  lw $t0, 0($t0) # Load value of pointer in $t0 2
  sw $t0, 0($sp) # Load value of pointer in $t0 2
  la $a0, str.1 # 
  li $v0, 4 # 
  syscall # 
  lw $t0, 4($sp) # Load int for printing
  move $a0, $t0 # 
  li $v0, 1 # 
  syscall # 
  la $a0, str.2 # 
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
  addiu $sp, $sp, 12 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  # Exit printf
  addiu $sp, $sp, 4 # Deallocate space used for method call
# Leaving Stack...
  addiu $sp, $sp, 8 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
# Left stack
  addiu $sp, $sp, -4 # Space for return value
  li $t0, 0 # 
  sw $t0, 0($sp) # 

