grammar c;

c: (line)* ;

line: ((definition SEMICOLON)|(method_declaration SEMICOLON)| method_definition| line_no_def | include);

line_no_def: (assignment_line SEMICOLON) | ifelse | for_loop | while_loop | scope |switchcase | break_line | continue_line | return_line;

include: '#include''<' 'stdio.h''>';

scope: LCURLYBRACE (line)* RCURLYBRACE;

ifelse : IF LBRACKET condition RBRACKET line_no_def
(ELSE line_no_def)?;

for_loop : FOR LBRACKET for_initial SEMICOLON condition SEMICOLON for_update RBRACKET
        line_no_def;

while_loop : (WHILE LBRACKET condition RBRACKET line_no_def)
            | do_block WHILE LBRACKET condition RBRACKET SEMICOLON;

for_initial : (definition | );
condition : assignment_line;
for_update : assignment_line;
break_line : BREAK SEMICOLON;
continue_line : CONTINUE SEMICOLON;
do_block : DO line_no_def;
return_line :RETURN (bool1)? SEMICOLON;

switchcase: SWITCH LBRACKET bool1 RBRACKET LCURLYBRACE
(case|default)*
RCURLYBRACE;

case:(CASE (INT|CHAR) ':' line*) ;
default : DEFAULT ':'line*;

method_declaration:((CONST? var_type)|VOID)IDENTIFIER LBRACKET (def_args)? RBRACKET ;

method_definition: ((CONST? var_type)|VOID)IDENTIFIER LBRACKET (def_args)? RBRACKET scope;

def_args: arg_definition (',' arg_definition)*;

arg_definition : CONST? var_type IDENTIFIER;

method_call: IDENTIFIER LBRACKET (args)? RBRACKET;

args :  assignment_line (',' assignment_line)*;

//declaration: CONST? var_type IDENTIFIER EQUALS bool1;
definition: CONST? var_type ((variable_identifier|assignment2|array)(','(variable_identifier|assignment2|array))*);

// het ding tussen [] moet een int zijn
array : variable_identifier SLBRACKET assignment_line SRBRACKET ;

variable_identifier : IDENTIFIER;

assignment_line
    : (assignment | bool1)(COMMA (assignment | bool1))*
    ;

assignment
    :lvalue EQUALS assignment
    |lvalue EQUALS bool1
    |array EQUALS assignment
    |array EQUALS bool1
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

increment_var_first: lvalue(MINMIN|PLUSPLUS);

increment_op_first: (MINMIN|PLUSPLUS)lvalue;


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
    : increment
    | lvalue
    | rvalue
    ;
rvalue
    :INT
    |FLOAT
    |CHAR
    |STRING
    |AMPERSAND IDENTIFIER
    |method_call
    ;
lvalue
    : LBRACKET lvalue RBRACKET
    | IDENTIFIER (SLBRACKET assignment_line SRBRACKET)*
    | dereference
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

VOID: 'void';
RETURN:'return';
IF : 'if';
ELSE : 'else';
FOR : 'for';
WHILE : 'while';
DO: 'do';
SWITCH: 'switch';
CASE: 'case';
DEFAULT: 'default';
BREAK: 'break';
CONTINUE: 'continue';
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
SLBRACKET: '[';
SRBRACKET: ']';
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
STRING: '"' ~('"')* '"';
//STRING : '"' CHAR_NO_NL* '"';
//fragment CHAR_NO_NL : 'a'..'z'| 'A'..'Z' | '\t'| '\\' | '\n' | EOF;
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


