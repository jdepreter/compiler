from src.helperfuncs import *
import re


def string_to_charptr(string, symbol_table):
    if not string in symbol_table.restrings:
        return string
    length = len(symbol_table.restrings[string]) + 1
    string = "getelementptr inbounds ([{} x i8], [{} x i8]* {}, i32 0, i32 0)" \
        .format(length, length, string)
    return string


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
            'int*': {'int': 'ptrtoint'},
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
        self.convert2 = lambda x: self.format_dict[get_type_and_stars(x)[0]] + get_type_and_stars(x)[1]

    def write_to_file(self, string):
        if self.write:
            self.file.write(string)

    def to_llvm(self):
        #         self.write_to_file("""
        # declare i32 @printf(i8*, ...)
        # @format = private constant [4 x i8] c"%d\\0A\\00"
        # @format_float = private constant [4 x i8] c"%f\\0A\\00"
        # @format_char = private constant [4 x i8] c"%c\\0A\\00"
        # define void @print_int(i32 %a){
        #   %p = call i32 (i8*, ...)
        #        @printf(i8* getelementptr inbounds ([4 x i8],
        #                                            [4 x i8]* @format,
        #                                            i32 0, i32 0),
        #                i32 %a)
        #   ret void
        # }
        #
        # define void @print_float(float %a){
        #   %a_1 = fpext float %a to double
        #   %p = call i32 (i8*, ...)
        #        @printf(i8* getelementptr inbounds ([4 x i8],
        #                                            [4 x i8]* @format_float,
        #                                            i32 0, i32 0),
        #                double %a_1)
        #   ret void
        # }
        #
        # define void @print_char(i8 %a){
        #   %p = call i32 (i8*, ...)
        #        @printf(i8* getelementptr inbounds ([4 x i8],
        #                                            [4 x i8]* @format_char,
        #                                            i32 0, i32 0),
        #                i8 %a)
        #   ret void
        # }\n""")
        # self.stack.insert(0, self.ast.startnode)
        # self.write_to_file("define i32 @main() {\n"
        #                 "start:\n")
        current_symbol_table = self.ast.startnode.symbol_table
        self.write_to_file(
            'target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"\ntarget triple = "x86_64-pc-linux-gnu"\n'
        )
        self.define_strings(current_symbol_table)
        self.solve_llvm_node(self.ast.startnode, current_symbol_table)

        # self.write_to_file("ret i32 0\n"
        #                 "}\n")

    def get_address_register(self, node, symbol_table):
        sym = symbol_table.get_assigned_symbol(node.label, node.ctx.start)
        sym_type, stars = get_type_and_stars(sym.symbol_type)
        address = sym.var_counter
        if node.node_type == 'array_element':
            address = self.get_index_of_array(sym.var_counter, self.format_dict[sym_type] + stars, sym.size,
                                              node.children[1], symbol_table, node.label,
                                              node.ctx.start)[0]

        if node.label.count('*') > 0:
            address = self.dereference(address, stars, sym_type, node.label.count('*'))[0]

        return address

    # helpermethod to write used for declaration or definition
    def allocate_node(self, node, symbol_table, symbol_type):
        variable = node.label
        if node.node_type in ['assignment2', 'array']:
            variable = node.children[0].label

        if node.node_type == 'Arg_definition':
            variable = node.children[1].label

        symbol = symbol_table.get_symbol(variable, node.ctx.start)
        sym_type, stars = get_type_and_stars(symbol_type)

        if symbol.is_global:
            # Do funny xD llvm global stuff
            if node.node_type == 'array':
                reg_nr = self.allocate_global_array(stars, self.format_dict[sym_type], symbol,
                                                    self.solve_math(node.children[1], symbol_table))[0]
                return None, None
            value = 0
            if node.node_type == 'assignment2':
                if node.children[1].node_type == 'rvalue':
                    value = node.children[1].label
                else:
                    raise Exception("Initializer element is not constant")

            self.write_to_file("{} = global {} {}\n".format(symbol.var_counter, self.format_dict[sym_type], value))
            symbol.written = True
            return None, None

        if node.node_type == 'array':
            reg_nr = self.allocate_array(stars, self.format_dict[sym_type], symbol,
                                         node.children[1], symbol_table)[0]
        else:
            reg_nr = self.alloc_instruction(stars, sym_type, symbol)

        if node.node_type == 'assignment2':
            register = None
            if node.children[1].node_type == 'assignment':
                register = self.assign_node(node.children[1], symbol_table)
            else:
                register = self.solve_math(node.children[1], symbol_table)
            self.store_symbol(reg_nr, register[0], symbol_type, register[1], node)

        return reg_nr, symbol_type

    def alloc_instruction(self, stars, sym_type, symbol):
        reg_nr = symbol.var_counter
        string = "{} = alloca {}{} \n".format(
            reg_nr,
            self.format_dict[sym_type], stars
        )
        self.write_to_file(string)
        symbol.written = True
        return reg_nr

    def allocate_array(self, stars, llvm_type, symbol, index_node, symbol_table):
        """
        Allocate array
        :param llvm_type: i32 / float / i8 ...
        :param size: (register, llvm_type)
        :return: register, llvm_type
        """
        register, symbol_type = self.solve_llvm_node(index_node, symbol_table)
        if symbol_type == 'int':
            ...
        elif symbol_type == 'char':
            register = self.cast_value(register, symbol_type, 'int', index_node.ctx.start)
        else:
            raise Exception("Error Line {}, Position {}: array subscript is not an integer".format(
                index_node.ctx.start.line, index_node.ctx.start.column
            ))
        try:
            size = int(register)
        except ValueError:
            raise Exception("Error Line {}, Position {}: ISO C90 forbids variable length array".format(
                index_node.ctx.start.line, index_node.ctx.start.column,
            ))
        size = register
        reg_nr = symbol.var_counter
        string = "{} = alloca [{} x {}]\n".format(
            reg_nr, register, llvm_type + stars
        )
        self.write_to_file(string)
        symbol.written = True
        symbol.size = size
        symbol.assigned = True
        return self.register, '[{} x {}]'.format(size, llvm_type)

    def allocate_global_array(self, stars, llvm_type, symbol, size):
        """
        Allocate Global Array
        :param stars:
        :param llvm_type:
        :param symbol:
        :param size:
        :return:
        """
        size = size[0]
        reg_nr = symbol.var_counter
        string = "{} = common global [{} x {}] zeroinitializer\n".format(
            reg_nr, size, llvm_type + stars
        )
        self.write_to_file(string)
        symbol.written = True
        symbol.size = size
        return self.register, '[{} x {}]'.format(size, llvm_type)

    def assign_node(self, node, symbol_table):
        expression = node.children[1]
        symbol_string = str(node.children[0].label)

        symbol = symbol_table.get_written_symbol(symbol_string, node.ctx.start)
        address = symbol.var_counter
        if node.children[1].node_type == 'assignment':
            register, symbol_type = self.assign_node(expression, symbol_table)
        else:
            register, symbol_type = self.solve_math(expression, symbol_table)

        if '[]' in str(node.children[0].label):
            # We are dealing with an array index
            address, temp = self.get_index_of_array(
                symbol.var_counter, self.format_dict[symbol_type], symbol.size,
                node.children[0].children[1], symbol_table, node.label,
                node.ctx.start
            )

        self.store_symbol(address, register, symbol.symbol_type, symbol_type, node, node.children[0].label.count('*'))
        symbol.assigned = True
        return register, symbol.symbol_type

    def not_value(self, register, symbol_type, node):
        reg = self.register
        self.register += 1
        new = self.cast_value(register, symbol_type, 'bool', node.ctx.start)
        string = "%r{} = add i1 {}, 1\n".format(reg, new)
        self.write_to_file(string)
        reg2 = self.register
        self.register += 1
        string2 = "%r{} = zext i1 %r{} to i32".format(reg2, reg)
        self.write_to_file(string2)

        return '%r' + str(reg2), 'int'

    def solve_llvm_node(self, node, symbol_table):
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

        elif node.node_type == 'include':
            self.include()

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

        elif node.node_type == 'method_declaration':
            return self.declare_method(node, symbol_table)

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

    def cast_value(self, register, current_type, new_type, error):

        current_sym_type, current_stars = get_type_and_stars(current_type)
        new_sym_type, new_stars = get_type_and_stars(new_type)
        if current_sym_type + current_stars == new_sym_type + new_stars:  # anders werkt & niet
            return register
        reg = self.register
        self.register += 1

        casted_type = self.cast_type(current_sym_type, new_sym_type, current_stars, new_stars)
        if not casted_type:
            raise_error(
                "Can't implicitely cast {} to {}".format(current_sym_type + current_stars, new_sym_type + new_stars),
                error.line, error.column
            )
        string = "%r{} = {} {}{} {} to {}{}\n".format(
            str(reg), casted_type, self.format_dict[current_sym_type], current_stars,
            register, self.format_dict[new_sym_type], new_stars
        )
        if not((current_type=="char" and (new_type =="int" or new_type =="float")) or (current_type == "int" and new_type == "float" )):
            print("[Warning] line {}: implicit cast from {} to {}".format(error.line, current_sym_type + current_stars,
                                                                      new_sym_type + new_stars))
        self.write_to_file(string)
        return '%r' + str(reg)

    def cast_type(self, current_sym_type, new_sym_type, current_stars, new_stars):
        if current_sym_type == 'void':
            raise Exception("Can't cast void")
        if len(current_stars) > 0 and len(new_stars) > 0:
            return 'bitcast'
        if len(current_stars) > 0:
            current_sym_type += '*'
            if new_sym_type == 'int':
                return 'ptrtoint'
        elif len(new_stars) > 0:
            new_sym_type += '*'
            if current_sym_type == 'int' or current_sym_type == 'char':
                return 'inttoptr'

        if current_sym_type in self.cast_dict and new_sym_type in self.cast_dict[current_sym_type]:
            return self.cast_dict[current_sym_type][new_sym_type]
        return False

    def store_symbol(self, address, value, address_symbol_type, value_symbol_type, node, dereference=0):
        address_sym_type, address_stars = get_type_and_stars(address_symbol_type)
        current_register, current_type = self.dereference(address, address_stars, address_sym_type, dereference)
        value_to_store = self.cast_value(value, value_symbol_type, current_type, node.ctx.start)

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
        return self.load_instruction(reg, stars, sym_type, symbol.var_counter)

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
            child_1 = self.cast_value(child1[0], child1[1], symbol_type, node.ctx.start)
            child_2 = self.cast_value(child2[0], child2[1], symbol_type, node.ctx.start)
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
            child_1 = self.cast_value(child1[0], child1[1], 'int', node.ctx.start)
            child_2 = self.cast_value(child2[0], child2[1], 'int', node.ctx.start)
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
            child_1 = self.cast_value(child1[0], child1[1], 'int', node.ctx.start)
            child_2 = self.cast_value(child2[0], child2[1], 'int', node.ctx.start)
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
            child_1 = self.cast_value(child1[0], child1[1], symbol_type, node.ctx.start)
            child_2 = self.cast_value(child2[0], child2[1], symbol_type, node.ctx.start)
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
            address_register = self.get_address_register(node.children[0], symbol_table)
            reg, symbol_type = self.solve_llvm_node(node.children[0], symbol_table)

            self.increment_register(reg, symbol_type, node.children[1].label, address_register, node)

            return reg, symbol_type

        elif node.node_type == 'Increment_op':
            address_register = self.get_address_register(node.children[1], symbol_table)
            reg, symbol_type = self.solve_llvm_node(node.children[1], symbol_table)

            new_register = self.increment_register(reg, symbol_type, node.children[0].label, address_register, node)

            return new_register, symbol_type

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
            if str(node.symbol_type) == "char*":
                return self.make_string(str(node.label), symbol_table), "char*"

            if str(node.symbol_type)[0] == '&':
                value = symbol_table.get_written_symbol(value, node.ctx.start).var_counter
            return value, str(node.symbol_type)

        elif node.node_type == 'lvalue':
            sym = symbol_table.get_assigned_symbol(node.label, node.ctx.start)
            sym_type, stars = get_type_and_stars(sym.symbol_type)
            address, symbol_type_stars = self.dereference(sym.var_counter, stars, sym_type,
                                                          node.label.count('*'))

            sym_type, stars = get_type_and_stars(symbol_type_stars)
            reg = self.register
            self.register += 1
            if sym.size:

                # string = "%r{} = ".format(str(reg))+ self.get_array_ptr(address, self.format_dict[sym_type]+stars, sym.size) +"\n"
                # self.write_to_file(string)
                reg, ltype = self.get_fixed_index_of_array(address, self.format_dict[sym_type] + stars, 0, sym.size)

                return reg, sym_type + stars + '*'
            else:

                return self.load_instruction(reg, stars, sym_type, address), symbol_type_stars

        elif node.node_type == 'array_element':
            sym = symbol_table.get_symbol(node.label, node.ctx.start)
            if not sym.size:
                symbol_name = re.sub(r'\[]', '', node.label)
                raise Exception("Error Line {}, Position {}: {} is not an array".format(
                    node.ctx.start.line, node.ctx.start.column, symbol_name
                ))
            sym = symbol_table.get_assigned_symbol(node.label, node.ctx.start)
            sym_type, stars = get_type_and_stars(sym.symbol_type)
            address = self.get_index_of_array(sym.var_counter, self.format_dict[sym_type] + stars, sym.size,
                                              node.children[1], symbol_table, node.label,
                                              node.ctx.start)[0]
            reg = self.register
            self.register += 1
            return self.load_instruction(reg, stars, sym_type, address), sym.symbol_type

        elif node.node_type == 'bool2' and node.children[0].label == '!':

            value = self.solve_math(node.children[1], symbol_table)
            return self.not_value(value[0], value[1], node)

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
        self.store_symbol(symbol.var_counter, '%r' + str(reg), symbol_type, symbol_type, node)
        return reg

    def increment_register(self, register, symbol_type, plusplus, address, node):
        reg = self.register
        self.register += 1
        sym_type, stars = get_type_and_stars(symbol_type)
        string = '%r{} = {} {}{} {}, 1\n'.format(
            str(reg), self.optype[symbol_type][plusplus], self.format_dict[sym_type], stars,
            register
        )
        self.write_to_file(string)
        self.store_symbol(address, '%r' + str(reg), symbol_type, symbol_type, node)
        return "%r" + str(reg)

    def call_printf(self, node, symbol_table):
        args = node.children[1].children[:]
        arg_types = []
        arg_reg = []
        arg_reg_types = []
        expected_args = []
        i = 0
        print_string = args[0].label
        while i < len(print_string) - 1:
            # print_string == printed string
            if print_string[i] == '%':
                if print_string[i + 1] == 'i':
                    expected_args += ['int']
                elif print_string[i + 1] == 'f':
                    expected_args += ['float']
                elif print_string[i + 1] == 'd':
                    expected_args += ['int']
                elif print_string[i + 1] == 'c':
                    expected_args += ['char']
                elif print_string[i + 1] == 's':
                    expected_args += ['char*']
                i += 1
            i += 1

        if len(expected_args) != len(args) - 1:
            error = node.ctx.start
            if len(expected_args) > len(args) - 1:
                raise Exception(
                    "[Error] Line {}, Position {}: Too few arguments for calling {} missing arg(s) with type(s): {}".format(
                        error.line, error.column, 'printf', ', '.join(expected_args[len(args) - 1:])
                    ))

            elif len(expected_args) < len(args) - 1:
                raise Exception(
                    "[Error] Line {}, Position {}: Too many arguments for calling {}".format(
                        error.line, error.column, 'printf'
                    ))

        for arg in args:
            reg, symbol_type = self.solve_math(arg, symbol_table)
            arg_reg.append(reg)
            arg_types.append(symbol_type)
            val, stars = get_type_and_stars(symbol_type)
            if symbol_type == "char*" and '%r' not in str(reg):
                arg_reg_types.append(
                    '{} {}'.format(self.format_dict[val] + stars, string_to_charptr(reg, symbol_table)))
            elif symbol_type == "float":
                arg_reg_types.append('{} {}'.format("double", self.float_to_double(reg)))
            else:
                arg_reg_types.append('{} {}'.format(self.format_dict[val] + stars, reg))

        newreg = self.register
        self.register += 1

        string = "%r{} = call i32 (i8*, ...) @printf(i8* {}".format(str(newreg),
                                                                    string_to_charptr(arg_reg[0], symbol_table))
        if len(args) > 1:
            string += ",{}".format(','.join(arg_reg_types[1:]))
        string += ")\n"
        self.write_to_file(string)
        return "%r" + str(newreg), "int"

    def call_scanf(self, node, symbol_table):
        args = node.children[1].children[:]
        arg_types = []
        arg_reg = []
        arg_reg_types = []
        first = True
        for arg in args:
            array = False
            if not first:
                symbol = symbol_table.get_symbol(arg.label, arg.ctx.start)
                symbol.written = True
                array = symbol.size
            reg, symbol_type = self.solve_math(arg, symbol_table)
            arg_reg.append(reg)
            arg_types.append(symbol_type)
            val, stars = get_type_and_stars(symbol_type)
            val_type = self.format_dict[val] + stars
            if array and "%r" not in str(reg):
                # reg = self.get_array_ptr(reg, self.format_dict[val], symbol.size)
                val_type = "[{} x {}]{}".format(symbol.size, self.format_dict[val], stars)

            arg_reg_types.append('{} {}'.format(val_type, reg))
            first = False

        newreg = self.register
        self.register += 1

        string = "%r{} = call i32 (i8*, ...) @__isoc99_scanf(i8* {}".format(str(newreg),
                                                                            string_to_charptr(arg_reg[0], symbol_table))
        if len(args) > 1:
            string += ",{}".format(','.join(arg_reg_types[1:]))
        string += ")\n"
        self.write_to_file(string)
        first = True
        for arg in args:
            if not first:
                symbol = symbol_table.get_symbol(arg.label, arg.ctx.start)
                symbol.assigned = True
            first = False
        return "%r" + str(newreg), "int"

    def call_method(self, node, symbol_table):
        method_name = node.children[0].label
        if method_name == "printf":
            return self.call_printf(node, symbol_table)
        if method_name == "scanf":
            return self.call_scanf(node, symbol_table)
        args = node.children[1].children[:]
        arg_types = []
        arg_reg = []
        for arg in args:
            reg, symbol_type = self.solve_math(arg, symbol_table)
            arg_reg.append(reg)
            arg_types.append(symbol_type)

        method = node.symbol_table.get_written_method(method_name, arg_types, node.ctx.start)

        if len(method.arguments) < len(arg_types):
            error = args[len(method.arguments)].ctx.start
            raise Exception("[Error] Line {}, Position {}: Too many arguments for calling {}".format(
                error.line, error.column, method_name
            ))

        elif len(method.arguments) > len(arg_types):
            if len(arg_types) > 0:
                error = args[-1].ctx.start
            else:
                error = node.ctx.start
            raise Exception(
                "[Error] Line {}, Position {}: Too few arguments for calling {} missing arg(s) with type(s): {}".format(
                    error.line, error.column, method_name, ', '.join(method.arguments[len(args):])
                )
            )

        for i, arg_type in enumerate(arg_types):
            if arg_type != method.arguments[i]:
                arg_reg[i] = self.cast_value(arg_reg[i], arg_type, method.arguments[i], node.ctx.start)
                if not arg_reg[i]:
                    error = args[i].ctx.start
                    raise Exception(
                        "[Error] Line {}, Postition {}: Argument types do not match expected {}, got {}".format(
                            error.line, error.column, method.arguments[i], arg_type
                        )
                    )

        m = list(map(self.convert2, method.arguments))
        for i in range(len(args)):
            args[i] = m[i] + ' ' + arg_reg[i]

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
        branchval = self.cast_value(switchval, switchtype, "int", node.ctx.start)

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

    def declare_method(self, method_node, symbol_table):
        args = []
        if len(method_node.children) > 2 and method_node.children[2].node_type == 'def_args':
            for arg in method_node.children[2].children:
                args.append(arg.children[0].label)
        func = symbol_table.get_method(method_node.children[1].label, args, method_node.ctx.start)
        func.written = True
        return None, None

    def generate_method(self, method_node, symbol_table):
        args = []
        if method_node.children[2].node_type == 'def_args':
            for arg in method_node.children[2].children:
                args.append(arg.children[0].label)
        func = symbol_table.get_method(method_node.children[1].label, args, method_node.ctx.start)
        func.written = True
        self.function_stack.insert(0, func)

        if not func.defined:
            raise Exception("temp")

        if len(args) != len(func.arguments):
            raise Exception("temp")

        m = list(map(self.convert2, args))
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
            val_type = get_type_and_stars(val_type)
            store_str = "store {} %{}, {}* {}\n".format(self.format_dict[val_type[0]] + val_type[1], str(i),
                                                        self.format_dict[val_type[0]] + val_type[1],
                                                        new_val)
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
        if len(self.function_stack) == 0:
            raise Exception(
                'Error at line: {} column :{} return statement outside of function '.format(node.ctx.start.line,
                                                                                            node.ctx.start.column))
        if len(node.children) == 0:
            # return void
            if self.function_stack[0].symbol_type == 'void':
                string = "ret void\n"
                self.file.write(string)
                self.write = False
                return
            else:
                raise Exception(
                    'Error at line: {} column :{} non-void function should not return void '.format(node.ctx.start.line,
                                                                                                    node.ctx.start.column))

        if self.function_stack[0].symbol_type == 'void':
            raise Exception(
                'Error at line: {} column :{} void function should not return value '.format(node.ctx.start.line,
                                                                                             node.ctx.start.column))
        returnreg, return_type = self.solve_llvm_node(node.children[0], symbol_table)
        newtype = self.function_stack[0].symbol_type
        castedreg = self.cast_value(returnreg, return_type, newtype, node.ctx.start)

        string = "ret {} {}\n".format(self.format_dict[newtype], castedreg)
        self.write_to_file(string)
        self.write = False
        return

    def get_array_ptr(self, array_register, llvm_type, size):
        string = "getelementptr inbounds ([{} x {}], [{} x {}]* {}, i32 0, i32 0)" \
            .format(size, llvm_type, size, llvm_type, array_register)
        return string

    def get_index_of_array(self, array_register, llvm_type, size, index_node, symbol_name, symbol_table, error):
        """
        :param array_register: number of register
        :param llvm_type: i32 / float / i8 ...
        :param size: int
        :param index_node: int
        :return: register, llvm_type + *
        """
        # register = size x type, size x type array_register, type 0, type index
        if not size:
            symbol_name = re.sub(r'\[]', '', symbol_name)
            raise Exception("Error Line {}, Position {}: {} is not a array".format(
                error.line, error.column, symbol_name
            ))

        register, symbol_type = self.solve_llvm_node(index_node, symbol_table)
        if symbol_type == 'int':
            ...
        elif symbol_type == 'char':
            register = self.cast_value(register, symbol_type, 'int', error)
        else:
            raise Exception("Error Line {}, Position {}: array subscript is not an integer".format(
                index_node.ctx.start.line, index_node.ctx.start.column
            ))

        return self.get_fixed_index_of_array(array_register, llvm_type, register, size)

    def get_fixed_index_of_array(self, array_register, llvm_type, index, size):
        current_reg = self.register
        self.register += 1
        string = "%r{} = getelementptr inbounds [{} x {}], [{} x {}]* {}, i32 0, i32 {}\n".format(
            current_reg, size, llvm_type, size, llvm_type, array_register, index
        )
        self.write_to_file(string)
        return "%r" + str(current_reg), llvm_type

    def include(self):
        string = "declare i32 @printf(i8 *, ...)\ndeclare i32 @__isoc99_scanf(i8*, ...)\n"
        self.write_to_file(string)

    def make_string(self, string, symbol_table):
        all_strings = symbol_table.get_strings()
        # write_string = '{} = private unnamed_addr constant [{} x i8] c"{}\\00", align 1\n'.format(all_strings[string], len(string[1:-1])+1,string[1:-1])
        # self.write_to_file(write_string)
        if string in all_strings:
            return all_strings[string]
        else:
            return None

    def define_strings(self, symbol_table):
        all_strings = symbol_table.get_strings()
        for string in all_strings:
            write_string = '{} = private unnamed_addr constant [{} x i8] c"{}\\00", align 1\n'.format(
                all_strings[string],
                len(string) + 1,
                string
            )
            self.write_to_file(write_string)
        return

    def float_to_double(self, float_reg):
        reg = self.register
        self.register += 1

        string = "%r{} = fpext float {} to double".format(str(reg), float_reg)
        self.write_to_file(string)

        return "%r" + str(reg)
