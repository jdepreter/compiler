grammar grammer1;

input : line ';' (line ';')* ;

line :  expr
     //|  empty
     ;

expr :  INT
     |  '(' expr ')'
     |  INT (OPERATOR expr)*
     ;

INT
    : '0'
    | '-'?[1-9][0-9]*
    ;

OPERATOR
    : '+'
    | '-'
    | '*'
    | '/'
    ;

// empty : '' ;

WS : [ \n\t\r]+ -> skip;

// lege haakjes valid?