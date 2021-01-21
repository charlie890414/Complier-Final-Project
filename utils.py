import enum

RESERVED_WORDS = ['Plus', 'Minus', 'Multiply', 'Divide',
                  'Modulus', 'Greater', 'Smaller', 'Equal', 'define', 'fun', 'if']

class Tree_type(enum.Enum):
    program = "program"
    plus = "plus"
    minus = "minus"
    multiply = "multiply"
    divide = "divide"
    modulus = "modulus"
    greater = "greater"
    smaller = "smaller"
    equal = "equal"
    def_stmt = "def_stmt"
    variable = "variable"
    fun_exp = "fun_exp"
    fun_call = "fun_call"
    fun_name = "fun_name"
    fun_ids = "fun_ids"
    fun_body = "fun_body"
    and_op = "and_op"
    or_op = "or_op"
    not_op = "not_op"
    if_exp = "if_exp"
    print_num = "print_num"
    print_bool = "print_bool"


class Token_type(enum.Enum):
    NOT_TOKEN = "NOT_TOKEN"
    NUMBER = "NUMBER"
    BOOL_VAL = "BOOL_VAL"
    ID = "ID"
