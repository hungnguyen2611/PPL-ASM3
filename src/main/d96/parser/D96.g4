// my ID: 1952737

grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}


/**
 *  2. Program structure
 *  only one special method 'main' in the Program
 *  class Program is the entry of the program
 */
 // A D96 program consists of many class declarations
program: class_declare+  EOF;


// 2.1. Class declaration
// other classes
class_declare: CLASS (ID) (COLON (ID))? LB class_body* RB;


// 2.2. Attribute declaration

att_declare: (VAR|VAL) mixed_list COLON type_name (ASSIGN exp_list)? SEMI;

//att_declare: att_declare_with_asm | att_declare_with_no_asm ;
//
//att_declare_with_no_asm: ((VAR|VAL) mixed_list COLON type_name SEMI);
//
//att_declare_with_asm: ((VAR|VAL) member_id midside exp SEMI);
//midside: COLON type_name ASSIGN
//        | COMMA member_id midside exp COMMA
//        ;
//
mixed_list: member_id (COMMA member_id)* ;

member_id: (ID|DOLLARID) ;




method_declare: member_id LP param_list? RP LB body RB
            | constructor_declare
            | destructor_declare ;

constructor_declare: CONSTRUCTOR LP param_list? RP LB cons_des_body RB ;

destructor_declare: DESTRUCTOR LP RP LB cons_des_body RB ;

//////////////////////////////////////

class_body: (att_declare|method_declare) ;

body: stmt* ;

cons_des_body: cons_des_stmt* ;
param_list: id_list_with_type (SEMI id_list_with_type)* ;  // abc, def : Int; str: String

id_list_with_type: ids_list COLON type_name ;

ids_list : (ID) (COMMA (ID))* ;

type_name:  primitive_type | arr_type | (ID);

primitive_type: INT | FLOAT | BOOLEAN | STRING ;

// for array type
arr_type: ARRAY LSB type_name COMMA INTEGER_LITERAL RSB ;


// statements

cons_des_stmt: var_declare
            |assignment
            |if_stmt
            |for_stmt
            |break_stmt
            |continue_stmt
            |return_stmt
            |method_invoc_stmt
            |block_stmt;
stmt: var_declare
    |assignment
    |if_stmt
    |for_stmt
    |break_stmt
    |continue_stmt
    |return_stmt
    |method_invoc_stmt
    |block_stmt
    ;
var_declare: (VAR|VAL) ID (COMMA ID)* COLON type_name (ASSIGN exp_list)? SEMI;
//var_declare: var_declare_with_asm
//            | var_declare_with_no_asm
//            ;
//
//var_declare_with_no_asm: (VAR|VAL) ids_list COLON type_name SEMI;
//
//var_declare_with_asm: ((VAR|VAL) var_id mid exp SEMI);
//
//mid: COLON type_name ASSIGN
//        | COMMA var_id mid exp COMMA
//        ;
//var_id: (ID) ;

assignment: assign_lhs ASSIGN assign_rhs SEMI;

assign_lhs: (ID|DOLLARID)
        |   operands index
        | exp DOT ID
        | ID DOUBLECOLON DOLLARID
        | exp
        ;

assign_rhs: exp;

// if statement
if_stmt: IF LP exp RP block_stmt elseif_stmt* else_stmt?;

elseif_stmt: ELSEIF LP exp RP block_stmt;
else_stmt: ELSE block_stmt ;

// for statement

for_stmt: FOREACH LP (ID|DOLLARID) IN exp DOTDOT exp (BY exp)? RP block_stmt;

// break/continue/return statement
break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

return_stmt: RETURN exp? SEMI;

// method invocation

method_invoc_stmt: exp DOT instance_method SEMI
                |ID DOUBLECOLON static_method  SEMI
                ;

// block statement
block_stmt: LB stmt* RB;





relational: EQ | NEQ | LT | GT | LTE | GTE ;

// expression
exp: exp1 (CONCATSTR|EQSTR) exp1 | exp1 ;
exp1: exp2 relational exp2 | exp2 ;
exp2: exp2 (AND|OR) exp3 | exp3;
exp3: exp3 (ADD|SUB) exp4 | exp4;
exp4: exp4 (MUL|DIV|MODULO) exp5 | exp5;
exp5: NOT exp5 | exp6 ;
exp6: SUB exp6 | exp7 ;
exp7: exp7 index | exp8;
exp8: exp8 DOT exp9| exp9;
exp9: exp9 DOUBLECOLON exp10| exp10 ;
exp10: NEW exp10 | operands ;



operands: literal
        | instance_method
        | static_method
        | index
//        | static_invoc_exp
//        | instance_invoc_exp
        | obj_create
        | LP exp RP
        | (ID|DOLLARID)
        ;






// to reference or extract selected elements of an array
index: LSB exp RSB index
    | LSB exp RSB;  // [exp][exp]...

instance_method: ID LP exp_list? RP;
static_method: DOLLARID LP exp_list? RP;

//instance_invoc_exp: (SELF|ID) DOT (ID|instance_method) ;
//static_invoc_exp: ID DOUBLECOLON (DOLLARID|static_method) ;

obj_create: ID LP exp_list? RP;
exp_list: (exp COMMA)* exp;



