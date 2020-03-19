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

Each exception also contains the line and position of the error.

Assignment 3 
- (Multiline & single line) Comments are skipped 
- Printf: for a single int, float or char (variable or literal)

### Requirements
Also make sure graphviz is installed on your system for AST dot output.

`pip install -r requirements.txt`

### Building ANLTR Classes
`build.sh`

This should create the ANTLR source files in `./ANTLR/LLVM`

### Compiling
`python compile.py [inputfile] [outputname]`

This generates `llvm-[outputname].ll` and a matching `[outputname]` binary.
The AST Tree can be viewed in `./output/output-[outputname].png`

### Testing
`python run_tests.py` or `test.sh`

NB: Om één of andere reden is na een enkele run van de tests soms `scope_1.txt` 
en `char_casting.txt` volledig corrupt en dus niet meer leesbaar door ons programma. 
Ondertussen kunnen we het niet meer reproduceren.

### List of test files and contents


| File  | Tests |
| ------------- | ------------- |
| assignment_to_r_value.txt         | definition, assignment to rvalue  |
| basic_definition.txt              | definition  |
| basic_declaration.txt             | declaration, assignment  |
| bool_testing.txt                  | definition, boolean folding, print |
| char_casting.txt                  | definition, boolean folding, print |
| char_folding.txt                  | definition, char folding, print |
| const_assignment_error.txt        | const definition, const assignment error |
| duplicate_declaration_error.txt   | definition, duplicate declaration |
| folding.txt                       | definition, assignment, folding ints and floats  |
| incompatible_type_error.txt       | definition, pointers, pointer + pointer error |
| modulo.txt                        | definition, assignment, modulo floats and ints, print |
| not_testing.txt                   | definition, bool folding with not |
| pointers.txt                      | definition, pointer  |
| pointer_dereference.txt           | definition, pointer, & * unary operators, print  |
| scope_1.txt                       | single scope test  |
| scope_empty.txt                   | empty scope test  |
| scope_nested.txt                  | Int addition, print(int), scopes  |
| syntax_error.txt                  | Custom Syntax Error: `int;`   |
| syntax_error_1.txt                | Custom Syntax Error: unfinished scope: `{` |
| unary_++.txt                      | ++x, x++, print, definition  |
| unary_--.txt                      | --x, x--, print, definition  |
| unary_magic.txt                   | unary operators + and -  |
| undeclared_var_error.txt          | not declared error  |
| uninitialised_var_error.txt       | declaration, not initialised error  |
