grammar C_gram;

gram: line*;

line: if_statement| forloop| whileloop|assignment;

if_statement:IF LBRACKET bool1 RBRACKET ((OPENC gram CLOSEC)|line) (ELSE ((OPENC gram CLOSEC)|line))?;
whileloop: (WHILE LBRACKET bool1 RBRACKET ((OPENC gram CLOSEC)|line))|(DO ((OPENC gram CLOSEC)|line)WHILE LBRACKET bool1 RBRACKET );
forloop: FOR LBRACKET *ENTER* RBRACKET ((OPENC gram CLOSEC)|line);
assignment: CAST VARIABLENAME EQUAL bool1;




CAST: 'int';
VARIABLENAME: [a-zA-Z][a-zA-Z1-9]*;
SEMICOLON: ';';
EQUAL: '=';
LBRACKET: '(';
RBRACKET: ')';
OPENC: '{';
CLOSEC: '}';
IF: 'if';
ELSE: 'else';
FOR:'for';
WHILE: 'while';
DO: 'do';

bool1:;
