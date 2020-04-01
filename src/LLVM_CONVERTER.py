from src.helperfuncs import *


class LLVM_Converter:
    def __init__(self, ast, file):
        self.ast = ast
        self.stack = []
        self.register = 0
        self.label = 0
        self.write = True
        self.breaks = False
        self.break_stack = []
        self.continue_stack = []
        self.function_stack = []
        self.file = file
        self.null = {'int': '0', 'float': double_to_hex(0.0), 'char': '0'}
        self.format_dict = {'int': 'i32', 'float': 'float', 'char': 'i8', 'bool': 'i1', 'void': 'void'}
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

    def write_to_file(self, string):
        if self.write:
            self.file.write(string)

    def to_llvm(self):
        self.write_to_file("""
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
        # self.write_to_file("define i32 @main() {\n"
        #                 "start:\n")
        current_symbol_table = self.ast.startnode.symbol_table
        self.solve_llvm_node(self.ast.startnode, current_symbol_table)

        # self.write_to_file("ret i32 0\n"
        #                 "}\n")

    # helpermethod to write used for declaration or definition
    def allocate_node(self, node, symbol_table, symbol_type):
        variable = node.label
        if node.node_type == 'assignment2':
            variable = node.children[0].label

        if node.node_type == 'Arg_definition':
            variable = node.children[1].label
        symbol = symbol_table.get_symbol(variable, node.ctx.start)
        sym_type, stars = get_type_and_stars(symbol_type)

        if symbol.is_global:
            # Do funny xD llvm global stuff
            value = 0
            if node.node_type == 'assignment2':
                if node.children[1].node_type == 'rvalue':
                    value = node.children[1].label
                else:
                    raise Exception("Initializer element is not constant")

            self.write_to_file("{} = common global {} {}\n".format(symbol.current_register, self.format_dict[sym_type], value))
            return None, None

        reg_nr = symbol.current_register
        string = "{} = alloca {}{} \n".format(
            reg_nr,
            self.format_dict[sym_type], stars
        )
        self.write_to_file(string)
        if node.node_type == 'assignment2':
            register = None
            if node.children[1].node_type == 'assignment':
                register = self.assign_node(node.children[1], symbol_table)
            else:
                register = self.solve_math(node.children[1], symbol_table)
            self.store_symbol(reg_nr, register[0], symbol_type, register[1])

        return reg_nr, symbol_type

    def assign_node(self, node, symbol_table):
        symbol = symbol_table.get_symbol(str(node.children[0].label), node.ctx.start)
        address = symbol.current_register
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
        self.write_to_file(string)
        reg2 = self.register
        self.register += 1
        string2 = "%r{} = zext i1 %r{} to i32".format(reg2, reg)
        self.write_to_file(string2)

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

        elif node.node_type == 'for':
            return self.loop(node, symbol_table)

        elif node.node_type == 'for break':
            if len(self.break_stack) > 0:
                self.go_to_label(self.break_stack[0])
                self.write = False
                self.breaks = True
                return None, None
            else:
                raise BreakError("[Error] Line {} Position {} break statement not within loop or switch".format(
                    node.ctx.start.line, node.ctx.start.column
                ))

        elif node.node_type == 'for continue':
            if len(self.continue_stack) > 0:
                self.go_to_label(self.continue_stack[0])
                self.write = False
                return None, None
            else:
                raise BreakError("[Error] Line {} Position {} continue statement not within loop".format(
                    node.ctx.start.line, node.ctx.start.column
                ))

        elif node.node_type == "switch":
            return self.switch(node, symbol_table)

        elif node.node_type == 'ifelse':
            return self.if_else(node, symbol_table)

        elif node.node_type == 'method_definition':
            return self.generate_method(node, symbol_table)

        elif node.node_type == 'return':
            return self.return_node(node, symbol_table)
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
            str(reg), self.cast_type(current_sym_type, new_sym_type), self.format_dict[current_sym_type], current_stars,
            register, self.format_dict[new_sym_type], new_stars
        )
        self.write_to_file(string)
        return '%r' + str(reg)

    def cast_type(self, current_sym_type, new_sym_type):
        if current_sym_type == 'void':
            raise Exception("Can't cast void")
        return self.cast_dict[current_sym_type][new_sym_type]

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
        self.write_to_file(string)

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
        self.write_to_file(string)
        return '%r' + str(reg)

    def load_symbol(self, symbol):
        reg = self.register
        self.register += 1
        sym_type, stars = get_type_and_stars(symbol.symbol_type)
        return self.load_instruction(reg, stars, sym_type, symbol.current_register)

    def load_instruction(self, reg, stars, sym_type, current_register):
        string = '%r{} = load {}{} ,{}{}* {} \n'.format(
            str(reg), self.format_dict[sym_type], stars, self.format_dict[sym_type], stars, current_register
        )
        self.write_to_file(string)
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
            self.write_to_file(string)
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
            self.write_to_file(string)
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
            self.write_to_file(string)
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
            self.write_to_file(string)
            reg2 = self.register
            self.register += 1
            string2 = '%r{} = zext i1 %r{} to i32\n'.format(str(reg2), str(reg))
            self.write_to_file(string2)

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
            self.write_to_file(string)
            return '%r' + str(reg), value[1]

        elif node.node_type == 'method_call':
            return self.call_method(node, symbol_table)

        elif node.node_type == 'rvalue':
            value = str(node.label)

            if str(node.symbol_type) == "float":
                value = self.store_float(float(node.label))
            if str(node.symbol_type)[0] == '&':
                value = symbol_table.get_assigned_symbol(value, node.ctx.start).current_register
            return value, str(node.symbol_type)

        elif node.node_type == 'lvalue':
            sym = symbol_table.get_assigned_symbol(node.label, node.ctx.start)
            sym_type, stars = get_type_and_stars(sym.symbol_type)
            address, symbol_type_stars = self.dereference(sym.current_register, stars, sym_type,
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
        self.write_to_file(string)
        self.store_symbol(symbol.current_register, '%r' + str(reg), symbol_type, symbol_type)
        return reg

    def call_method(self, node, symbol_table):
        method_name = node.children[0].label
        args = node.children[1].children[:]
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
        string = ""
        if method.symbol_type != "void":
            newreg = self.register
            self.register += 1
            string = "%r{} = call {} ({}) @{}({})\n".format(str(newreg), self.format_dict[method.symbol_type],
                                                            ','.join(m),
                                                            method.internal_name,
                                                            ','.join(args))
            self.write_to_file(string)
            return '%r' + str(newreg), method.symbol_type
        else:
            string = "call {} ({}) @{}({})\n".format(
                method.symbol_type,
                ','.join(m),
                method.internal_name,
                ','.join(args)
            )
            self.write_to_file(string)
            return "void", "void"

    def go_to_label(self, label):
        string = "br label %label{}\n".format(label)
        self.write_to_file(string)

    def go_to_conditional(self, condition, label_true, label_false):
        """
        :param condition: register with value of condition, should be i1
        :param label_true:
        :param label_false:
        :return: nothing
        """
        string = "br i1 {}, label %label{}, label %label{}\n".format(condition, label_true, label_false)
        self.write_to_file(string)

    def add_label(self, label):
        string = "\nlabel{}:\n".format(label)
        self.write_to_file(string)

    def loop(self, node, symbol_table):
        # Write initial assignment
        total_labels = len(node.children)
        skip_condition = False
        if node.children[0].node_type == 'for initial':
            self.solve_llvm_node(node.children[0].children[0], symbol_table)
            total_labels -= 1

        elif node.children[0].node_type == 'for do':
            skip_condition = True

        breaks = self.breaks

        labels = {
            "condition": self.label,
            "code_block": self.label + 1,
            "update": self.label + 2,
            "next_block": self.label + total_labels,
        }
        self.break_stack.insert(0, labels["next_block"])
        self.continue_stack.insert(0, labels["condition"])
        write = self.write
        self.label += 4
        if skip_condition:
            # Do While
            self.go_to_label(labels["code_block"])
        else:
            # Go to conditional
            self.go_to_label(labels["condition"])
        self.register += 1
        update = False
        for child in node.children:
            if child.node_type == "condition":
                self.write = write
                self.add_label(labels["condition"])
                reg, value_type = self.solve_llvm_node(child, child.symbol_table)
                string = "%r{} = icmp ne {} {}, 0\n".format(
                    self.register, self.format_dict[value_type], reg
                )
                self.write_to_file(string)
                self.go_to_conditional("%r" + str(self.register), labels["code_block"], labels["next_block"])
                self.register += 1

            elif child.node_type == 'for update':
                self.write = write
                self.continue_stack[0] = labels["update"]
                self.add_label(labels["update"])
                self.solve_llvm_node(child, child.symbol_table)
                self.go_to_label(labels["condition"])
                update = True

            elif child.node_type != 'for initial':
                self.write = write
                self.add_label(labels["code_block"])
                self.solve_llvm_node(child, child.symbol_table)
                if update:
                    self.go_to_label(labels["update"])
                else:
                    self.go_to_label(labels["condition"])

        self.break_stack.pop()
        self.continue_stack.pop()
        self.write = write
        self.add_label(labels["next_block"])
        self.breaks = breaks

    def if_else(self, node, symbol_table):
        if not self.write:
            return
        condition = node.children[0]
        reg, value_type = self.solve_llvm_node(condition, symbol_table)
        string = "%r{} = icmp ne {} {}, 0\n".format(
            self.register, self.format_dict[value_type], reg
        )
        label = self.label
        self.label += len(node.children)
        self.write_to_file(string)
        self.go_to_conditional("%r" + str(self.register), label, label + 1)
        self.register += 1
        self.add_label(label)
        write = self.write
        # schrijf if true gedeelte

        self.solve_llvm_node(node.children[1], symbol_table)
        self.go_to_label(label + len(node.children) - 1)
        if_write = self.write
        else_write = write

        # schrijf if false gedeelte
        if len(node.children) > 2:
            self.write = write

            self.add_label(label + 1)
            self.solve_llvm_node(node.children[2], symbol_table)
            self.go_to_label(label + 2)
            else_write = self.write

        self.write = else_write or if_write
        # schrijf alle volgende instructies achter een label
        self.add_label(label + len(node.children) - 1)

        return

    def switch(self, node, symbol_table):
        if not self.write:
            return
        switchval, switchtype = self.solve_math(node.children[0], symbol_table)
        branchval = self.cast_value(switchval, switchtype, "int")

        write = self.write
        breaks = self.breaks
        self.breaks = False

        continue_writing = False

        current_label = self.label
        default_label = current_label + len(node.children) - 1

        self.break_stack.insert(0, default_label)
        self.label += len(node.children)
        string = ""

        default = False
        for i in range(1, len(node.children)):
            curr = node.children[i]
            if curr.label == "default":
                if default:
                    raise Exception(
                        "[Error] line {} position {} Secondary definition of default".format(node.ctx.start.line,
                                                                                             node.ctx.start.column))

                default = True
                default_label = current_label + i - 1

            else:
                string += "i32 {}, label %label{}\n".format(str(int(curr.label)), str(current_label + i - 1))

        operation = "switch i32 {}, label %label{} [{}]\n".format(branchval, default_label, string)

        self.write_to_file(operation)
        for i in range(1, len(node.children)):
            continue_writing = continue_writing or self.write or self.breaks
            self.write = write
            self.breaks = False
            self.go_to_label(current_label + i - 1)
            self.add_label(current_label + i - 1)
            self.solve_llvm_node(node.children[i], symbol_table)

        if default:
            self.write = continue_writing
        else:
            self.write = write

        self.go_to_label(current_label + len(node.children) - 1)
        self.add_label(current_label + len(node.children) - 1)

        self.break_stack.pop()
        self.breaks = breaks

    def generate_method(self, method_node, symbol_table):
        args = []
        if method_node.children[2].node_type == 'def_args':
            for arg in method_node.children[2].children:
                args.append(arg.children[0].label)
        func = symbol_table.get_method(method_node.children[1].label, args, method_node.ctx.start)
        self.function_stack.insert(0, func)

        if not func.defined:
            raise Exception("temp")

        if len(args) != len(func.arguments):
            raise Exception("temp")

        m = list(map(self.convert, args))
        startstring = "define {} @{}({}) {}\n".format(self.format_dict[func.symbol_type], func.internal_name,
                                                      ','.join(m), '{')
        self.write_to_file(startstring)
        method_llvm = LLVM_Converter(method_node, self.file)
        method_llvm.function_stack = self.function_stack
        method_llvm.write = self.write
        for i in range(len(args)):
            new_val, val_type = method_llvm.allocate_node(method_node.children[2].children[i],
                                                          method_node.children[2].children[i].symbol_table,
                                                          method_node.children[2].children[i].children[0].label)
            store_str = "store {} %{}, {}* {}\n".format(self.format_dict[val_type], str(i), self.format_dict[val_type],
                                                        new_val)
            # TODO CAST VALUES
            method_llvm.write_to_file(store_str)

        method_llvm.solve_llvm_node(method_node.children[-1], symbol_table)
        if func.symbol_type == 'void':
            return_string = "ret void\n"
        else:

            return_string = "ret {} {}\n".format(self.format_dict[func.symbol_type], self.null[func.symbol_type])
        self.write_to_file(return_string)

        self.write = True

        endstring = "}\n"
        self.write_to_file(endstring)
        self.function_stack.pop(0)
        return

    def return_node(self, node, symbol_table):
        if len(node.children) == 0:
            # return void
            if self.function_stack[0].symbol_type == 'void':
                string = "ret void\n"
                self.file.write(string)
                self.write = False
                return
            else:
                raise Exception('niet void verdomme')

        if self.function_stack[0].symbol_type == 'void':
            raise Exception('functie is void verdomme ')
        returnreg, return_type = self.solve_llvm_node(node.children[0], symbol_table)
        newtype = self.function_stack[0].symbol_type
        castedreg = self.cast_value(returnreg, return_type, newtype)

        string = "ret {} {}\n".format(self.format_dict[newtype], castedreg)
        self.write_to_file(string)
        self.write = False
        return



