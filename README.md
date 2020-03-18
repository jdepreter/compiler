# C Compiler
### Requirements
Also make sure graphviz is installed on your system for AST dot output.

`pip install -r requirements.txt`

### Compiling
`python test.py [inputfile] `


### Testing
`python run_tests.py`

NB: Om één of andere reden is na een enkele run van de tests `scope_1.txt` 
en `char_casting.txt` volledig corrupt en dus niet meer leesbaar door ons programma. 

###List of test files and contents


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
| pointers.txt                      | definition pointer  |
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
