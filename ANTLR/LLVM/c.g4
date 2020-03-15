grammar c;

c: (line)* ;

line: ((definition SEMICOLON)| (assignment SEMICOLON) | (bool1 SEMICOLON)| (method_call SEMICOLON) | scope);


method_call: IDENTIFIER LBRACKET (args)? RBRACKET;

args :  bool1 (',' bool1)*;

scope: LCURLYBRACE (line)* RCURLYBRACE;

//declaration: CONST? var_type IDENTIFIER EQUALS bool1;
definition: CONST? var_type ((variable_identifier|assignment2)(','(variable_identifier|assignment2))*);

variable_identifier : IDENTIFIER;

assignment
    :lvalue EQUALS assignment
    |lvalue EQUALS bool1
    ;

assignment2
    :lvalue EQUALS assignment
    |lvalue EQUALS bool1
    ;

var_type: (INT_TYPE | FLOAT_TYPE | CHAR_TYPE | pointer_type);

increment
    :increment_var_first
    |increment_op_first
    ;

increment_var_first: IDENTIFIER(MINMIN|PLUSPLUS);

increment_op_first: (MINMIN|PLUSPLUS)IDENTIFIER;

EQUALS: '=';
CONST : 'const';
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
CHAR_TYPE: 'char';
IDENTIFIER: [a-zA-Z_][0-9a-zA-Z_]*;
pointer_type: (INT_TYPE | FLOAT_TYPE | CHAR_TYPE)'*';

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
    ;
lvalue
    :IDENTIFIER
    |MAAL IDENTIFIER
    |MAAL LBRACKET address RBRACKET
    ;

address
    :(INT(PLUS|MIN))*IDENTIFIER((PLUS|MIN)INT)*

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
    [1-9][0-9]*('.'[0-9]+)
    ;

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
INT
    : '0'
    | [1-9][0-9]*
    ;

CHAR: '\''[ -~]'\'';

// empty : '' ;

COMMENT1:('//'~('\n')* [\n]) -> skip ;
COMMENT2:('/*' (~('*')*'*')*'/') -> skip ;
WS : [ \n\t\r]+ -> skip;


