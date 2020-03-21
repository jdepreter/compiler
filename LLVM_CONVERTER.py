from helperfuncs import *


class LLVM_Converter:
    def __init__(self, ast, file):
        self.ast = ast
        self.stack = []
        self.register = 0
        self.label = 0
        self.file = file
        self.null = {'int': '0', 'float': double_to_hex(0.0)}
        self.format_dict = {'int': 'i32', 'float': 'float', 'char': 'i8', 'bool': 'i1'}
        self.optype = {'int':
            {
                '+': 'add',
                '++': 'add',
                '-': 'sub',
                '--': 'sub',
                '*': 'mul',
                '/': 'sdiv',
                '%': 'srem'
            },
            'char': {
                '+': 'add',
                '++': 'add',
                '-': 'sub',
                '--': 'sub',
                '*': 'mul',
                '/': 'sdiv',
                '%': 'srem'
            },
            'float': {
                '+': 'fadd',
                '++': 'fadd',
                '-': 'fsub',
                '--': 'fsub',
                '*': 'fmul',
                '/': 'fdiv',
            }

        }

        self.cast_dict = {
            'int': {'float': 'sitofp', 'char': 'trunc', 'bool': 'trunc'},
            'float': {'int': 'fptosi', 'char': 'fptosi', 'bool': 'fptoui'},
            'char': {'int': 'zext', 'float': 'sitofp', 'bool': 'trunc'}
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
        self.convert = lambda x: self.format_dict[get_type_and_stars(x)[0]]

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
  %a_1 = fpext float %a to double
  %p = call i32 (i8*, ...)
       @printf(i8* getelementptr inbounds ([4 x i8],
                                           [4 x i8]* @format_float,
                                           i32 0, i32 0),
               double %a_1)
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
    def allocate_node(self, node, symbol_table, symbol_type):
        variable = node.label
        if node.node_type == 'assignment2':
            variable = node.children[0].label
        reg_nr = symbol_table.get_symbol(variable, node.ctx.start).current_register
        sym_type, stars = get_type_and_stars(symbol_type)
        string = "%a{} = alloca {}{} \n".format(
            reg_nr,
            self.format_dict[sym_type], stars
        )
        self.file.write(string)
        if node.node_type == 'assignment2':
            register = None
            if node.children[1].node_type == 'assignment':
                register = self.assign_node(node.children[1], symbol_table)
            else:
                register = self.solve_math(node.children[1], symbol_table)
            self.store_symbol("%a" + str(reg_nr), register[0], symbol_type, register[1])

        return "%a" + str(reg_nr), symbol_type

    def assign_node(self, node, symbol_table):
        symbol = symbol_table.get_symbol(str(node.children[0].label), node.ctx.start)
        address = '%a' + str(symbol.current_register)
        if node.children[1].node_type == 'assignment':
            register = self.assign_node(node.children[1], symbol_table)
        else:
            register = self.solve_math(node.children[1], symbol_table)
        self.store_symbol(address, register[0], symbol.symbol_type, register[1], node.children[0].label.count('*'))
        symbol.assigned = True
        return register, symbol.symbol_type

    def not_value(self, register, symbol_type):
        reg = self.register
        self.register += 1
        new = self.cast_value(register, symbol_type, 'bool')
        string = "%r{} = add i1 {}, 1\n".format(reg, new)
        self.file.write(string)
        reg2 = self.register
        self.register += 1
        string2 = "%r{} = zext i1 %r{} to i32".format(reg2, reg)
        self.file.write(string2)

        return '%r' + str(reg2), 'int'

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
                address, symbol_type = self.allocate_node(node.children[i], symbol_table, typing.label)
            return address, symbol_type

        elif node.node_type == 'assignment':
            return self.assign_node(node, symbol_table)

        elif node.node_type == 'method_call':
            return self.call_method(node, symbol_table)

        elif node.node_type == 'for':
            return self.loop(node, symbol_table)

        elif node.node_type == 'ifelse':
            return self.if_else(node, symbol_table)

        else:

            sol = self.solve_math(node, symbol_table)

            if sol[0] is None:
                for child in node.children:
                    if node.symbol_table is not None:
                        symbol_table = node.symbol_table

                    sol = self.solve_llvm_node(child, symbol_table)
            return sol

    def cast_value(self, register, current_type, new_type):

        current_sym_type, current_stars = get_type_and_stars(current_type)
        new_sym_type, new_stars = get_type_and_stars(new_type)
        if current_sym_type == new_sym_type:
            return register
        reg = self.register
        self.register += 1

        string = "%r{} = {} {}{} {} to {}{}\n".format(
            str(reg), self.cast_dict[current_sym_type][new_sym_type], self.format_dict[current_sym_type], current_stars,
            register, self.format_dict[new_sym_type], new_stars
        )
        self.file.write(string)
        return '%r' + str(reg)

    def store_symbol(self, address, value, address_symbol_type, value_symbol_type, dereference=0):
        value_to_store = self.cast_value(value, value_symbol_type, address_symbol_type)
        address_sym_type, address_stars = get_type_and_stars(address_symbol_type)
        current_register = self.dereference(address, address_stars, address_sym_type, dereference)[0]

        string = "store {}{} {}, {}*{} {}\n".format(
            self.format_dict[address_sym_type],
            address_stars[dereference:],
            value_to_store,
            self.format_dict[address_sym_type],
            address_stars[dereference:],
            current_register
        )
        self.file.write(string)

    def dereference(self, current_register, address_stars, address_sym_type, dereference):
        for i in range(dereference):
            reg = self.register
            self.register += 1
            current_register = self.load_instruction(reg, "*" * (len(address_stars) - i), address_sym_type,
                                                     current_register)
        return current_register, address_sym_type + (len(address_stars) - dereference) * '*'

    def store_float(self, _float):
        _float = float(_float)
        reg = self.register
        self.register += 1
        string = "%r{} = fptrunc double {} to float\n".format(str(reg), str(_float))
        self.file.write(string)
        return '%r' + str(reg)

    def load_symbol(self, symbol):
        reg = self.register
        self.register += 1
        sym_type, stars = get_type_and_stars(symbol.symbol_type)
        return self.load_instruction(reg, stars, sym_type, "%a" + str(symbol.current_register))

    def load_instruction(self, reg, stars, sym_type, current_register):
        string = '%r{} = load {}{} ,{}{}* {} \n'.format(
            str(reg), self.format_dict[sym_type], stars, self.format_dict[sym_type], stars, current_register
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
            allowed_operation(child1[1], child2[1], node.label, node.ctx.start)
            symbol_type = get_return_type(child1[1], child2[1])
            child_1 = self.cast_value(child1[0], child1[1], symbol_type)
            child_2 = self.cast_value(child2[0], child2[1], symbol_type)
            sym_type, stars = get_type_and_stars(symbol_type)
            if symbol_type == 'float' and node.label == '%':
                raise Exception("Error: incompatible type %: float")

            string = '%r{} = {} {}{} {}, {}\n'.format(
                str(reg), self.optype[symbol_type][node.label], self.format_dict[sym_type], stars,
                child_1,
                child_2
            )
            self.file.write(string)
            return '%r' + str(reg), symbol_type

        elif node.label == '&&':
            reg = self.register
            self.register += 1
            child1 = self.solve_math(node.children[0], symbol_table)
            child2 = self.solve_math(node.children[1], symbol_table)
            child_1 = self.cast_value(child1[0], child1[1], 'int')
            child_2 = self.cast_value(child2[0], child2[1], 'int')
            string = "%r{} = and i32 {}, {}\n".format(
                str(reg), child_1, child_2
            )
            self.file.write(string)
            return '%r' + str(reg), "int"
        elif node.label == '||':
            reg = self.register
            self.register += 1
            child1 = self.solve_math(node.children[0], symbol_table)
            child2 = self.solve_math(node.children[1], symbol_table)
            child_1 = self.cast_value(child1[0], child1[1], 'int')
            child_2 = self.cast_value(child2[0], child2[1], 'int')
            string = "%r{} = or i32 {}, {}\n".format(
                str(reg), child_1, child_2
            )
            self.file.write(string)
            return '%r' + str(reg), "int"

        elif node.label in ['==', '!=', '<', '>', '<=', '>=']:

            reg = self.register
            self.register += 1
            child1 = self.solve_math(node.children[0], symbol_table)
            child2 = self.solve_math(node.children[1], symbol_table)
            symbol_type = get_return_type(child1[1], child2[1])
            child_1 = self.cast_value(child1[0], child1[1], symbol_type)
            child_2 = self.cast_value(child2[0], child2[1], symbol_type)
            sym_type, stars = get_type_and_stars(symbol_type)
            string = '%r{} = {} {}{} {}, {} \n'.format(
                str(reg), self.bool_dict[sym_type][node.label], self.format_dict[sym_type], stars,
                child_1,
                child_2
            )
            self.file.write(string)
            reg2 = self.register
            self.register += 1
            string2 = '%r{} = zext i1 %r{} to i32\n'.format(str(reg2), str(reg))
            self.file.write(string2)

            return '%r' + str(reg2), 'int'

        elif node.node_type == 'Increment_var':

            symbol = symbol_table.get_assigned_symbol(node.children[0].label, node.ctx.start)
            new_sym = self.load_symbol(symbol)

            self.increment_var(new_sym, node, symbol, symbol.symbol_type)

            return new_sym, symbol.symbol_type

        elif node.node_type == 'Increment_op':
            symbol = symbol_table.get_assigned_symbol(node.children[0].label, node.ctx.start)
            new_sym = self.load_symbol(symbol)

            reg = self.increment_var(new_sym, node, symbol, symbol.symbol_type)

            return '%r' + str(reg), symbol.symbol_type

        elif node.node_type == 'unary plus':
            return self.solve_math(node.children[1], symbol_table)

        elif node.node_type == 'unary min':
            value = self.solve_math(node.children[1], symbol_table)
            reg = self.register
            self.register += 1
            string = "%r{} = {} {} {}, {}\n".format(
                reg, self.optype[value[1]]['-'], self.format_dict[value[1]], self.null[value[1]], value[0]
            )
            self.file.write(string)
            return '%r' + str(reg), value[1]

        elif node.node_type == 'rvalue':
            value = str(node.label)

            if str(node.symbol_type) == "float":
                value = self.store_float(float(node.label))
            if str(node.symbol_type)[0] == '&':
                value = '%a' + str(symbol_table.get_assigned_symbol(value, node.ctx.start).current_register)
            return value, str(node.symbol_type)

        elif node.node_type == 'lvalue':
            sym = symbol_table.get_assigned_symbol(node.label, node.ctx.start)
            sym_type, stars = get_type_and_stars(sym.symbol_type)
            address, symbol_type_stars = self.dereference('%a' + str(sym.current_register), stars, sym_type,
                                                          node.label.count('*'))
            reg = self.register
            self.register += 1
            sym_type, stars = get_type_and_stars(symbol_type_stars)
            return self.load_instruction(reg, stars, sym_type, address), symbol_type_stars

        elif node.node_type == 'bool2' and node.children[0].label == '!':

            value = self.solve_math(node.children[1], symbol_table)
            return self.not_value(value[0], value[1])

        return None, None

    def increment_var(self, new_sym, node, symbol, symbol_type):
        reg = self.register
        self.register += 1
        sym_type, stars = get_type_and_stars(symbol_type)
        string = '%r{} = {} {}{} {}, 1\n'.format(
            str(reg), self.optype[symbol_type][node.children[1].label], self.format_dict[sym_type], stars,
            new_sym
        )
        self.file.write(string)
        self.store_symbol('%a' + str(symbol.current_register), '%r' + str(reg), symbol_type, symbol_type)
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

        method = node.symbol_table.get_method(method_name, arg_types, node.ctx.start)
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

    def go_to_label(self, label):
        string = "br label %{}\n\n".format(label)
        self.file.write(string)

    def go_to_conditional(self, condition, label_true, label_false):
        """
        :param condition: register with value of condition, should be i1
        :param label_true:
        :param label_false:
        :return: nothing
        """
        string = "br i1 {}, label %{}, label %{}\n\n".format(condition, label_true, label_false)
        self.file.write(string)

    def add_label(self, label):
        string = "; <label>:%{}:\n".format(label)
        self.file.write(string)

    def loop(self, node, symbol_table):
        if node.children[0].node_type == 'for initial':
            self.solve_llvm_node(node.children[0].children[0], symbol_table)

        labels = {
            "code_block": None,
            "comparison": None,
            "update": None,
            "next_block": None,
        }
        self.go_to_label("{}".format(self.register))
        self.add_label("{}".format(self.register))
        self.register += 1
        for child in node.children:
            if child.node_type == "condition":
                self.solve_llvm_node(child, child.symbol_table)

            elif child.node_type == 'for update':
                self.solve_llvm_node(child, child.symbol_table)
                self.go_to_label(labels["comparison"])
            else:
                self.solve_llvm_node(child, child.symbol_table)
                self.go_to_label(labels["update"])

    def if_else(self, node, symbol_table):
        condition = node.children[0]
        reg, value_type = self.solve_llvm_node(condition, symbol_table)
        string = "%r{} = icmp ne {} {}, 0\n".format(
            self.register, self.format_dict[value_type], reg
        )
        self.file.write(string)
        self.go_to_conditional("%r" + str(self.register), self.label, self.label + 1)
        self.register += 1
        self.add_label(self.label)
        self.label += 1
        # schrijf if true gedeelte

        self.solve_llvm_node(node.children[1], symbol_table)
        self.go_to_label(self.label + len(node.children) - 2)

        # schrijf if false gedeelte
        if len(node.children) > 2:
            self.add_label(self.label)
            self.label += 1
            self.solve_llvm_node(node.children[1], symbol_table)

        # schrijf alle volgende instructies achter een label
        self.add_label(self.label)
        self.label += 1
        return
