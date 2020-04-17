# C Compiler

### Implemented Features (20/03/2020)
Assignment 1
- Binary operations+,-,*, and / 
- Binary operations >,<, and ==
- Unary operators + and -
- Brackets to overwrite the order of operations
- (optional) Binary operator %
- (optional) Comparison operators >=, <=, and !=
- (optional) Logical operators &&, ||, and !
- (optional) Constant folding

Assignment 2
- Types: char, int, float, char*, int*, float*
- Const keyword
- Variables
- Pointer operations * and &
- (optional) Identifier Operations: ++ and --
- (optional) Conversions (in LLVM and in Constant folding)

Errors (Assignment 2 continued) 
- Syntax Errors(throws a CSyntaxError Exception)
- Use of undefined or uninitialised variable (throws a UndeclaredVariable / UninitializedVariable Exception respectively)
- Redeclaration or redefinition of an existing variable (throws a DuplicateDeclaration Exception)
- Operations or assignments of incompatible types (throws a IncompatibleType Exception)
- Assignment to an rvalue (throws a CSyntaxError Exception)
- Assignment to a const variable (throws a ConstAssignment Exception)
- Division by zero (throws a ZeroDivisionError Exception)

Each exception also contains the line and position of the error.

Assignment 3 
- (Multiline & single line) Comments are skipped 
- Printf: for a single int, float or char (variable or literal)

Assignment 4
- if, else
- while, for, break, continue
- (optional) switch, case, default 
- (extra) do

Assignment 5
- Return, void
- Scopes
- Local and Global vars
- Functions
- Code after return, break is not generated

Assignment 6
- Arrays
- Import stdio: printf() and scanf()

### Requirements
Also make sure graphviz is installed on your system for AST dot output.

`sudo apt-get install graphviz`

`pip install -r requirements.txt`

### Project Structure
`AST.py`: AST Structure and visitor class.

`cCustomListener.py`: Generates the AST.

`cErrorListener.py`: Listens to ANTLR errors and throws syntax errors.

`compile.py`: Execution script.

`LLVM_CONVERTER.py`: Traverses the AST and generates LLVM code.

`symbolTables.py`: Data structure for symbol table.

`/ANTLR/LLVM/c.g4`: ANTLR grammar.


### Building ANLTR Classes
`build.sh`

This should create the ANTLR source files in `./ANTLR/LLVM`

### Compiling
`python compile.py [inputfile] [outputname]`

This generates `llvm-[outputname].ll` and a matching `[outputname]` binary.
The AST Tree can be viewed in `./output/output-[outputname].png`

It also compiles the `.ll` file using clang and runs the binary.
(Files that contain errors are not compiled)

### Testing
`python run_tests.py` or `test.sh`

NB: Om één of andere reden is na een enkele run van de tests soms `scope_1.c` 
en `char_casting.c` volledig corrupt en dus niet meer leesbaar door ons programma. 
Ondertussen kunnen we het niet meer reproduceren.

The AST trees of the test files can be viewed at `./src/tests/trees`. 

Also the `.ll` files are generated. They're compiled to binary using clang. And the binaries are executed. 
(Files that contain errors are not compiled.) These can be found in `./src/tests/llvm`

The expected output of our files can be found in `./ExpectedOutput`

### Benchmark
`python benchmark.py` runs all files in `./src/tests/benchmark1/CorrectCode` and `./src/tests/benchmark1/SemanticErrors`.
The expected output of these files can be found in `benchmark.py` 

### List of test files and contents


| File  | Tests |
| ------------- | ------------- |
| assignment_to_r_value.c         | definition, assignment to rvalue  |
| basic_definition.c              | definition  |
| basic_declaration.c             | declaration, assignment  |
| bool_testing.c                  | definition, boolean folding, print |
| char_casting.c                  | definition, boolean folding, print |
| char_folding.c                  | definition, char folding, print |
| const_assignment_error.c        | const definition, const assignment error |
| duplicate_declaration_error.c   | definition, duplicate declaration |
| folding.c                       | definition, assignment, folding ints and floats  |
| incompatible_type_error.c       | definition, pointers, pointer + pointer error |
| modulo.c                        | definition, assignment, modulo floats and ints, print |
| not_testing.c                   | definition, bool folding with not |
| pointers.c                      | definition, pointer  |
| pointer_dereference.c           | definition, pointer, & * unary operators, print  |
| scope_1.c                       | single scope test  |
| scope_empty.c                   | empty scope test  |
| scope_nested.c                  | Int addition, print(int), scopes  |
| syntax_error.c                  | Custom Syntax Error: `int;`   |
| syntax_error_1.c                | Custom Syntax Error: unfinished scope: `{` |
| unary_++.c                      | ++x, x++, print, definition  |
| unary_--.c                      | --x, x--, print, definition  |
| unary_magic.c                   | unary operators + and -  |
| undeclared_var_error.c          | not declared error  |
| uninitialised_var_error.c       | declaration, not initialised error  |

| Folder  | ifelse |
| ------------- | ------------- |

| File  | Tests |
| ------------- | ------------- |
| false.c         | else part of each if-statement  |
| false_true.c         |  else part of first, if part of second if-statement  |
| fancy_if_false.c         | put an assignmentline in the condition that is false  |
| fancy_if_true.c         |  put an assignmentline in the condition that is true |
| no_else.c         | if-statements without an else  |
| true_false.c         | if_statement that has a true condition (false in unreached else)|
| true_true.c         | if_statement that has a true condition  |

| Folder  | functions |
| ------------- | ------------- |
| File  | Tests |
| ------------- | ------------- |
| declaration_1.c         | a declaration of a function before it's definition  |
| declaration_2.c         | a declaration of a function after it's definition   |
| declaration_multi.c         | a large amount of declarations before and after the definition  |
| definition_after.c         | definition after main  |
| definition_only.c         | definition before main without declaration  |
| faculty.c         | the faculty function with 3 with unused arguments  |
| mult_definition.c         | multiple definitions of the same function (Error) |

| Folder  | loops |
| ------------- | ------------- |
| File  | Tests |
| ------------- | ------------- |
| break_error.c | break statement outside loop |
| continue_error.c | continue statement outside loop |
| do_while.c | do while loop one iteration |
| do_while_2.c | do while loop multiple iterations |
| for_continue.c | for loop, continue |
| loop.c | normal for loop, for loop break |
| loop_return.c | return statement in for loop |
| nested_break.c | break inside nested loop |
