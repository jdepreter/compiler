class LLVM_Converter:
    def __init__(self, ast, file):
        self.ast = ast
        self.stack = []
        self.register = 0
        self.file = file
        self.format_dict = {'int': 'i32', 'float': 'f32', 'char': 'i8'}
        self.optype = {'int':
            {
                '+': 'add',
                '-': 'sub',
                '*': 'mul',
                '/': 'sdiv',
                '%': 'srem'
            },
            'float':{
                '+': 'fadd',
                '-': 'fsub',
                '*': 'fmul',
                '/': 'fdiv',
                '%': 'frem'
            }

        }

        self.bool_dict = {'int':
                              {
                                  '==': 'icmp eq',
                                  '!=': 'icmp ne',
                                  '>': 'icmp sgt',
                                  '<': 'icmp slt',
                                  '>=': 'icmp sge',
                                  '<=': 'icmp sle'
                              },
                          'float':
                              {
                                  '==': 'fcmp oeq',
                                  '!=': 'fcmp ole',
                                  '>': 'fcmp ogt',
                                  '<': 'fcmp olt',
                                  '>=': 'fcmp oge',
                                  '<=': 'fcmp ole'
                              }
                          }

    def to_llvm(self):
        # self.stack.insert(0, self.ast.startnode)
        current_symbol_table = self.ast.startnode.symbol_table
        self.solve_llvm_node(self.ast.startnode, current_symbol_table)

    # helpermethod to write used for declaration or definition
    def allocate_node(self, node, symbol_table):
        reg_nr = symbol_table.get_symbol(str(node.children[1].label), None).current_register
        string = "%a{} = alloca {} \n".format(
            reg_nr,
            self.format_dict[str(node.children[0].label)]
        )
        self.file.write(string)
        return "%a" + str(reg_nr)

    def solve_llvm_node(self, node, symbol_table):
        # TODO x++ & ++x staan nog ni ok in den boom && add char / double && maybe arrays && typeswitching + warnings
        if node.symbol_table is not None:
            symbol_table = node.symbol_table

        if node.label == 'dec':
            self.allocate_node(node, symbol_table)
        elif node.label == 'def':
            address = self.allocate_node(node, symbol_table)
            register = self.solve_math(node.children[2], symbol_table, 'int')
            self.store_symbol(address, register, 'int')
        elif node.label == 'ass':
            address = '%a' + str(symbol_table.get_symbol(str(node.children[0].label), None).current_register)
            register = self.solve_math(node.children[1], symbol_table, 'int')
            self.store_symbol(address, register, 'int')

        else:
            for child in node.children:
                if node.symbol_table is not None:
                    symbol_table = node.symbol_table

                self.solve_llvm_node(child, symbol_table)

    def store_symbol(self, address, value, symbol_type):
        string = 'store ' + self.format_dict[symbol_type] + ' ' + value + ', ' + self.format_dict[symbol_type] + '* ' + address + '\n'
        self.file.write(string)

    def load_symbol(self, symbol_type):
        reg = self.register
        self.register += 1
        string = '%r{} = load {} * %a{} \n'.format(
            str(reg), self.format_dict[symbol_type.symbol_type], symbol_type.current_register
        )
        self.file.write(string)
        return '%r' + str(reg)

    def solve_math(self, node, symbol_table, symbol_type):
        string = ''
        if node.label in ['+', '-', '*', '/', '%']:
            reg = self.register
            self.register += 1
            string = '%r{} = {} {} {}, {}\n'.format(
                str(reg), self.optype[symbol_type][node.label], self.format_dict[symbol_type],
                self.solve_math(node.children[0], symbol_table, symbol_type),
                self.solve_math(node.children[1], symbol_table, symbol_type)
            )

            self.file.write(string)
            return '%r' + str(reg)

        elif node.label == '&&':
            reg = self.register
            self.register += 1
            string = '%r' + str(reg) + ' = and i32 ' + \
                     self.solve_math(node.children[0], symbol_table, symbol_type) + ', ' + self.solve_math(node.children[1],
                                                                                                    symbol_table,
                                                                                                    symbol_type) + '\n'
            self.file.write(string)
            return '%r' + str(reg)
        elif node.label == '||':
            reg = self.register
            self.register += 1
            string = '%r' + str(reg) + ' = or i32 ' + \
                     self.solve_math(node.children[0], symbol_table, symbol_type) + ', ' + self.solve_math(node.children[1],
                                                                                                    symbol_table,
                                                                                                    symbol_type) + '\n'

            self.file.write(string)
            return '%r' + str(reg)

        elif node.label in ['==', '!=', '<', '>', '<=', '>=']:

            reg = self.register
            self.register += 1
            string = '%r{} = {} {} {}, {} \n'.format(
                str(reg), self.bool_dict[symbol_type][node.label], self.format_dict[symbol_type],
                self.solve_math(node.children[0], symbol_table, symbol_type),
                self.solve_math(node.children[1], symbol_table, symbol_type)
            )
            self.file.write(string)
            return '%r' + str(reg)

        else:
            try:
                newval = int(node.label)
                return str(newval)
            except:
                # assume we'll have a symbol
                sym = symbol_table.get_symbol(node.label, None)
                return self.load_symbol(sym)



















