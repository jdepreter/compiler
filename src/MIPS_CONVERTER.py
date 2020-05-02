from src.CustomExceptions import *
from src.helperfuncs import get_type_and_stars, get_return_type, allowed_operation
from src.MIPS_Operations import *


class MIPS_Converter:
    def __init__(self, ast, file):
        self.ast = ast
        self.stack = []
        self.register = 0
        self.label = 0
        self.write = True
        self.breaks = False
        self.break_stack = []
        self.continue_stack = []
        self.file = file
        self.optype = optype
        self.bool_dict = bool_dict
        self.temp_used_registers = []

        self.data_section = ".data\n"
        self.instruction_section = ".text\n"

    def write_to_file(self, string: str):
        """
        Write a single line with a set indentation
        :param string: line
        :return:
        """
        self.file.write(string + "\n")

    def write_to_data(self, string: str):
        """
        Adds to MIPS .data section
        .data
            [var_name]:   .word   [init value]
        :return:
        """
        if self.write:
            self.data_section += "  " + string + "\n"

    def write_to_instruction(self, string: str, indentation: int = 0):
        """
        Adds to MIPS .text section
        """
        indent = "".join([" " for i in range(indentation)])
        if self.write:
            self.instruction_section += indent + string + "\n"

    def define_strings(self, symbol_table):
        """
        Add all strings to data section
        :param symbol_table:
        :return:
        """
        all_strings = symbol_table.get_mips_strings()
        for string_value, var_name in all_strings.items():
            self.write_to_data('%s: .asciiz "%s"' % (var_name, string_value))

        return

    def allocate_mem(self, amount, symbol_table):
        """
        Create space for variable
        Stack grows downwards
        to use this mem spot access 0($sp)
        to use previous mem spot 4($sp)
        :return:
        """
        string = "addiu $sp, $sp, -%d" % amount   # Reserve word on stack
        self.write_to_instruction(string, 2)
        # Increase offset of previous variables in stack (offset can never be < 0)
        symbol_table.increase_offset(amount)

    def deallocate_mem(self, amount, symbol_table):
        """
        When closing scope, deallocate space used in this scope
        Also used when calculating expressions
        :param amount: amount of variables in this scope
        :return:
        """
        string = "addiu $sp, $sp, %d" % amount  # Reserve word on stack
        self.write_to_instruction(string, 2)
        # Decrease offset of previous variables in stack
        symbol_table.decrease_offset(amount)

    def load_immediate(self, value, destination):
        """
        Load Immediate Instruction
        :param value:
        :param destination:
        :return:
        """
        string = "li %s, %s" % (destination, value)
        self.write_to_instruction(string, 2)

    def load_symbol(self, symbol, symbol_table):
        self.allocate_mem(4, symbol_table)
        offset = str(symbol.offset)
        string = "lw $sp, %s($sp)" % offset
        self.write_to_instruction(string, 2)

    def load_word(self, left, right):
        string = "lw %s, %s" % (left, right)
        self.write_to_instruction(string, 2)

    def store_symbol(self, value, symbol):
        """
        Store register in frame pointer
        :param value: register
        :param symbol:
        :return:
        """
        offset = str(symbol.offset)
        string = "sw %s, %s($sp)" % (str(value), offset)
        self.write_to_instruction(string, 2)

    def store(self, source, destination):
        """
        Load Word instruction
        :param source:
        :param destination:
        :return:
        """
        string = "sw %s, %s" % (source, destination)
        self.write_to_instruction(string, 2)

    # JUMPS
    def go_to_label(self, label):
        """
        go to a label
        :param label:
        :return:
        """
        string = "j label{}\n".format(label)
        self.write_to_instruction(string)

    def go_to_label_linked(self, label):
        """
        jumps to a label and stores current pc in $ra
        :param label:
        :return:
        """
        string = "jal label{}".format(label)
        self.write_to_instruction(string)

    def go_to_register(self, reg):
        """
        jumps to the number in a given register (mainly used for $ra)
        :param reg:
        :return:
        """
        string = "jr {}".format(reg)
        self.write_to_instruction(string)

    def to_mips(self):
        """
        Generate MIPS Assembly
        :return:
        """
        current_symbol_table = self.ast.startnode.symbol_table
        self.define_strings(current_symbol_table)

        self.solve_node(self.ast.startnode, self.ast.startnode.symbol_table)

        self.write_to_file(self.data_section)
        self.write_to_file(self.instruction_section)
        # self.solve_llvm_node(self.ast.startnode, current_symbol_table)

    def allocate_symbol(self, symbol, symbol_table):
        """
        Allocate space for a variable
        :param symbol:
        :param symbol_table:
        :return:
        """
        self.allocate_mem(4, symbol_table)
        symbol.written = True

    def solve_node(self, node, symbol_table):
        if node.symbol_table is not None:
            symbol_table = node.symbol_table

        if node.node_type == 'definition':
            typing = node.children[0]
            varstart = 1
            if typing.node_type == 'const':
                typing = node.children[1]
                varstart = 2
            for i in range(varstart, len(node.children)):
                # address, symbol_type = self.allocate_node(node.children[i], symbol_table, typing.label)
                self.allocate_node(node.children[i], symbol_table)
            # return address, symbol_type
        else:
            for child in node.children:
                if node.symbol_table is not None:
                    symbol_table = node.symbol_table

                self.solve_node(child, symbol_table)
        # elif node.node_type == 'include':
        #     self.include()
        #
        # elif node.node_type == 'assignment':
        #     return self.assign_node(node, symbol_table)
        #
        # elif node.node_type == 'for':
        #     return self.loop(node, symbol_table)
        #
        # elif node.node_type == 'for break':
        #     if len(self.break_stack) > 0:
        #         self.go_to_label(self.break_stack[0])
        #         self.write = False
        #         self.breaks = True
        #         return None, None
        #     else:
        #         raise BreakError("[Error] Line {} Position {} break statement not within loop or switch".format(
        #             node.ctx.start.line, node.ctx.start.column
        #         ))
        #
        # elif node.node_type == 'for continue':
        #     if len(self.continue_stack) > 0:
        #         self.go_to_label(self.continue_stack[0])
        #         self.write = False
        #         return None, None
        #     else:
        #         raise BreakError("[Error] Line {} Position {} continue statement not within loop".format(
        #             node.ctx.start.line, node.ctx.start.column
        #         ))
        #
        # elif node.node_type == "switch":
        #     return self.switch(node, symbol_table)
        #
        # elif node.node_type == 'ifelse':
        #     return self.if_else(node, symbol_table)
        #
        # elif node.node_type == 'method_declaration':
        #     return self.declare_method(node, symbol_table)
        #
        # elif node.node_type == 'method_definition':
        #     return self.generate_method(node, symbol_table)
        #
        # elif node.node_type == 'return':
        #     return self.return_node(node, symbol_table)
        # else:
        #     sol = self.solve_math(node, symbol_table)
        #
        #     if sol[0] is None:
        #         for child in node.children:
        #             if node.symbol_table is not None:
        #                 symbol_table = node.symbol_table
        #
        #             sol = self.solve_llvm_node(child, symbol_table)
        #     return sol

    def allocate_node(self, node, symbol_table):
        variable = node.label
        if node.node_type in ['assignment2', 'array']:
            variable = node.children[0].label

        # if node.node_type == 'Arg_definition':
        #     variable = node.children[1].label

        symbol = symbol_table.get_symbol(variable, node.ctx.start)

        # if symbol.is_global:
        #     # Do funny xD llvm global stuff
        #     if node.node_type == 'array':
        #         reg_nr = self.allocate_global_array(stars, self.format_dict[sym_type], symbol,
        #                                             self.solve_math(node.children[1], symbol_table))[0]
        #         return None, None
        #     value = 0
        #     if node.node_type == 'assignment2':
        #         if node.children[1].node_type == 'rvalue':
        #             value = node.children[1].label
        #         else:
        #             raise Exception("Initializer element is not constant")
        #
        #     self.write_to_file("{} = global {} {}\n".format(symbol.current_register, self.format_dict[sym_type], value))
        #     symbol.written = True
        #     return None, None

        # if node.node_type == 'array':
        #     reg_nr = self.allocate_array(stars, self.format_dict[sym_type], symbol,
        #                                  node.children[1], symbol_table)[0]
        # else:
        #     reg_nr = self.alloc_instruction(stars, sym_type, symbol)

        self.allocate_symbol(symbol, symbol_table)  # Remove L8er

        if node.node_type == 'assignment2':
            self.assign_node(node, symbol_table)

        return symbol

    def assign_node(self, node, symbol_table):
        """
        Assign a value to the symbol in node: node
        :param node: node containing symbol
        :param symbol_table: scope of node
        :return:
        """
        symbol_string = str(node.children[0].label)
        symbol = symbol_table.get_written_symbol(symbol_string, node.ctx.start)

        if node.children[1].node_type == 'assignment':
            value = self.assign_node(node.children[1], symbol_table)
        else:
            value = self.solve_math(node.children[1], symbol_table)
            self.load_word("$t0", value)
            self.store_symbol("$t0", symbol)
            self.deallocate_mem(4, symbol_table)

        # if '[]' in str(node.children[0].label):
        #     # We are dealing with an array index
        #     address, temp = self.get_index_of_array(
        #         symbol.var_counter, self.format_dict[symbol_type], symbol.size,
        #         node.children[0].children[1], symbol_table, node.label,
        #         node.ctx.start
        #     )
        symbol.assigned = True
        return value

    def solve_math(self, node, symbol_table):
        """
        load vars in temp register,
        store result on stack,
        deallocate when used
        :param node:
        :param symbol_table:
        :return:
        """
        string = ''
        if node.label in ['+', '-', '*']:
            # Calculate values and store on stack
            child1 = self.solve_math(node.children[0], symbol_table)
            child2 = self.solve_math(node.children[1], symbol_table)

            # # Check if current op is allowed
            # allowed_operation(child1[1], child2[1], node.label, node.ctx.start)
            # symbol_type = get_return_type(child1[1], child2[1])
            #
            # # Cast if required
            # child_1 = self.cast_value(child1[0], child1[1], symbol_type, node.ctx.start)
            # child_2 = self.cast_value(child2[0], child2[1], symbol_type, node.ctx.start)

            self.load_word("$t0", "0($sp)")
            self.load_word("$t1", "4($sp)")
            string = "%s $t0, $t1, $t0" % self.optype['int']['+']
            self.write_to_instruction(string, 2)
            self.deallocate_mem(4, symbol_table)    # Delete one
            self.store("$t0", "0($sp)")              # Overwrite the other

            return "0($sp)"

        elif node.label in ["/", "%"]:
            ...
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

        # elif node.node_type == 'method_call':
        #     return self.call_method(node, symbol_table)

        elif node.node_type == 'rvalue':
            value = str(node.label)
            # if str(node.symbol_type) == "float":
            #     value = self.store_float(float(node.label))
            # if str(node.symbol_type) == "char*":
            #     return self.make_string(str(node.label), symbol_table), "char*"
            #
            # if str(node.symbol_type)[0] == '&':
            #     value = symbol_table.get_written_symbol(value, node.ctx.start).var_counter
            self.allocate_mem(4, symbol_table)
            self.load_immediate(value, "$t0")
            self.store("$t0", "0($sp)")

            return "0($sp)"

        elif node.node_type == 'lvalue':
            # TODO Check array, check address
            symbol = symbol_table.get_assigned_symbol(node.label, node.ctx.start)
            self.load_symbol(symbol, symbol_table)
            return "0($sp)"

        # elif node.node_type == 'array_element':
        #     sym = symbol_table.get_symbol(node.label, node.ctx.start)
        #     if not sym.size:
        #         symbol_name = re.sub(r'\[]', '', node.label)
        #         raise Exception("Error Line {}, Position {}: {} is not an array".format(
        #             node.ctx.start.line, node.ctx.start.column, symbol_name
        #         ))
        #     sym = symbol_table.get_assigned_symbol(node.label, node.ctx.start)
        #     sym_type, stars = get_type_and_stars(sym.symbol_type)
        #     address = self.get_index_of_array(sym.var_counter, self.format_dict[sym_type] + stars, sym.size,
        #                                       node.children[1], symbol_table, node.label,
        #                                       node.ctx.start)[0]
        #     reg = self.register
        #     self.register += 1
        #     return self.load_instruction(reg, stars, sym_type, address), sym.symbol_type

        elif node.node_type == 'bool2' and node.children[0].label == '!':

            value = self.solve_math(node.children[1], symbol_table)
            return self.not_value(value[0], value[1], node)

        return None, None

