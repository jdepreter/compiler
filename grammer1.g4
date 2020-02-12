grammar grammer1;

input : line (';')+ (line (';')+)* ;

line : expr|bool

     //|  empty
     ;

bool
    :bool2 (BINOP bool2)*
    ;


bool2
    :'!'? '(' bool ')'
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