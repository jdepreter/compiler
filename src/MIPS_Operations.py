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
    'float': {
        '==': 'c.eq.s',
        '!=': 'c.ne.s',
        '>': 'c.gt.s',
        '<': 'c.lt.s',
        '>=': 'c.ge.s',
        '<=': 'c.le.s'
    }
}
