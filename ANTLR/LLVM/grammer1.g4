grammar grammer1;

gram : line (SEMICOLON)+ (line (SEMICOLON)+)* ;

line : bool1

     //|  empty
     ;

bool1
    :bool2 ((AND|OR) bool2)*
    ;


bool2
    :NOT? LBRACKET bool1 RBRACKET
    |expr BINOP2 expr
    |expr
    ;

BINOP2
    :'=='
    |'>'
    |'<'
    |'>='
    |'<='
    |'!='
    ;


expr :
     | plus
     ;

plus : (vm|) ((PLUS|MIN) (vm|neg_sol))*
     ;

vm   :
    mod ((MAAL|DEEL) (mod | neg_sol))*
     ;

mod  :
    vm_sol (MOD (vm_sol | neg_sol))?
    ;

neg_sol
    :neg_value|(LBRACKET'-'LBRACKET plus RBRACKET RBRACKET)
    ;

vm_sol
    : value
    | LBRACKET plus RBRACKET
    ;

neg_value
    :NEG_INT
    ;


value
    :INT
    ;


NEG_INT
    :LBRACKET('0'| ('-'?[1-9][0-9]*) )RBRACKET
    ;

INT
    : '0'
    | [1-9][0-9]*
    ;


PLUS : '+';
MIN  : '-';
MAAL : '*';
DEEL : '/';
MOD  : '%';
SEMICOLON: ';';
LBRACKET: '(';
RBRACKET: ')';
NOT: '!';
AND: '&&';
OR: '||'

// empty : '' ;

WS : [ \n\t\r]+ -> skip;

// lege haakjes valid?