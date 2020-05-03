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
        '>': 'c.gt.s',
        '<': 'c.lt.s',
        '>=': 'c.ge.s',
        '<=': 'c.le.s'
    }
}

mips_operators ={
    'int': {
        'li': 'li',
        'lw': 'lw',
        'sw': 'sw',
        'neg': 'neg'
    },
    'char': {
        'li': 'li',
        'lw': 'lw',
        'sw': 'sw',
        'neg': 'neg'
    },
    'float': {
        'li': 'li.s',
        'lw': 'lwc1',
        'sw': 'swc1',
        'neg': 'neg.s'
    }


}


def register_dict(symbol_type, regnr):
    sym = 't'
    if symbol_type == "float":
        sym = 'f'
    return '$%s%d' % (sym, regnr)
