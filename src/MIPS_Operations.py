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
        '!=': 'sge',
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
        '!=': 'c.eq.s',
        '>': 'c.le.s',
        '<': 'c.lt.s',
        '>=': 'c.lt.s',
        '<=': 'c.le.s'
    }
}

mips_operators ={
    'int': {
        'li': 'li',
        'lw': 'lw',
        'sw': 'sw'
    },
    'char': {
        'li': 'li',
        'lw': 'lw',
        'sw': 'sw'
    },
    'float': {
        'li': 'li.s',
        'lw': 'lwc1',
        'sw': 'swc1'
    }


}


def register_dict(symbol_type, regnr):
    sym = 't'
    if symbol_type == "float":
        sym = 'f'
    return '$%s%d' % (sym, regnr)