literal: INTEGER_LITERAL
        | ZERO_INTLIT
        | FLOAT_LITERAL
        | STRING_LITERAL
        | array_literal
        | boolean_literal
        | SELF
        | NULL
        ;



/**
 * Keywords
 */

// Class, attribute, methods
CLASS   : 'Class' ;
fragment STATIC  : '$' ;
SELF: 'Self' ;

// Stop Statement
BREAK   : 'Break' ;
CONTINUE: 'Continue' ;
RETURN: 'Return';

// Flow Statement
IF      : 'If' ;
ELSEIF  : 'Elseif' ;
ELSE    : 'Else' ;


// Loop Statement
FOREACH : 'Foreach' ;
IN      : 'In' ;

// value
TRUE    : 'True' ;
FALSE   : 'False' ;
NULL    : 'Null' ;


// data type
INT     : 'Int' ;
FLOAT   : 'Float' ;
BOOLEAN : 'Boolean' ;
STRING  : 'String' ;
ARRAY   : 'Array' ;


// Constructor, Destructor
CONSTRUCTOR  : 'Constructor' ;
DESTRUCTOR   : 'Destructor' ;

//
NEW      : 'New' ;
BY       : 'By'  ;
//
VAR     : 'Var' ;
VAL     : 'Val' ;


// Operators


// Boolean
NOT   : '!' ;
AND   : '&&' ;
OR    : '||' ;
EQSTR : '==.' ;

// String
CONCATSTR: '+.' ;
// Arithmetic
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MODULO: '%' ;

// Relational
EQ    : '==' ;
NEQ   : '!=' ;
LT : '<' ;
GT : '>' ;
LTE: '<=';
GTE: '>=';


ASSIGN: '=' ;




// Seperators
LP: '(';

RP: ')';

LB: '{';

RB: '}';

SEMI: ';';

COLON: ':';

COMMA: ',';

DOTDOT: '..' ;

DOT: '.' ;


DOUBLECOLON: COLON COLON ;
fragment UNDERLINE: '_' ;

LSB: '['; // Left Square Bracket

RSB: ']'; // Right Square Bracket

/**
 * Literals
 */

// boolean
boolean_literal    : TRUE | FALSE ;


// integer
INTEGER_LITERAL    :  (DEC | OCT | HEX | BIN)
                    {
                        self.text = self.text.replace('_', '')
                    }
                    ;
ZERO_INTLIT         : '0' | '00' | '0' [Bb] '0' | '0' [Xx] '0' ;
// base-n literal
fragment DEC                : ([1-9] (UNDERLINE? DIGIT)*) ;
                                                  // 1 | 1_2 | 123_23_1
fragment Decwithzero        : DIGIT+ ;

fragment OCT                : [0] [1-7](UNDERLINE? [0-7])* ;
                                                       // 00 | 012 | 067
fragment HEX                : [0][Xx][1-9A-F](UNDERLINE? [0-9A-F])* ;
                                                       // 0x12 | 0X45 | 0xCAFE
fragment BIN                : [0][Bb][1](UNDERLINE? [01])* ;
                                                       // 0b0101 | 0B1101

FLOAT_LITERAL      : ((DEC|'0') DEC_PART EXPONENTIAL?      // 1. | 1.05 | 1.e-4 | 1.25e-5 | 0.04
	                | DEC_PART EXPONENTIAL          // .5e-4
	                | (DEC|'0') EXPONENTIAL)               // 12e-5
	                {
                        self.text = self.text.replace('_', '')
                    }
                    ;

STRING_LITERAL     : (["] STRCHAR* ["])
                    {
                        self.text = self.text[1:-1]
                    };



// Array(1,2,3,4)
array_literal          : ARRAY LP array_literal (COMMA array_literal)* RP
                        | ARRAY LP exp_list? RP ;


fragment EXPONENTIAL         : [eE] SIGN?  Decwithzero ;
fragment DEC_PART            : DOT Decwithzero? ;

fragment DIGIT: [0-9];



fragment SIGN               : [-+] ;

ID: [a-zA-Z_][a-zA-Z_0-9]* ;
DOLLARID: STATIC [a-zA-Z_0-9]+;             // may be static or non-static


// Skip comments
COMMENT: ('##' .*? '##') -> skip ;

WS: [ \t\r\n]+ -> skip;         // skip spaces, tabs, newlines


fragment STRCHAR    : ESC_SEQ | ([']["]) | ~[\n\\"];

fragment ESC_SEQ    : '\\' [btnfr'\\];

fragment ESC_ILLEGAL: '\\' ~[btnfr'\\];

UNCLOSE_STRING: ["] STRCHAR* ([\n] | EOF)
                    {
                        y = str(self.text)
                        if y[-1] == '\n':
                            raise UncloseString(y[1:-2])
                        else:
                            raise UncloseString(y[1:])
                    }
                    ;

ILLEGAL_ESCAPE: ["] STRCHAR* ESC_ILLEGAL
                    {
                        y = str(self.text)
                        raise IllegalEscape(y[1:])
                    }
                    ;

ERROR_CHAR: .
        {
            raise ErrorToken(self.text)
        }
        ;

