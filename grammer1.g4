grammar grammer1;

input : line (';')+ (line (';')+)* ;

line :  expr
     //|  empty
     ;

expr :  INT
     |  '(' expr ')'
     |  plus
     ;

plus : INT (OPERATOR2 expr)*
     | vm
     ;

vm   : INT
     | INT (OPERATOR expr)*
     ;


INT
    : '0'
    | '-'?[1-9][0-9]*
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