from functools import reduce
from lark.tree import Tree
from lark.lexer import Token
from utils import *


class define():

    def __init__(self, argv, exp, vars={}, func={}):
        self.argv = argv.children
        self.exp = exp.children
        self.vars = vars
        self.func = func

    def __call__(self, argv, vars={}, func={}):

        vars = {**vars, **self.vars}
        func = {**func, **self.func}

        for i, j in zip(self.argv, argv):
            if isinstance(j, define):
                func[i] = j
            else:
                vars[i] = j

        for exp in self.exp[:-1]:
            traverse(exp, vars, func)

        return traverse(self.exp[-1], vars, func)


def converge(token, Type=None):

    if Type and Token_type(token.type) != Type:
        print(
            f"Type Error: Expect '{'number' if Type == Token_type.NUMBER else 'boolean'}' but got '{'number' if Type == Token_type(token.type) else 'boolean'}'.")
        exit()

    if Token_type(token.type) == Token_type.NUMBER:
        return int(token)

    if Token_type(token.type) == Token_type.BOOL_VAL:
        return True if token == '#t' else False


def visit(tree, vars={}, func={}):
    children = []

    for e in tree.children:
        if not isinstance(tree, Token):
            e = traverse(e, vars, func)
        children.append(e)

    return children


def traverse(tree, vars={}, func={}):

    if isinstance(tree, Token):
        if Token_type(tree.type) == Token_type.ID:
            if tree in vars:
                return vars[tree]
            else:
                print("Symbol not defined")
                exit()
        return tree

    if Tree_type(tree.data) == Tree_type.program:
        return visit(tree, vars, func)

    elif Tree_type(tree.data) == Tree_type.print_num:
        for node in visit(tree, vars, func):
            print(node)

    elif Tree_type(tree.data) == Tree_type.print_bool:
        for node in visit(tree, vars, func):
            print(node)

    elif Tree_type(tree.data) == Tree_type.plus:
        return Token(Token_type.NUMBER.value, reduce((lambda a, b: a + b), [converge(e, Token_type.NUMBER) for e in visit(tree, vars, func)]))

    elif Tree_type(tree.data) == Tree_type.minus:
        return Token(Token_type.NUMBER.value, reduce((lambda a, b: a - b), [converge(e, Token_type.NUMBER) for e in visit(tree, vars, func)]))

    elif Tree_type(tree.data) == Tree_type.multiply:
        return Token(Token_type.NUMBER.value, reduce((lambda a, b: a * b), [converge(e, Token_type.NUMBER) for e in visit(tree, vars, func)]))

    elif Tree_type(tree.data) == Tree_type.divide:
        return Token(Token_type.NUMBER.value, reduce((lambda a, b: a // b), [converge(e, Token_type.NUMBER) for e in visit(tree, vars, func)]))

    elif Tree_type(tree.data) == Tree_type.modulus:
        return Token(Token_type.NUMBER.value, reduce((lambda a, b: a % b), [converge(e, Token_type.NUMBER) for e in visit(tree, vars, func)]))

    elif Tree_type(tree.data) == Tree_type.and_op:
        return Token(Token_type.BOOL_VAL.value, '#t' if reduce((lambda a, b: True if a and b else False), [converge(e, Token_type.BOOL_VAL) for e in visit(tree, vars, func)]) else '#f')

    elif Tree_type(tree.data) == Tree_type.or_op:
        return Token(Token_type.BOOL_VAL.value, '#t' if reduce((lambda a, b: True if a or b else False), [converge(e, Token_type.BOOL_VAL) for e in visit(tree, vars, func)]) else '#f')

    elif Tree_type(tree.data) == Tree_type.not_op:
        return Token(Token_type.BOOL_VAL.value, '#t' if not converge(visit(tree, vars, func)[0], Token_type.BOOL_VAL) else '#f')

    elif Tree_type(tree.data) == Tree_type.greater:
        return Token(Token_type.BOOL_VAL.value, '#t' if reduce((lambda a, b: True if a > b else False), [converge(e, Token_type.NUMBER) for e in visit(tree, vars, func)]) else '#f')

    elif Tree_type(tree.data) == Tree_type.smaller:
        return Token(Token_type.BOOL_VAL.value, '#t' if reduce((lambda a, b: True if a < b else False), [converge(e, Token_type.NUMBER) for e in visit(tree, vars, func)]) else '#f')

    elif Tree_type(tree.data) == Tree_type.equal:
        return Token(Token_type.BOOL_VAL.value, '#t' if reduce((lambda a, b: True if a == b else False), [converge(e, Token_type.NUMBER) for e in visit(tree, vars, func)]) else '#f')

    elif Tree_type(tree.data) == Tree_type.if_exp:
        _if, _then, _else = tree.children
        return traverse(_then, vars, func) if converge(traverse(_if, vars, func), Token_type.BOOL_VAL) else traverse(_else, vars, func)

    elif Tree_type(tree.data) == Tree_type.def_stmt:
        [var, exp] = tree.children

        if isinstance(exp, Tree) and (Tree_type(exp.data) == Tree_type.fun_exp or Tree_type(exp.data) == Tree_type.fun_call):
            func[var] = traverse(exp, vars, func)
        else:
            vars[var] = traverse(exp, vars, func)

    elif Tree_type(tree.data) == Tree_type.fun_call:
        f = traverse(tree.children[0], vars, func)
        params = [traverse(el, vars, func) for el in tree.children[1:]]
        return f(params, vars, func)

    elif Tree_type(tree.data) == Tree_type.fun_exp:
        [argv, exp] = tree.children
        return define(argv, exp, vars, func)

    elif Tree_type(tree.data) == Tree_type.fun_name:
        if tree.children[0] in func:
            return func[tree.children[0]]
        else:
            print("Symbol not defined")
            exit()
