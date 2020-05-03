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
        self.instruction_section = ".text\nmain:\n"

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

    def load_immediate(self, value, destination, symbol_type):
        """
        Load Immediate Instruction
        :param value:
        :param destination:
        :return:
        """
        string = "%s %s, %s" % (mips_operators[symbol_type]['li'],destination, value)
        self.write_to_instruction(string, 2)

    def load_symbol(self, symbol, symbol_table):
        # TODO maak dit efficient
        self.allocate_mem(4, symbol_table)
        offset = str(symbol.offset)
        reg = register_dict(symbol.symbol_type,0)
        string = "%s %s, %s($sp)" % (mips_operators[symbol.symbol_type]['lw'], reg,offset)
        self.write_to_instruction(string, 2)
        string = "%s %s 0($sp)" % (mips_operators[symbol.symbol_type]['sw'], reg)
        self.write_to_instruction(string, 2)

    def load_word(self, left, right, symbol_type):
        string = "%s %s, %s" % ( mips_operators[symbol_type]['sw'], left, right)
        self.write_to_instruction(string, 2)

    def store_symbol(self, value, symbol):
        """
        Store register in frame pointer
        :param value: register
        :param symbol:
        :return:
        """
        offset = str(symbol.offset)
        string = "%s %s, %s($sp)" % (mips_operators[symbol.symbol_type]['lw'],str(value), offset)
        self.write_to_instruction(string, 2)

    def store(self, source, destination, symbol_type):
        """
        Load Word instruction
        :param source:
        :param destination:
        :return:
        """
        string = "%s %s, %s" % (mips_operators[symbol_type]['sw'],source, destination)
        self.write_to_instruction(string, 2)

    def cast_value(self, current_reg, current_type, new_type, error):
        """
        casqt a value in a register to a new register of the proper typing
        :param register:
        :param current_type:
        :param new_type:
        :param error:
        :return:
        """
        current_sym_type, current_stars = get_type_and_stars(current_type)
        new_sym_type, new_stars = get_type_and_stars(new_type)
        if current_sym_type + current_stars == new_sym_type + new_stars:  # anders werkt & niet
            return current_reg

        newreg = register_dict(new_type, int(current_reg[-1]))

        if current_type == "int" and new_type == 'float':
            string = "mtc1 %s, %s" % (current_reg, newreg)
            self.write_to_instruction(string, 2)
            string = "cvt.s.w %s, %s" % (newreg, newreg)
            self.write_to_instruction(string, 2)

        elif current_type == "float" and new_type == 'int':
            string = "cvt.w.s %s, %s" % (current_reg, current_reg)
            self.write_to_instruction(string, 2)
            string = "mfc1 %s, %s" % ( newreg, current_reg)
            self.write_to_instruction(string, 2)
        else:
            raise Exception("uninstated conversion")
        return newreg

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

    # Prints
    def print_int(self, reg):
        """
        move $a0, $t0
        li $v0, 1
        syscall
        :param reg: register to print
        :return:
        """
        if '(' in reg:
            self.load_word("$t0", reg)
            reg = "$t0"
        self.write_to_instruction("move $a0, %s" % reg, 2)
        self.write_to_instruction("li $v0, 1", 2)
        self.write_to_instruction("syscall", 2)

    def print_string(self, reg):
        if '(' in reg:
            self.load_word("$t0", reg)
            reg = "$t0"
        self.write_to_instruction("move $a0, %s" % reg, 2)
        self.write_to_instruction("li $v0, 4", 2)
        self.write_to_instruction("syscall", 2)

    def print_float(self, reg):
        """
        :param reg: Should be $f0-11
        :return:
        """
        self.write_to_instruction("mov.s $f12, %s" % reg, 2)
        self.write_to_instruction("li $v0, 2", 2)
        self.write_to_instruction("syscall", 2)

    def print_char(self, reg):
        """
        :param reg:
        :return:
        """
        if '(' in reg:
            self.load_word("$t0", reg)
            reg = "$t0"
        self.write_to_instruction("move $a0, %s" % reg, 2)
        self.write_to_instruction("li $v0, 11", 2)
        self.write_to_instruction("syscall", 2)

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
            reg = register_dict(value[1], 0)
            self.load_word(reg, value[0], value[1])
            reg = self.cast_value(reg, value[1], symbol.symbol_type, node.ctx.start)
            self.store_symbol(reg, symbol)
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
            child1 = self.solve_math(node.children[0], symbol_table)
            child2 = self.solve_math(node.children[1], symbol_table)

            # # Check if current op is allowed
            allowed_operation(child1[1], child2[1], node.label, node.ctx.start)
            symbol_type = get_return_type(child1[1], child2[1])
            #
            # # Cast if required
            self.load_word(register_dict(child2[1], 0), "0($sp)", child2[1])
            self.load_word(register_dict(child1[1], 1), "4($sp)", child1[1])

            child_1 = self.cast_value(register_dict(child1[1], 1), child1[1], symbol_type, node.ctx.start)
            child_2 = self.cast_value(register_dict(child2[1], 0), child2[1], symbol_type, node.ctx.start)


            string = "%s %s, %s, %s" % (self.optype[symbol_type][node.label], child_2, child_1, child_2)
            self.write_to_instruction(string, 2)
            self.deallocate_mem(4, symbol_table)    # Delete one
            self.store(child_2, "0($sp)", symbol_type)              # Overwrite the other

            return "0($sp)", symbol_type

        elif node.label == "/":
            child1 = self.solve_math(node.children[0], symbol_table)
            child2 = self.solve_math(node.children[1], symbol_table)

            # # Check if current op is allowed
            allowed_operation(child1[1], child2[1], node.label, node.ctx.start)
            symbol_type = get_return_type(child1[1], child2[1])
            #
            # # Cast if required
            self.load_word(register_dict(child2[1], 0), "0($sp)", child2[1])
            self.load_word(register_dict(child1[1], 1), "4($sp)", child1[1])

            child_1 = self.cast_value(register_dict(child1[1], 1), child1[1], symbol_type, node.ctx.start)
            child_2 = self.cast_value(register_dict(child2[1], 0), child2[1], symbol_type, node.ctx.start)

            if symbol_type == "float" :
                string = "div.s %s, %s, %s" % (child_2, child_1, child_2)
                self.write_to_instruction(string, 2)
                self.deallocate_mem(4, symbol_table)  # Delete one
                self.store(child_2, "0($sp)", symbol_type)  # Overwrite the other
            else:
                string = "%s %s, %s" % (self.optype['int'][node.label], child_1, child_2)
                self.write_to_instruction(string, 2)
                string = "mflo $t0"
                self.write_to_instruction(string, 2)
                self.deallocate_mem(4, symbol_table)  # Delete one
                self.store("$t0", "0($sp)",symbol_type)  # Overwrite the other

            return "0($sp)", symbol_type
        elif node.label == "%":
            child1 = self.solve_math(node.children[0], symbol_table)
            child2 = self.solve_math(node.children[1], symbol_table)

            # # Check if current op is allowed
            allowed_operation(child1[1], child2[1], node.label, node.ctx.start)
            symbol_type = get_return_type(child1[1], child2[1])
            #
            # # Cast if required
            self.load_word(register_dict(child2[1], 0), "0($sp)", child2[1])
            self.load_word(register_dict(child1[1], 1), "4($sp)", child2[1])

            child_1 = self.cast_value(register_dict(child1[1], 1), child1[1], symbol_type, node.ctx.start)
            child_2 = self.cast_value(register_dict(child2[1], 0), child2[1], symbol_type, node.ctx.start)


            string = "%s %s, %s" % (self.optype[symbol_type][node.label], child_1, child_2)
            self.write_to_instruction(string, 2)
            string = "mfhi $t0"
            self.write_to_instruction(string, 2)
            self.deallocate_mem(4, symbol_table)  # Delete one
            self.store("$t0", "0($sp)", symbol_type)  # Overwrite the other

            return "0($sp)", symbol_type

        elif node.label in ['&&', '||']:
            # Calculate values and store on stack
            child1 = self.solve_math(node.children[0], symbol_table)
            child2 = self.solve_math(node.children[1], symbol_table)
            # No cast because bitwise
            self.load_word("$t0", "0($sp)", 'int')
            self.load_word("$t1", "4($sp)", 'int')
            instruction = "and" if node.label == "&&" else "or"
            string = "%s $t0, $t1, $t0" % instruction
            self.write_to_instruction(string, 2)
            self.deallocate_mem(4, symbol_table)  # Delete one
            self.store("$t0", "0($sp)", 'int')  # Overwrite the other
            # self.print_int('$t0')
            return "0($sp)", 'int'

        elif node.label in ['==', '!=', '<', '>', '<=', '>=']:
            # Move values on stack
            child1 = self.solve_math(node.children[0], symbol_table)
            child2 = self.solve_math(node.children[1], symbol_table)

            # # Check if current op is allowed
            allowed_operation(child1[1], child2[1], node.label, node.ctx.start)
            symbol_type = get_return_type(child1[1], child2[1])
            #
            # # Cast if required
            self.load_word(register_dict(child2[1], 0), "0($sp)", child2[1])
            self.load_word(register_dict(child1[1], 1), "4($sp)", child1[1])

            child_1 = self.cast_value(register_dict(child1[1], 1), child1[1], symbol_type, node.ctx.start)
            child_2 = self.cast_value(register_dict(child2[1], 0), child2[1], symbol_type, node.ctx.start)
            # TODO Float detection
            # TODO floats mee werken

            if symbol_type == 'int':
                string = "%s $t0, $t1, $t0" % self.bool_dict['int'][node.label]
                self.write_to_instruction(string, 2)

                # Store value
                self.deallocate_mem(4, symbol_table)  # Delete one
                self.store("$t0", "0($sp)", 'int')  # Overwrite the other
                self.print_int('$t0')
                return '0($sp)', "int"

        elif node.node_type == 'Increment_var':
            reg, symbol_type = self.solve_math(node.children[0], symbol_table)

            reg = register_dict(symbol_type, 0)

            string = "%s %s, %s, 1" % (self.optype[symbol_type][node.children[1].label], reg, reg)

            self.write_to_instruction(string, 2)

            sym = symbol_table.get_written_symbol(node.children[0].label, node.ctx.start)
            self.store_symbol(reg, sym)
            return reg, symbol_type

        elif node.node_type == 'Increment_op':
            address_register = self.get_address_register(node.children[1], symbol_table)
            reg, symbol_type = self.solve_math(node.children[0], symbol_table)

            reg = register_dict(symbol_type, 0)

            string = "%s %s, %s, 1" % (self.optype[symbol_type][node.children[1].label], reg, reg)

            self.write_to_instruction(string, 2)

            sym = symbol_table.get_written_symbol(node.children[0].label, node.ctx.start)
            self.store_symbol(reg, sym)

            self.store(reg, '0($sp)', symbol_type)

            return reg, symbol_type

        elif node.node_type == 'unary plus':
            return self.solve_math(node.children[1], symbol_table)

        elif node.node_type == 'unary min':
            value = self.solve_math(node.children[1], symbol_table)
            reg = register_dict(value[1],0)
            self.load_word(reg, '0($sp)', value[1])
            string = "%s %s" % (mips_operators[value[1]]['neg'], reg)
            self.write_to_instruction(string, 2)

            self.store(reg, '0($sp)', value[1])

            return reg, value[1]



            # reg = self.register
            # self.register += 1
            # string = "%r{} = {} {} {}, {}\n".format(
            #     reg, self.optype[value[1]]['-'], self.format_dict[value[1]], self.null[value[1]], value[0]
            # )
            # self.write_to_file(string)
            # return '%r' + str(reg), value[1]

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
            reg = register_dict(str(node.symbol_type), 0)
            self.load_immediate(value, reg, str(node.symbol_type))
            self.store(reg, "0($sp)", str(node.symbol_type))

            return "0($sp)", str(node.symbol_type)

        elif node.node_type == 'lvalue':
            # TODO Check array, check address
            symbol = symbol_table.get_assigned_symbol(node.label, node.ctx.start)
            self.load_symbol(symbol, symbol_table)
            return "0($sp)", str(symbol.symbol_type)

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

