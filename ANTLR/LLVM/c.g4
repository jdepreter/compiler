grammar c;

c: (line)* ;

line: ((definition SEMICOLON)| line_no_def);

line_no_def: (assignment_line SEMICOLON) | (bool1 SEMICOLON)| ifelse | for_loop | while_loop | scope |switchcase | break_line;

scope: LCURLYBRACE (line)* RCURLYBRACE;

ifelse : IF LBRACKET condition RBRACKET line_no_def
(ELSE line_no_def)?;

for_loop : FOR LBRACKET for_initial SEMICOLON condition SEMICOLON for_update RBRACKET
        line_no_def;

while_loop : (WHILE LBRACKET condition RBRACKET line_no_def)
            | do_block WHILE LBRACKET condition RBRACKET SEMICOLON;

for_initial : (definition | );
condition : (bool1 | assignment_line | );
for_update : (bool1 | assignment_line | );
break_line : BREAK SEMICOLON;
do_block : DO line_no_def;

switchcase: SWITCH LBRACKET value RBRACKET LCURLYBRACE
(CASE (INT|FLOAT|CHAR) ':' line_no_def*)*
DEFAULT ':'line_no_def*
RCURLYBRACE;

method_call: IDENTIFIER LBRACKET (args)? RBRACKET;

args :  bool1 (',' bool1)*;

//declaration: CONST? var_type IDENTIFIER EQUALS bool1;
definition: CONST? var_type ((variable_identifier|assignment2)(','(variable_identifier|assignment2))*);

variable_identifier : IDENTIFIER;

assignment_line
    : assignment(COMMA assignment)*
    ;

assignment
    :lvalue EQUALS assignment
    |lvalue EQUALS bool1
    ;

assignment2
    :IDENTIFIER EQUALS assignment
    |IDENTIFIER EQUALS bool1
    ;

var_type: (pointer_type | INT_TYPE | FLOAT_TYPE | CHAR_TYPE);

increment
    :increment_var_first
    |increment_op_first
    ;

increment_var_first: IDENTIFIER(MINMIN|PLUSPLUS);

increment_op_first: (MINMIN|PLUSPLUS)IDENTIFIER;


pointer_type: (INT_TYPE | FLOAT_TYPE | CHAR_TYPE)MAAL+;

bool1
    :bool2 (boolop bool2)*
    ;


bool2
    : not_value? LBRACKET bool1 RBRACKET
    | plus (EQ|LT|LE|GT|GE|NE) plus
    | plus
    ;

boolop
    :AND
    |OR;

not_value:
NOT;

plus : vm (operator2 (vm|neg_sol))*
     ;

vm   :
    mod (operator (mod | neg_sol))*
     ;

mod  :
    vm_sol (MOD (vm_sol | neg_sol))?
    ;

neg_sol
    :(LBRACKET MIN LBRACKET plus RBRACKET RBRACKET) // 1+-3 not allowed 1+(-3) allowed
    ;

vm_sol
    : value
    | unary_min
    | unary_plus
    | LBRACKET bool1 RBRACKET
    ;

value
    : lvalue
    | rvalue
    | increment
    ;
rvalue
    :INT
    |FLOAT
    |CHAR
    |AMPERSAND IDENTIFIER
    |method_call
    ;
lvalue
    :IDENTIFIER
    |dereference
    ;

dereference
    :MAAL+ IDENTIFIER
    |MAAL+ LBRACKET address RBRACKET
    ;

address
    :(INT(PLUS))*IDENTIFIER((PLUS|MIN)INT)*
    ;

operator: MAAL | DEEL;
operator2: PLUS | MIN ;

unary_min : MIN value
          | MIN unary_plus
          | MIN LBRACKET bool1 RBRACKET
          ;
unary_plus : PLUS value
           | PLUS unary_min
           | PLUS LBRACKET bool1 RBRACKET
           ;

FLOAT:
    [1-9][0-9]*('.'[0-9]+) | '0.'[0-9]+
    ;

IF : 'if';
ELSE : 'else';
FOR : 'for';
WHILE : 'while';
DO: 'do';
SWITCH: 'switch';
CASE: 'case';
DEFAULT: 'default';
BREAK: 'break';
AMPERSAND: '&';
PLUSPLUS : '++';
PLUS : '+';
MINMIN  : '--';
MIN  : '-';
MAAL : '*';
DEEL : '/';
MOD  : '%';
SEMICOLON: ';';
LBRACKET: '(';
RBRACKET: ')';
NOT: '!';
AND: '&&';
OR: '||';
EQ: '==';
GT: '>';
LT: '<';
NE: '!=';
GE:'>=';
LE:'<=';
LCURLYBRACE:'{';
RCURLYBRACE: '}';
COMMA: ',';
INT
    : '0'
    | [1-9][0-9]*
    ;

CHAR: '\''[ -~]'\'';
EQUALS: '=';
CONST : 'const';
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
CHAR_TYPE: 'char';
IDENTIFIER: [a-zA-Z_][0-9a-zA-Z_]*;

// empty : '' ;

COMMENT1:('//'~('\n')* [\n]) -> skip ;
COMMENT2:('/*' (~('*')*'*')*'/') -> skip ;
WS : [ \n\t\r]+ -> skip;


