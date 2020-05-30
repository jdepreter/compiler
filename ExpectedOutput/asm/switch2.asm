.data


  str.0: .asciiz "Niet 2"
  str.1: .asciiz "%d"
  str.2: .asciiz ""
  str.3: .asciiz "Default"
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
  li $t0, 10 # 
  sw $t0, 0($sp) # 
  lw $t0, 0($sp) # 
  sw $t0, 4($sp) # Assigning to x
  addiu $sp, $sp, 4 # deallocate solve math
  addiu $sp, $sp, -4 # allocate space for instance of x
  lw $t0, 4($sp) # Put on top of stack load
  sw $t0, 0($sp) # Put on top of stack save
  lw $t0, 0($sp) # 
  addiu $sp, $sp, 4 # Deallocate solve math
  li $t1, 1 # 
  beq $t0, $t1, label0 # 
  li $t1, 2 # 
  beq $t0, $t1, label1 # 
  li $t1, 3 # 
  beq $t0, $t1, label2 # 
  li $t1, 4 # 
  beq $t0, $t1, label3 # 
j label4
 # 
j label0
 # 
label0: # 
j label1
 # 
label1: # 
  addiu $sp, $sp, -4 # Allocate space for $ra
  sw $ra, 0($sp) # 
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  # Call printf
  addiu $sp, $sp, -4 # Allocate space for rvalue
  la $a0, str.0 # 
  li $v0, 4 # 
  syscall # 
# Leaving Stack...
  addiu $sp, $sp, 4 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  # Exit printf
  addiu $sp, $sp, 4 # Deallocate space used for method call
j label2
 # 
label2: # 
j label3
 # 
label3: # 
  addiu $sp, $sp, -4 # Allocate space for $ra
  sw $ra, 0($sp) # 
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  # Call printf
  addiu $sp, $sp, -4 # Allocate space for rvalue
  addiu $sp, $sp, -4 # allocate space for instance of x
  lw $t0, 16($sp) # Put on top of stack load
  sw $t0, 0($sp) # Put on top of stack save
  la $a0, str.2 # 
  li $v0, 4 # 
  syscall # 
  lw $t0, 0($sp) # Load int for printing
  move $a0, $t0 # 
  li $v0, 1 # 
  syscall # 
  la $a0, str.2 # 
  li $v0, 4 # 
  syscall # 
# Leaving Stack...
  addiu $sp, $sp, 8 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  # Exit printf
  addiu $sp, $sp, 4 # Deallocate space used for method call
j label5
 # 
j label4
 # 
label4: # 
  addiu $sp, $sp, -4 # Allocate space for $ra
  sw $ra, 0($sp) # 
# Entering new stack...
  addiu $sp, $sp, -4 # Allocate mem for previous frame pointer
  sw $fp, 0($sp) # Save previous frame pointer on stack
  move $fp, $sp # Save current stack pointer in frame pointer
# Entered Stack
  # Call printf
  addiu $sp, $sp, -4 # Allocate space for rvalue
  la $a0, str.3 # 
  li $v0, 4 # 
  syscall # 
# Leaving Stack...
  addiu $sp, $sp, 4 # Deallocate stack
  lw $fp, 0($sp) # Load previous frame pointer
  addiu $sp, $sp, 4 # Deallocate space for old frame pointer
# Left stack
  # Exit printf
  addiu $sp, $sp, 4 # Deallocate space used for method call
j label5
 # 
label5: # 
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

