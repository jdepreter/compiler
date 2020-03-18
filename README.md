# C Compiler
### Requirements
Also make sure graphviz is installed on your system for AST dot output.

`pip install -r requirements.txt`

### Compiling
`python test.py [inputfile] `


### Testing
`python run_tests.py`

For testing syntax errors:
- syntax_error.txt
- syntax_error_1.txt

List of test files and contents


| File  | Tests |
| ------------- | ------------- |
| syntax_error.txt  | Custom Syntax Error: `int;`   |
| syntax_error_1.txt  | Custom Syntax Error: unfinished scope (`{`) |
| scope_nested.txt  | Int addition, print(int), scopes  |
| scope_empty.txt  | empty scope test  |
| scope_1.txt  | single scope test  |
| folding.txt | definition, assignment, folding ints and floats  |
| bool_testing.txt  | definition, boolean folding, print |
| basic_definition.txt  | definition  |
| basic_declaration.txt  | declaration, assignment  |
| unary_magic.txt  | unary operators + and -  |
| pointers.txt  | definition pointer  |
| unary_++.txt  | ++x, x++, print, definition  |
| unary_--.txt  | --x, x--, print, definition  |
| uninitialised_var_error.txt  | declaration, not initialised error  |
| undeclared_var_error.txt  | not declared error  |
| x  | x  |
| x  | x  |
