grammar c;

c: (line)* ;

line: ((declaration SEMICOLON)|(definition SEMICOLON)| (assignment SEMICOLON) | (bool1 SEMICOLON) | scope);

scope: LCURLYBRACE (line)* RCURLYBRACE;

definition: CONST? var_type IDENTIFIER EQUALS bool1;
declaration: CONST? var_type IDENTIFIER;

assignment: IDENTIFIER EQUALS bool1;
var_type: (INT_TYPE | FLOAT_TYPE | CHAR_TYPE | pointer_type);


EQUALS: '=';
CONST : 'const';
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
CHAR_TYPE: 'char';
IDENTIFIER: [a-zA-Z_][0-9a-zA-Z_]*;
pointer_type: (INT_TYPE | FLOAT_TYPE | CHAR_TYPE)'*';

bool1
    :bool2 ((AND|OR) bool2)*
    ;


bool2
    :NOT? LBRACKET bool1 RBRACKET
    |plus (EQ|LT|LE|GT|GE|NE) plus
    |plus
    ;


plus : (vm|) (operator2 (vm|neg_sol))*
     ;

vm   :
    mod (operator (mod | neg_sol))*
     ;

mod  :
    vm_sol (MOD (vm_sol | neg_sol))?
    ;

neg_sol
    :neg_value|(LBRACKET MIN LBRACKET plus RBRACKET RBRACKET) // 1+-3 not allowed 1+(-3) allowed
    ;

vm_sol
    : value
    | LBRACKET plus RBRACKET
    ;

neg_value
    :NEG_INT
    ;


value
    : INT
    | FLOAT
    | IDENTIFIER(MINMIN|PLUSPLUS)?
    | (MINMIN|PLUSPLUS)IDENTIFIER
    ;

operator: MAAL | DEEL;
operator2: PLUS | MIN ;

NEG_INT
    :LBRACKET('0'| (MIN?[1-9][0-9]*) )RBRACKET
    ;

INT
    : '0'
    | [1-9][0-9]*
    ;

FLOAT:
    [1-9][0-9]*('.'[0-9]+)
    ;

PLUS : '+';
PLUSPLUS : '++';
MIN  : '-';
MINMIN  : '--';
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
// empty : '' ;

WS : [ \n\t\r]+ -> skip;