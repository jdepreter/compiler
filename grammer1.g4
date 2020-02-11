grammar grammer1;

input : (';')* line (';')+ (line (';')+)* ;

line :  expr
     //|  empty
     ;

expr :  INT
     |  plus (OPERATOR | OPERATOR2) '(' expr ')' ((OPERATOR|OPERATOR2) expr )*
     |  plus
     ;

plus : vm (OPERATOR2 plus)*
     | vm
     ;

vm   : INT
     | INT (OPERATOR vm)*
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