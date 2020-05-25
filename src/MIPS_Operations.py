optype = {
    'int': {
            '+': 'add',
            '++': 'addi',
            '-': 'sub',
            '--': 'subi',
            '*': 'mul',
            '/': 'div',
            '%': 'div'
    },
    'char': {
        '+': 'add',
        '++': 'addi',
        '-': 'sub',
        '--': 'subi',
        '*': 'mul',
        '/': 'div',
        '%': 'div'
    },
    'float': {
        '+': 'add.s',
        '++': 'add.s',
        '-': 'sub.s',
        '--': 'sub.s',
        '*': 'mul.s',
        '/': 'div.s',
    }
}

bool_dict = {
    'int': {
        '==': 'seq',
        '!=': 'sne',
        '>': 'sgt',
        '<': 'slt',
        '>=': 'sge',
        '<=': 'sle'
    },
    'char': {
        '==': 'seq',
        '!=': 'sge',
        '>': 'sgt',
        '<': 'slt',
        '>=': 'sge',
        '<=': 'sle'
    },
    'float': {
        '==': 'c.eq.s',
        '!=': 'c.ne.s',
        '>': 'c.le.s',
        '<': 'c.lt.s',
        '>=': 'c.lt.s',
        '<=': 'c.le.s'
    }
}

mips_operators = {
    'int': {
        'li': 'li',
        'lw': 'lw',
        'sw': 'sw',
        'neg': 'neg'
    },
    'char': {
        'li': 'li',
        'lw': 'lb',
        'sw': 'sb',
        'neg': 'neg'
    },
    'float': {
        'li': 'li.s',
        'lw': 'lwc1',
        'sw': 'swc1',
        'neg': 'neg.s'
    }
}

mips_globals = {
    "float": ".float",
    "char": ".byte",
    "char*": ".asciiz",
    "int": ".word"

}


def register_dict(symbol_type, regnr):
    sym = 't'
    if symbol_type == "float":
        sym = 'f'
    return '$%s%d' % (sym, regnr)


def get_operator_type(symbol_type: str) -> str:
    """
    pointers use the same operations instructions as integers
    :param symbol_type:
    :return: string
    """

    return 'int' if '*' in symbol_type or '&' in symbol_type == symbol_type else symbol_type
