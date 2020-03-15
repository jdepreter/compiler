from helperfuncs import get_return_type

class LLVM_Converter:
    def __init__(self, ast, file):
        self.ast = ast
        self.stack = []
        self.register = 0
        self.file = file
        self.format_dict = {'int': 'i32', 'float': 'float', 'char': 'i8'}
        self.optype = {'int':
            {
                '+': 'add',
                '++': 'add',
                '-': 'sub',
                '-*': 'sub',
                '*': 'mul',
                '/': 'sdiv',
                '%': 'srem'
            },
            'float':{
                '+': 'fadd',
                '++': 'fadd',
                '-': 'fsub',
                '--': 'fsub',
                '*': 'fmul',
                '/': 'fdiv',
                '%': 'frem'
            }

        }
        self.cast_dict = {
            'int': {'float': 'sitofp'},
            'float': {'int': 'fptosi'}


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
        self.convert = lambda x: self.format_dict[x]

    def to_llvm(self):
        self.file.write("""
declare i32 @printf(i8*, ...)
@format = private constant [4 x i8] c"%d\\0A\\00"
@format_float = private constant [4 x i8] c"%f\\0A\\00"
@format_char = private constant [4 x i8] c"%c\\0A\\00"

define void @print_int(i32 %a){
  %p = call i32 (i8*, ...)
       @printf(i8* getelementptr inbounds ([4 x i8],
                                           [4 x i8]* @format,
                                           i32 0, i32 0),
               i32 %a)
  ret void
}

define void @print_float(float %a){
  %p = call i32 (i8*, ...)
       @printf(i8* getelementptr inbounds ([4 x i8],
                                           [4 x i8]* @format_float,
                                           i32 0, i32 0),
               float %a)
  ret void
}

define void @print_char(i8 %a){
  %p = call i32 (i8*, ...)
       @printf(i8* getelementptr inbounds ([4 x i8],
                                           [4 x i8]* @format_char,
                                           i32 0, i32 0),
               i8 %a)
  ret void
}\n""")
        # self.stack.insert(0, self.ast.startnode)
        self.file.write("define i32 @main() {\n"
                        "start:\n")
        current_symbol_table = self.ast.startnode.symbol_table
        self.solve_llvm_node(self.ast.startnode, current_symbol_table)

        self.file.write("ret i32 0\n"
                        "}\n")

    # helpermethod to write used for declaration or definition
    def allocate_node(self, node, symbol_table, type):
        variable = node.label
        if node.node_type == 'assignment2':
            variable = node.children[0].label
        reg_nr = symbol_table.get_symbol(variable, None).current_register
        string = "%a{} = alloca {} \n".format(
            reg_nr,
            self.format_dict[type]
        )
        self.file.write(string)
        if node.node_type == 'assignment2':
            register = None
            if node.children[1].node_type == 'assignment':
                register = self.assign_node(node.children[1], symbol_table)
            else:
                register = self.solve_math(node.children[1], symbol_table)[0]
            self.store_symbol("%a" + str(reg_nr), register, type)

        return "%a" + str(reg_nr)

    def assign_node(self, node, symbol_table):
        symbol = symbol_table.get_symbol(str(node.children[0].label), None)
        address = '%a' + str(symbol.current_register)
        if node.children[1].node_type == 'assignment':
            register = self.assign_node(node.children[1], symbol_table)
        else:
            register = self.solve_math(node.children[1], symbol_table)[0]
        self.store_symbol(address, register, symbol.symbol_type)
        return register

    def solve_llvm_node(self, node, symbol_table):
        # TODO x++ & ++x staan nog ni ok in den boom && add char / double && maybe arrays && typeswitching + warnings
        if node.symbol_table is not None:
            symbol_table = node.symbol_table

        if node.node_type == 'definition':
            typing = node.children[0]
            varstart = 1
            if typing.node_type == 'const':
                typing = node.children[1]
                varstart = 2
            for i in range(varstart, len(node.children)):
                address = self.allocate_node(node.children[i], symbol_table, typing.label)

        elif node.node_type == 'assignment':
            self.assign_node(node, symbol_table)
            # symbol = symbol_table.get_symbol(str(node.children[0].label), None)
            # address = '%a' + str(symbol.current_register)
            # register = self.solve_math(node.children[1], symbol_table, symbol.symbol_type)
            # self.store_symbol(address, register, symbol.symbol_type)

        elif node.node_type == 'method_call':
            self.call_method(node, symbol_table)

        else:

            sol = self.solve_math(node, symbol_table)[0]

            if sol is None:
                for child in node.children:
                    if node.symbol_table is not None:
                        symbol_table = node.symbol_table

                    self.solve_llvm_node(child, symbol_table)

    def store_symbol(self, address, value, address_symbol_type, value_symbol_type):
        value_to_store = value

        if address_symbol_type != value_symbol_type:
            reg = self.register
            self.register += 1
            string = "%r{} = {} {} {} to {}".format(
                str(reg), self.cast_dict[value_symbol_type][address_symbol_type], self.format_dict[value_symbol_type],
                value, self.format_dict[address_symbol_type]
            )
            self.file.write(string)
            value_to_store ='%r'+str(reg)


        string = 'store ' + self.format_dict[address_symbol_type] + ' ' + value_to_store + ', ' + self.format_dict[address_symbol_type] + '* ' + address + '\n'
        self.file.write(string)

    def load_symbol(self, symbol):
        reg = self.register
        self.register += 1
        string = '%r{} = load {} ,{}* %a{} \n'.format(
            str(reg), self.format_dict[symbol.symbol_type],self.format_dict[symbol.symbol_type], symbol.current_register
        )
        self.file.write(string)
        return '%r' + str(reg)

    def solve_math(self, node, symbol_table):
        string = ''
        if node.label in ['+', '-', '*', '/', '%']:
            reg = self.register
            self.register += 1
            child1 = self.solve_math(node.children[0], symbol_table)
            child2 = self.solve_math(node.children[1], symbol_table)
            symbol_type = get_return_type(child1[1], child2[1])
            string = '%r{} = {} {} {}, {}\n'.format(
                str(reg), self.optype[symbol_type][node.label], self.format_dict[symbol_type],
                child1[0],
                child2[0]
            )

            self.file.write(string)
            return '%r' + str(reg), symbol_type

        elif node.label == '&&':
            reg = self.register
            self.register += 1
            child1 = self.solve_math(node.children[0], symbol_table)
            child2 = self.solve_math(node.children[1], symbol_table)
            string = "%r{} = and i32 {}, {}\n".format(
                str(reg), child1[0], child2[0]
            )
            self.file.write(string)
            return '%r' + str(reg), "int"
        elif node.label == '||':
            reg = self.register
            self.register += 1
            child1 = self.solve_math(node.children[0], symbol_table)
            child2 = self.solve_math(node.children[1], symbol_table)
            string = "%r{} = or i32 {}, {}\n".format(
                str(reg), child1[0], child2[0]
            )
            self.file.write(string)
            return '%r' + str(reg), "int"

        elif node.label in ['==', '!=', '<', '>', '<=', '>=']:

            reg = self.register
            self.register += 1
            child1 = self.solve_math(node.children[0], symbol_table)
            child2 = self.solve_math(node.children[1], symbol_table)
            symbol_type = get_return_type(child1[1], child2[1])
            string = '%r{} = {} {} {}, {} \n'.format(
                str(reg), self.bool_dict[symbol_type][node.label], self.format_dict[symbol_type],
                child1[0],
                child2[0]
            )
            self.file.write(string)
            return '%r' + str(reg), symbol_type

        elif node.node_type == 'Increment_var':

            symbol = symbol_table.get_symbol(node.children[0].label, None)
            new_sym = self.load_symbol(symbol)

            self.increment_var(new_sym, node, symbol, symbol.symbol_type)

            return new_sym, symbol.symbol_type

        elif node.node_type == 'Increment_op':
            symbol = symbol_table.get_symbol(node.children[0].label, None)
            new_sym = self.load_symbol(symbol)

            reg = self.increment_var(new_sym, node, symbol, symbol.symbol_type)

            return '%r' + str(reg), symbol.symbol_type

        elif node.node_type == 'unary plus':
            return self.solve_math(node.children[1], symbol_table)

        elif node.node_type == 'unary min':
            value = self.solve_math(node.children[1], symbol_table)
            reg = self.register
            self.register += 1
            string = "%r{} = fneg {} {}".format(
                reg, self.format_dict[value[1]], value[0]
            )
            self.file.write(string)
            return '%r' + str(reg), value[1]



        elif node.node_type == 'rvalue':
            return str(node.label), str(node.symbol_type)

        elif node.node_type == 'lvalue':
            sym = symbol_table.get_symbol(node.label, None)
            return self.load_symbol(sym), sym.symbol_type

        return None, None

    def increment_var(self, new_sym, node, symbol, symbol_type):
        reg = self.register
        self.register += 1
        string = '%r{} = {} {} {}, 1\n'.format(
            str(reg), self.optype[symbol_type][node.children[1].label], self.format_dict[symbol_type],
            new_sym
        )
        self.file.write(string)
        self.store_symbol('%a' + str(symbol.current_register), '%r' + str(reg), symbol_type)
        return reg

    def call_method(self, node, symbol_table):
        method_name = node.children[0].label
        args = [node.children[1]]
        arg_types = []
        arg_reg = []
        for arg in args:
            reg, symbol_type = self.solve_math(arg, symbol_table)
            arg_reg.append(reg)
            arg_types.append(symbol_type)

        method = node.symbol_table.get_method(method_name, arg_types, None)
        m = list(map(self.convert, method.arguments))
        for i in range(len(args)):
            args[i] = m[i] + ' ' + arg_reg[i]

        string = "call {} ({}) @{}({})\n".format(
            method.symbol_type,
            ','.join(m),
            method.internal_name,
            ','.join(args)
        )
        self.file.write(string)
