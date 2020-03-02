grammar grammer1;

gram : line (';')+ (line (';')+)* ;

line : bool1

     //|  empty
     ;

bool1
    :bool2 (BINOP bool2)*
    ;


bool2
    :'!'? '(' bool1 ')'
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

BINOP
    :'&&'
    |'||'
    ;

expr :
     | plus
     ;

plus : (vm|) (OPERATOR2 (vm|neg_sol))*
     ;

vm   :
    mod (OPERATOR (mod | neg_sol))*
     ;

mod  :
    vm_sol ('%' (vm_sol | neg_sol))?
    ;

neg_sol
    :neg_value|('(-(' plus '))')
    ;

vm_sol
    : value
    | '(' plus ')'
    ;

neg_value
    :NEG_INT
    ;


value
    :INT
    ;


NEG_INT
    :'('('0'| ('-'?[1-9][0-9]*) )')'
    ;

INT
    : '0'
    | [1-9][0-9]*
    ;

OPERATOR
    : '*'
    | '/'
    ;
OPERATOR2
    : '+'
    | '-'
    ;

// empty : '' ;

WS : [ \n\t\r]+ -> skip;

// lege haakjes valid?