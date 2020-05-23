from src.CustomExceptions import *
from src.helperfuncs import get_type_and_stars, get_return_type, allowed_operation
from src.MIPS_Operations import *
from src.AST import *
from src.symbolTables import *
from src.MIPS_Offset import MIPSOffset
from copy import deepcopy


def get_string(string: str, symbol_table: SymbolTable):
    """
    Retrun MIPS label (address) for the given string
    :param string:
    :param symbol_table:
    :return:
    """
    all_strings = symbol_table.get_mips_strings()
    if string in all_strings:
        return all_strings[string]
    return None


class MIPS_Converter:
    def __init__(self, ast: ASTVisitor, file):
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
        self.function_stack = []
        self.floatp = 0
        self.float_branches = 0
        self.allocation_stack = [0]
        self.offset_stack = [MIPSOffset()]
        self.loop_stacksize = []
        self.in_loop = False    # Determines if break is for switch case or for loop
        self.func_stacksize = []

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

    def write_comment(self, string: str, indentation: int = 0):
        """
        Write a comment to the .text section
        """
        indent = "".join([" " for _ in range(indentation)])
        if self.write:
            self.instruction_section += indent + '# ' + string + "\n"

    def write_to_instruction(self, string: str, indentation: int = 0, comment: str = ''):
        """
        Adds to MIPS .text section
        """
        indent = "".join([" " for _ in range(indentation)])
        if self.write:
            self.instruction_section += indent + string + " # " + comment + "\n"

    def define_strings(self, symbol_table: SymbolTable):
        """
        Add all strings to data section
        :param symbol_table:
        :return:
        """
        all_strings = symbol_table.get_mips_strings()
        for string_value, var_name in all_strings.items():
            self.write_to_data('%s: .asciiz "%s"' % (var_name, string_value))

        return

    def allocate_mem(self, amount, symbol_table: SymbolTable, comment: str = ''):
        """
        Create space for variable
        Stack grows downwards
        to use this mem spot access 0($sp)
        to use previous mem spot 4($sp)
        :return:
        """
        self.allocation_stack[0] += amount
        string = "addiu $sp, $sp, -%d" % amount  # Reserve word on stack
        self.write_to_instruction(string, 2, comment)
        # Increase offset of previous variables in stack (offset can never be < 0)
        self.offset_stack[0].increase_offset(amount)

    def deallocate_mem(self, amount, symbol_table: SymbolTable, comment: str = ''):
        """
        When closing scope, deallocate space used in this scope
        Also used when calculating expressions
        :param amount: amount of variables in this scope
        :param symbol_table:
        :param comment:
        :return:
        """
        self.allocation_stack[0] -= amount
        string = "addiu $sp, $sp, %d" % amount  # Reserve word on stack
        self.write_to_instruction(string, 2, comment)
        # Decrease offset of previous variables in stack
        self.offset_stack[0].decrease_offset(amount)

    def load_immediate(self, value, destination, symbol_type):
        """
        Load Immediate Instruction
        :param value:
        :param destination:
        :param symbol_type:
        :return:
        """
        if symbol_type == "float":
            float_Str = "fp%d" % self.floatp
            self.write_to_data("%s: .float %s" % (float_Str, value))
            string = "l.s %s %s" % (destination, float_Str)
            self.write_to_instruction(string, 2)
            self.floatp += 1
        else:
            # string = "%s %s, %s" % (mips_operators[symbol_type]['li'], destination, value)
            string = "li %s, %s" % (destination, value)
            self.write_to_instruction(string, 2)

    def load_symbol(self, symbol: SymbolType, symbol_table: SymbolTable):
        # TODO maak dit efficient
        self.allocate_mem(4, symbol_table, comment="Allocate for %s" % symbol.name)
        offset = self.offset_stack[0].get_offset(symbol)
        self.put_on_top_of_stack("%s($sp)" % offset, symbol.symbol_type)

    def put_on_top_of_stack(self, stack_pointer: str, symbol_type: str):
        operator_type = get_operator_type(symbol_type)
        reg = register_dict(symbol_type, 0)

        # Load instruction from the stack
        string = "%s %s, %s" % (mips_operators[operator_type]['lw'], reg, stack_pointer)
        self.write_to_instruction(string, 2, comment='Put on top of stack load')

        # Put it on top of the stack
        string = "%s %s, 0($sp)" % (mips_operators[operator_type]['sw'], reg)
        self.write_to_instruction(string, 2, comment='Put on top of stack save')

    def load_word(self, left: str, right: str, symbol_type: str, comment: str = ''):
        if left != right:
            operator_type = get_operator_type(symbol_type)
            string = "%s %s, %s" % (mips_operators[operator_type]['lw'], left, right)
            self.write_to_instruction(string, 2, comment)

    def load_address(self, left, right, comment: str = ''):
        """
        Load the address of register right into register left
        :param left:
        :param right: address of some kind
        :return:
        """
        if left != right:
            string = "la %s, %s" % (left, right)
            self.write_to_instruction(string, 2, comment)

    def store_symbol(self, value, symbol: SymbolType, comment: str = ''):
        """
        Store register in stack pointer
        :param value: register
        :param symbol:
        :return:
        """
        if symbol.is_global:
            self.load_address("$t9", "global_%s%d"%(symbol.name, symbol.reg), "load in global .data address")
            operator_type = get_operator_type(symbol.symbol_type)
            string = "%s %s, 0($t9)" % (mips_operators[operator_type]['sw'], str(value))
            self.write_to_instruction(string, 2, comment)
        else:
            offset = self.offset_stack[0].get_offset(symbol)
            operator_type = get_operator_type(symbol.symbol_type)
            string = "%s %s, %s($sp)" % (mips_operators[operator_type]['sw'], str(value), offset)
            self.write_to_instruction(string, 2, comment)

    def store(self, source, destination, symbol_type, comment: str = ''):
        """
        Load Word instruction
        :param source:
        :param destination:
        :param symbol_type:
        :return:
        """
        operator_type = get_operator_type(symbol_type)
        string = "%s %s, %s" % (mips_operators[operator_type]['sw'], source, destination)
        self.write_to_instruction(string, 2, comment)

    def move(self, left, right, comment: str = ''):
        """
        Set content of left to right
        :param left: is changed
        :param right: is not changed
        :param comment:
        :return:
        """
        self.write_to_instruction("move %s %s" % (left, right), 2, comment)

    def cast_value(self, current_reg, current_type, new_type, error):
        """
        casqt a value in a register to a new register of the proper typing
        :param current_reg:
        :param current_type:
        :param new_type:
        :param error:
        :return:
        """
        current_sym_type, current_stars = get_type_and_stars(current_type)
        new_sym_type, new_stars = get_type_and_stars(new_type)
        if current_sym_type + current_stars == new_sym_type + new_stars:  # anders werkt & niet
            return current_reg
        elif current_type in ["int", "char"] and new_type in ["int", "char"]:
            return current_reg

        newreg = register_dict(new_type, int(current_reg[-1]))

        if current_type in ["int", "char"] and new_type == 'float':
            string = "mtc1 %s, %s" % (current_reg, newreg)
            self.write_to_instruction(string, 2)
            string = "cvt.s.w %s, %s" % (newreg, newreg)
            self.write_to_instruction(string, 2)

        elif current_type == "float" and new_type in ["int", "char"]:
            string = "cvt.w.s %s, %s" % (current_reg, current_reg)
            self.write_to_instruction(string, 2)
            string = "mfc1 %s, %s" % (newreg, current_reg)
            self.write_to_instruction(string, 2)



        elif '*' in current_type and new_type == 'int':
            # Pointer to int does not need any conversion
            ...

        else:
            raise Exception("uninstated conversion")
        return newreg

    # JUMPS
    def write_label(self, label):
        self.write_to_instruction(label + ':', 0)

    def go_to_label(self, label):
        """
        go to a label
        :param label:
        :return:
        """
        string = "j {}\n".format(label)
        self.write_to_instruction(string)

    def add_label(self, labelnr):
        string = "label%d:" % labelnr
        self.write_to_instruction(string, 0)

    def go_to_label_linked(self, label):
        """
        jumps to a label and stores current pc in $ra
        :param label:
        :return:
        """
        string = "jal {}".format(label)
        self.write_to_instruction(string)

    def go_to_label_conditional(self, register: str, label: str):
        """
        First get the result of the condition
        Then use this to jump to else part
        :param register: register will be compared to zero
        :param label: else label
        :return:
        """
        string = "beq %s, $0, %s" % (register, label)
        self.write_to_instruction(string, 2)

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
            self.load_word("$t0", reg, "int", comment='Load int for printing')
            reg = "$t0"
        self.write_to_instruction("move $a0, %s" % reg, 2)
        self.write_to_instruction("li $v0, 1", 2)
        self.write_to_instruction("syscall", 2)

    def print_string(self, reg):
        if '(' in reg:
            self.load_word("$t0", reg, "char*", comment='Load string for printing')
            reg = "$t0"
        self.write_to_instruction("la $a0, %s" % reg, 2)  # String from data segment use la
        self.write_to_instruction("li $v0, 4", 2)
        self.write_to_instruction("syscall", 2)

    def print_float(self, reg):
        """
        :param reg: Should be $f0-11
        :return:
        """
        # self.write_to_instruction("mov.s $f12, %s" % reg, 2)
        self.load_word("$f12", reg, "float")
        self.write_to_instruction("li $v0, 2", 2)
        self.write_to_instruction("syscall", 2)

    def print_char(self, reg):
        """
        :param reg:
        :return:
        """
        if '(' in reg:
            self.load_word("$t0", reg, "char", comment='Load char for printing')
            reg = "$t0"
        self.write_to_instruction("move $a0, %s" % reg, 2)
        self.write_to_instruction("li $v0, 11", 2)
        self.write_to_instruction("syscall", 2)

    # Node Solvers
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

    def allocate_symbol(self, symbol: SymbolType, symbol_table: SymbolTable):
        """
        Allocate space for a variable
        :param symbol:
        :param symbol_table:
        :return:
        """
        self.allocate_mem(4, symbol_table, comment='Allocate space for symbol: %s' % symbol.name)
        symbol.written = True
        self.offset_stack[0].add_symbol(symbol)

    def solve_node(self, node: Node, symbol_table: SymbolTable):
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
                self.allocate_node(node.children[i], symbol_table), True
            # return address, symbol_type

        elif node.node_type == 'method_declaration':
            return self.declare_method(node, symbol_table), True

        elif node.node_type == 'method_definition':
            return self.generate_method(node, symbol_table), True

        elif node.node_type in ["Increment_var", "Increment_op", "unary plus", "unary min", 'rvalue',
                                'lvalue', 'bool2'] \
                or node.label in ['+', '-', '*', '/', '%', '&&', '||', '==', '!=', '<', '>', '<=', '>=']:

            register, value_type, not_pointer = self.solve_math(node, symbol_table)
            reg = '$t0'
            if value_type is not None and value_type != 'void':
                reg = register_dict(value_type, 0)

                self.load_word(reg, "0($sp)", value_type)
            self.deallocate_mem(4, symbol_table, comment='Deallocate space used for solve math')
            return reg, value_type, not_pointer

        elif node.node_type == 'method_call':
            register, value_type, not_pointer = self.solve_math(node, symbol_table)
            reg = '$t0'
            if value_type is not None and value_type != 'void':
                reg = register_dict(value_type, 0)

                self.load_word(reg, "0($sp)", value_type)
            self.deallocate_mem(4, symbol_table, comment='Deallocate space used for method call')
            return reg, value_type, not_pointer

        elif node.node_type == 'ifelse':
            return self.if_else(node, symbol_table), True

        # elif node.node_type == 'include':
        #     self.include()
        #
        elif node.node_type == 'assignment':
            return self.assign_node(node, symbol_table)
        #
        elif node.node_type == 'for':
            return self.loop(node, symbol_table)
        #
        elif node.node_type == 'for break':
            if len(self.break_stack) > 0:
                if self.in_loop:
                    self.leave_stack(symbol_table, len(self.allocation_stack) - self.loop_stacksize[0], False)
                self.go_to_label(self.break_stack[0])
                self.write = False
                self.breaks = True
                return None, None, None
            else:
                raise BreakError("[Error] Line {} Position {} break statement not within loop or switch".format(
                    node.ctx.start.line, node.ctx.start.column
                ))

        elif node.node_type == 'for continue':
            if len(self.continue_stack) > 0:

                self.leave_stack(symbol_table, len(self.allocation_stack) - self.loop_stacksize[0], False)
                self.go_to_label(self.continue_stack[0])
                self.write = False
                return None, None, None
            else:
                raise BreakError("[Error] Line {} Position {} continue statement not within loop".format(
                    node.ctx.start.line, node.ctx.start.column
                ))
        #
        elif node.node_type == "switch":
            return self.switch(node, symbol_table), True

        elif node.node_type == 'return':
            return self.return_node(node, symbol_table)

        elif node.node_type == 'scope':
            self.enter_stack(symbol_table)
            # Run the scope
            for child in node.children:
                self.solve_node(child, symbol_table)

            self.leave_stack(symbol_table), True

        else:
            sol = self.solve_math(node, symbol_table)

            if sol[0] is None:
                for child in node.children:
                    sol = self.solve_node(child, symbol_table)
            return sol

    def enter_stack(self, symbol_table):
        self.allocation_stack.insert(0, 0)
        self.offset_stack.insert(0, MIPSOffset(self.offset_stack[0].symbols))
        write = self.write
        self.write = True
        # Save old frame pointer
        self.write_comment("Entering new stack...")
        self.allocate_mem(4, symbol_table, comment="Allocate mem for previous frame pointer")
        self.store("$fp", "0($sp)", "int", comment="Save previous frame pointer on stack")
        # Set new frame pointer
        self.move("$fp", "$sp", comment="Save current stack pointer in frame pointer")
        self.write_comment("Entered Stack")
        self.write = write

    def leave_stack(self, symbol_table, amount=1, pop=True):

        stacks1 = []
        stacks2 = []
        write = self.write
        self.write = True
        for i in range(amount):
            self.write_comment("Leaving Stack...")
            diff = self.allocation_stack[0]
            offset = deepcopy(self.offset_stack[0])
            # Reset stack pointer
            # self.write_to_instruction("sub $t0, $fp, $sp", 2, comment="Calculate diff between frame and stack pointer")
            # self.write_to_instruction("addi $sp, $sp, %s" % diff, 2, comment="Deallocate stack")
            self.deallocate_mem(diff - 4, symbol_table, "Deallocate stack")  # Diff - 4 wegens frame pointer gealloceerd
            # Load old frame pointer
            self.load_word("$fp", "0($sp)", "int", comment="Load previous frame pointer")
            # Deallocate space from frame pointer
            self.deallocate_mem(4, symbol_table, comment="Deallocate space for old frame pointer")
            temp = self.allocation_stack[0]
            if temp != 0:
                raise Exception("Not properly deallocated stack")
            if not pop:
                self.allocation_stack[0] = diff
                self.offset_stack[0] = offset
            stacks1.insert(0, self.allocation_stack.pop(0))
            stacks2.insert(0, self.offset_stack.pop(0))
        if not pop:
            for i in range(amount):
                self.allocation_stack.insert(0, stacks1[i])
                self.offset_stack.insert(0, stacks2[i])

        self.write_comment("Left stack")
        self.write = write

    def allocate_node(self, node: Node, symbol_table: SymbolTable):
        variable = node.label
        if node.node_type in ['assignment2', 'array']:
            variable = node.children[0].label
        elif node.node_type == "Arg_definition":
            variable = node.children[1].label
        # if node.node_type == 'Arg_definition':
        #     variable = node.children[1].label

        symbol = symbol_table.get_symbol(variable, node.ctx.start)

        if symbol.is_global:
            # Do funny xD asm global stuff
            if node.node_type == 'array':
                raise Exception("Arrays not yet made global")
                reg_nr = self.allocate_global_array(stars, self.format_dict[sym_type], symbol,
                                                    self.solve_math(node.children[1], symbol_table))[0]
                return None, None
            value = 0
            if node.node_type == 'assignment2':
                if node.children[1].node_type == 'rvalue':
                    value = node.children[1].label
                else:
                    raise Exception("Initializer element is not constant")

            string = "global_%s%d: %s %s" %(symbol.name, symbol.reg, mips_globals[symbol.symbol_type], value)
            self.write_to_data(string)
            symbol.written = True
            return None, None

        # if node.node_type == 'array':
        #     reg_nr = self.allocate_array(stars, self.format_dict[sym_type], symbol,
        #                                  node.children[1], symbol_table)[0]
        # else:
        #     reg_nr = self.alloc_instruction(stars, sym_type, symbol)

        self.allocate_symbol(symbol, symbol_table)  # Remove L8er

        if node.node_type == 'assignment2':
            self.assign_node(node, symbol_table)

        return symbol

    def assign_node(self, node: Node, symbol_table: SymbolTable):
        """
        Assign a value to the symbol in node: node
        :param node: node containing symbol
        :param symbol_table: scope of node
        :return: register, type, is_address
        """
        symbol_string = str(node.children[0].label)
        symbol = symbol_table.get_written_symbol(symbol_string, node.ctx.start)
        symbol_type = symbol.symbol_type

        if node.children[1].node_type == 'assignment':
            value = self.assign_node(node.children[1], symbol_table)
        else:
            # Check if array
            address = None
            if '[]' in str(node.children[0].label):
                # TODO array element getter
                ...
            # Dereference if needed
            # TODO hier zit nog een fout met pointers en stuff
            if '*' in str(node.children[0].label):
                self.allocate_mem(4, symbol_type, comment="Space for dereferenced value")
                dereference_count = symbol_string.count('*')
                pointer_reg = "%s($sp)" % self.offset_stack[0].get_offset(symbol) if address is None else address
                address = self.dereference(pointer_reg, dereference_count,
                                       node.children[0].symbol_type.symbol_type[0:-dereference_count])
                symbol_type = symbol_type[:-dereference_count]
                self.move("$t2", address, comment="$t0 will be overwritten be solve math")
                address = "0($t2)"

            value = self.solve_math(node.children[1], symbol_table)
            reg = register_dict(value[1], 0)

            self.load_word(reg, value[0], value[1])
            reg = self.cast_value(reg, value[1], symbol_type, node.ctx.start)
            if address is None:
                self.store_symbol(reg, symbol, "Assigning to %s" % symbol.name)

            else:
                self.store(reg, address, symbol_type, comment="Store value at dereferenced pointer")
            self.deallocate_mem(4, symbol_table, comment='deallocate solve math')
            if symbol.is_global:
                return "global_%s%d" %(symbol.name, symbol.reg),symbol.symbol_type
            return "%s($sp)" % self.offset_stack[0].get_offset(symbol), symbol.symbol_type, address is None

        # if '[]' in str(node.children[0].label):
        #     # We are dealing with an array index
        #     address, temp = self.get_index_of_array(
        #         symbol.var_counter, self.format_dict[symbol_type], symbol.size,
        #         node.children[0].children[1], symbol_table, node.label,
        #         node.ctx.start
        #     )
        symbol.assigned = True
        return value

    def solve_math(self, node: Node, symbol_table: SymbolTable):
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
            # Load from address if required

            #
            # # Cast if required
            self.load_word(register_dict(child2[1], 0), "0($sp)", child2[1])
            self.load_word(register_dict(child1[1], 1), "4($sp)", child1[1])

            child_1 = self.cast_value(register_dict(child1[1], 1), child1[1], symbol_type, node.ctx.start)
            child_2 = self.cast_value(register_dict(child2[1], 0), child2[1], symbol_type, node.ctx.start)

            string = "%s %s, %s, %s" % (self.optype[symbol_type][node.label], child_2, child_1, child_2)
            self.write_to_instruction(string, 2)
            self.deallocate_mem(4, symbol_table)  # Delete one
            self.store(child_2, "0($sp)", symbol_type)  # Overwrite the other

            return "0($sp)", symbol_type, True

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

            if symbol_type == "float":
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
                self.store("$t0", "0($sp)", symbol_type)  # Overwrite the other

            return "0($sp)", symbol_type, True

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

            return "0($sp)", symbol_type, True

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
            return "0($sp)", 'int', True

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

            # TODO floats >, >= testen

            if symbol_type == 'float':
                string = "%s %s, %s" % (self.bool_dict[symbol_type][node.label], child_1, child_2)
                self.write_to_instruction(string, 2)

                self.write_to_instruction("bc1f L_CondFalse%d" % self.float_branches, 2)
                self.write_to_instruction("li $t0, 0", 2)
                self.write_to_instruction("j L_CondEnd%d" % self.float_branches, 2)
                self.write_to_instruction("L_CondFalse%d:" % self.float_branches, 0)
                self.write_to_instruction("li $t0, 1", 2)
                self.write_to_instruction("L_CondEnd%d:" % self.float_branches, 0)

                # Store value
                self.deallocate_mem(4, symbol_table)  # Delete one
                self.store("$t0", "0($sp)", 'int')  # Overwrite the other
                self.float_branches += 1
                # self.print_int('$t0')
                return '0($sp)', "int", True

            else:
                string = "%s $t0, $t1, $t0" % (self.bool_dict[symbol_type][node.label])
                self.write_to_instruction(string, 2)

                # Store value
                self.deallocate_mem(4, symbol_table)  # Delete one
                self.store("$t0", "0($sp)", 'int')  # Overwrite the other
                # self.print_int('$t0')
                return '0($sp)', "int", True

        elif node.node_type == 'Increment_var':
            address, symbol_type, not_pointer = self.solve_math(node.children[0], symbol_table)

            reg = register_dict(symbol_type, 0)
            reg1 = register_dict(symbol_type, 1) if not not_pointer else reg
            if not not_pointer:
                self.load_word(reg, address, symbol_type, comment="Load value of pointer in %s 1" % reg)
                self.load_word(reg1, "0(%s)" % reg, symbol_type, comment="Load value of pointer in %s 2" % reg)

            string = "%s %s, %s, 1" % (self.optype[symbol_type][node.children[1].label], reg1, reg1)

            self.write_to_instruction(string, 2)

            sym = symbol_table.get_written_symbol(node.children[0].label, node.ctx.start)
            if not_pointer:
                self.store_symbol(reg, sym)
            else:
                self.store(reg1, "0(%s)" % reg, symbol_type, comment="Store value at dereferenced pointer")
            return '0($sp)', symbol_type, True

        elif node.node_type == 'Increment_op':

            address, symbol_type, not_pointer = self.solve_math(node.children[1], symbol_table)

            reg = register_dict(symbol_type, 0)
            reg1 = register_dict(symbol_type, 1) if not not_pointer else reg
            if not not_pointer:
                self.load_word(reg, address, symbol_type, comment="Load value of pointer in %s 1" % reg)
                self.load_word(reg1, "0(%s)" % reg, symbol_type, comment="Load value of pointer in %s 2" % reg)

            string = "%s %s, %s, 1" % (self.optype[symbol_type][node.children[0].label], reg, reg)

            self.write_to_instruction(string, 2)

            sym = symbol_table.get_written_symbol(node.children[1].label, node.ctx.start)
            # TODO klopt dit
            if not_pointer:
                self.store_symbol(reg, sym)
            else:
                self.store(reg1, "0(%s)" % reg, symbol_type, comment="Store value at dereferenced pointer")

            self.store(reg, '0($sp)', symbol_type)

            return '0($sp)', symbol_type, True

        elif node.node_type == 'unary plus':
            return self.solve_math(node.children[1], symbol_table)

        elif node.node_type == 'unary min':
            value = self.solve_math(node.children[1], symbol_table)
            reg = register_dict(value[1], 0)
            self.load_word(reg, '0($sp)', value[1])
            operator_type = get_operator_type(value[1])
            string = "%s %s" % (mips_operators[operator_type]['neg'], reg)
            self.write_to_instruction(string, 2)

            self.store(reg, '0($sp)', value[1])

            return reg, value[1], True

        elif node.node_type == 'method_call':
            return self.call_method(node, symbol_table)

        elif node.node_type == 'rvalue':
            value = str(node.label)
            self.allocate_mem(4, symbol_table, "Allocate space for rvalue")

            # if str(node.symbol_type) == "float":
            #     value = self.store_float(float(node.label))
            if str(node.symbol_type) == "char*":
                return get_string(str(node.label), symbol_table), "char*", True

            # Get address of symbol and store it into t1
            elif str(node.symbol_type)[0] == '&':
                symbol = symbol_table.get_written_symbol(value, node.ctx.start)
                self.load_address("$t0", "%s($sp)" % self.offset_stack[0].get_offset(symbol),
                                  comment='Load address of %s' % symbol.name)
                reg = "$t0"

            else:
                reg = register_dict(str(node.symbol_type), 0)
                self.load_immediate(value, reg, str(node.symbol_type))

            self.store(reg, "0($sp)", str(node.symbol_type))

            return "0($sp)", str(node.symbol_type), True

        elif node.node_type == 'lvalue':
            # TODO Check array
            reg = None
            self.allocate_mem(4, symbol_table, 'allocate space for instance of %s' % node.label)
            symbol = symbol_table.get_assigned_symbol(node.label, node.ctx.start)
            symbol_type = str(symbol.symbol_type)
            # Dereference if needed
            if '*' in str(node.label):
                dereference_count = node.label.count('*')
                pointer_reg = "%s($sp)" % self.offset_stack[0].get_offset(symbol) if reg is None else reg
                # TODO add float
                reg = self.dereference(pointer_reg, dereference_count, "int")   # reg is the address of the value we want
                symbol_type = symbol_type[:-dereference_count]

                float_or_int_reg = register_dict(symbol_type, 0)

                # self.load_word(float_or_int_reg, "0(%s)" % reg, symbol_type, 'Load value at address')
                self.store(float_or_int_reg, '0($sp)', symbol_type, 'store reference value on top')

                return "0($sp)", symbol_type, False

            else:
                if symbol.is_global:
                    reg = "global_%s%d" % (symbol.name, symbol.reg)
                else:
                    reg = ("%s($sp)" % self.offset_stack[0].get_offset(symbol)) if reg is None else ("0(%s)" % reg)
                self.put_on_top_of_stack(reg, symbol_type)
                return "0($sp)", symbol_type, True

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

        return None, None, None

    def not_value(self, register, symbol_type, node):
        self.load_word("$t0", register, "int")
        self.write_to_instruction("seq $t0, $t0, $0")

        self.store("$t0", "0($sp)", 'int', "store the negated value")

        return "0($sp)", 'int', True

    def return_node(self, node, symbol_table):
        if len(self.function_stack) == 0:
            raise Exception(
                'Error at line: {} column :{} return statement outside of function '.format(node.ctx.start.line,
                                                                                            node.ctx.start.column))
        if len(node.children) == 0:
            # return void
            if self.function_stack[0].symbol_type == 'void':
                self.leave_stack(symbol_table, len(self.allocation_stack) - self.func_stacksize[0], False)

                self.go_to_register('$ra')

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
        returnreg, return_type, not_pointer = self.solve_node(node.children[0], symbol_table)
        # TODO check if pointer
        if not not_pointer:
            ...

        newtype = self.function_stack[0].symbol_type
        castedreg = self.cast_value(returnreg, return_type, newtype, node.ctx.start)

        self.leave_stack(symbol_table, len(self.allocation_stack) - self.func_stacksize[0], False)

        self.store(castedreg, "0($sp)", newtype)

        if self.function_stack[0].name == 'main':
            self.load_immediate(10, '$v0', 'int')
            self.write_to_instruction('syscall', 2)

        else:
            self.go_to_register('$ra')

        self.write = False
        return

    def call_method(self, node: Node, symbol_table: SymbolTable):
        method_name = node.children[0].label

        # Store return address
        self.allocate_mem(4, symbol_table, "Allocate space for $ra")
        self.store("$ra", "0($sp)", "int")
        # self.func_stacksize.insert(0, len(self.allocation_stack))

        self.enter_stack(symbol_table)

        if method_name == "printf":
            self.write_comment("Call printf", 2)
            self.call_printf(node, symbol_table)
            self.leave_stack(symbol_table)
            self.write_comment("Exit printf", 2)
            return "0($sp)", "void", True

        elif method_name == "scanf":
            self.write_comment("Call scanf", 2)
            self.call_scanf(node, symbol_table)
            self.leave_stack(symbol_table)
            self.write_comment("Exit scanf", 2)
            return "0($sp)", "void", True

        # Load arguments
        args = node.children[1].children[:]
        arg_types = []
        arg_reg = []
        for arg in args:
            reg, symbol_type, not_pointer = self.solve_math(arg, symbol_table)
            if not not_pointer:
                ...
            arg_reg.append(reg)
            arg_types.append(symbol_type)

        if method_name == "print_int":
            self.print_int("0($sp)")
            self.leave_stack(symbol_table)
            return "0($sp)", "void", True

        elif method_name == "print_char":
            self.print_char("0($sp)")
            self.leave_stack(symbol_table)
            return "0($sp)", "void", True

        else:
            method = node.symbol_table.get_written_method(method_name, arg_types, node.ctx.start)
            self.go_to_label_linked(method.internal_name)
            register = register_dict(method.symbol_type, 0)
            if method.symbol_type != "void":
                self.load_word(register, "0($sp)", method.symbol_type, comment='load in the return value of the function')
            # load solution into t0
            self.leave_stack(symbol_table)
            # self.leave_stack(symbol_table, len(self.allocation_stack) - self.func_stacksize[0])

            # self.func_stacksize.pop(0)

            self.load_word("$ra", "0($sp)", "int", comment='something with functions')
            if method.symbol_type != "void":
                self.store(register, "0($sp)", method.symbol_type, comment='something with functions')

            return "0($sp)", method.symbol_type, True

    def declare_method(self, method_node: Node, symbol_table: SymbolTable):
        args = []
        if len(method_node.children) > 2 and method_node.children[2].node_type == 'def_args':
            for arg in method_node.children[2].children:
                args.append(arg.children[0].label)
        func = symbol_table.get_method(method_node.children[1].label, args, method_node.ctx.start)
        func.written = True
        return None, None

    def generate_method(self, method_node: Node, symbol_table: SymbolTable):
        write2 = self.write
        self.write = True
        args = []
        self.func_stacksize.insert(0, len(self.allocation_stack))
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

        write = self.write
        self.write = False
        for i in range(len(args)):
            symbol = self.allocate_node(method_node.children[2].children[i],
                                        method_node.children[2].children[i].symbol_table)

        self.write = write

        # m = list(map(self.convert2, args))
        if func.internal_name == 'main':
            self.write_to_instruction(".globl %s" % func.internal_name)
        self.write_to_instruction(func.internal_name + ":", 0)

        self.solve_node(method_node.children[-1], symbol_table)
        # generate returns for returnless bois
        self.leave_stack(symbol_table, len(self.allocation_stack) - self.func_stacksize[0], False)
        self.allocate_mem(4, symbol_table)
        if func.symbol_type!= 'void':
            reg = register_dict(func.symbol_type,0)
            self.load_immediate(0, reg, func.symbol_type)

            self.store(reg, "0($sp)", func.symbol_type)
        if func.internal_name != 'main':
            self.go_to_register('$ra')


        self.function_stack.pop(0)
        self.func_stacksize.pop(0)
        self.write = write2

        return

    def if_else(self, node: Node, symbol_table: SymbolTable):
        """
        :param node: if else node
        :param symbol_table:
        :return: nothing
        """
        if not self.write:
            return
        condition = node.children[0]
        # Evaluate Condition
        temp_register, value_type, not_pointer = self.solve_node(condition, symbol_table)
        if not not_pointer:
            ...

        # Load stack pointer in temp register
        # TODO float must be converted to int
        # temp_reg = "$t0"
        temp_reg = register_dict(value_type, 0)
        self.load_word(temp_reg, temp_register, value_type)

        # Update Label
        label = self.label  # Label counter
        self.label += 1  # Else, Endif

        # Jump to else when $t0 = 0
        self.go_to_label_conditional(temp_reg, "Else%d" % label)

        # Write if block
        write = self.write
        self.solve_node(node.children[1], symbol_table)
        self.go_to_label("Endif%d" % label)

        # Store write
        if_write = self.write
        else_write = write

        self.write = write
        self.write_label("Else%d" % label)
        # Write else block
        if len(node.children) > 2:
            self.solve_node(node.children[2], symbol_table)
            self.go_to_label("Endif%d" % label)
            else_write = self.write

        # Continue writing if one of the 2 blocks has no return / break / continue
        self.write = else_write or if_write
        self.write_label("Endif%d" % label)
        return

    def switch(self, node, symbol_table):
        in_loop = self.in_loop
        self.in_loop = False
        if not self.write:
            return
        switchval, switchtype, not_pointer = self.solve_math(node.children[0], symbol_table)
        if not not_pointer :
            ...
        reg = '$t0'
        if switchtype is not None and switchtype != 'void':
            reg = register_dict(switchtype, 0)
        else:
            raise Exception("void can't be cast to int in switchcase")

        self.load_word(reg, "0($sp)", switchtype)
        self.deallocate_mem(4, symbol_table)
        branchval = self.cast_value(reg, switchtype, "int", node.ctx.start)

        write = self.write
        breaks = self.breaks
        self.breaks = False

        continue_writing = False

        current_label = self.label
        default_label = current_label + len(node.children) - 1

        self.break_stack.insert(0, "label%d" % default_label)
        self.label += len(node.children)
        string = ""
        labels = []

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
                if curr.label in labels:
                    raise Exception(
                        "[Error] line {} position {} Secondary definition of {}".format(node.ctx.start.line,
                                                                                        node.ctx.start.column,
                                                                                        curr.label))
                self.load_immediate(curr.label, '$t1', 'int')
                string = "beq %s, %s, label%d" % (branchval, "$t1", (current_label + i - 1))
                self.write_to_instruction(string, 2)
                labels.append(curr.label)

        self.go_to_label("label%d" % (default_label))

        for i in range(1, len(node.children)):
            continue_writing = continue_writing or self.write or self.breaks
            self.write = write
            self.breaks = False
            self.go_to_label("label%d" % (current_label + i - 1))
            self.add_label(current_label + i - 1)
            self.solve_node(node.children[i], symbol_table)

        if default:
            self.write = continue_writing
        else:
            self.write = write

        self.go_to_label("label%d" % (current_label + len(node.children) - 1))
        self.add_label(current_label + len(node.children) - 1)

        self.break_stack.pop()
        self.breaks = breaks
        self.in_loop = in_loop

    def loop(self, node: Node, symbol_table: SymbolTable):
        in_loop = self.in_loop
        self.in_loop = True
        skip_condition = False
        if node.children[0].node_type == 'for initial':
            self.solve_node(node.children[0].children[0], symbol_table)

        elif node.children[0].node_type == 'for do':
            skip_condition = True

        labels = {
            "condition": "for_condition%d" % self.label,
            "code_block": "for_block%d" % self.label,
            "update": "for_update%d" % self.label,
            "next_block": "for_end%d" % self.label,
            "break_block": "for_break%d" % self.label,
        }
        self.label += 1
        breaks = self.breaks
        self.break_stack.insert(0, labels["next_block"])
        self.continue_stack.insert(0, labels["condition"])
        self.loop_stacksize.insert(0, len(self.allocation_stack))
        write = self.write

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
                self.write_label(labels["condition"])
                reg, value_type, not_pointer = self.solve_node(child, child.symbol_table)
                if not not_pointer:
                    ...
                if value_type == 'float':
                    # TODO convert
                    pass
                self.go_to_label_conditional(reg, labels["next_block"])  # jump to end
                self.go_to_label(labels["code_block"])  # jump back to loop

            elif child.node_type == 'for update':
                self.write = write
                self.continue_stack[0] = labels["update"]
                self.write_label(labels["update"])
                self.solve_node(child, child.symbol_table)
                self.go_to_label(labels["condition"])
                update = True

            elif child.node_type != 'for initial':
                self.write = write
                self.write_label(labels["code_block"])
                self.solve_node(child, child.symbol_table)
                if update:
                    self.go_to_label(labels["update"])
                else:
                    self.go_to_label(labels["condition"])

        self.break_stack.pop()
        self.continue_stack.pop()
        self.loop_stacksize.pop()
        self.write = write
        self.write_label(labels["next_block"])
        self.breaks = breaks
        self.in_loop = in_loop

    def call_printf(self, node, symbol_table):
        args = node.children[1].children[:]
        arg_types = []
        arg_reg = []
        arg_reg_types = []
        expected_args = []
        i = 0
        print_string = args[0].label

        # Compute which argument types are needed to complete the print call
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

        # Check for no extra / missing params
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

        # Load all arguments into memory
        for arg in args:
            # Update Stack pointers of previous
            for index, prev_arg_reg in enumerate(arg_reg):
                if "($sp)" in prev_arg_reg:
                    offset = int(prev_arg_reg[0])
                    arg_reg[index] = str(offset + 4) + prev_arg_reg[1:]
            # Load arg
            address, symbol_type, not_pointer = self.solve_math(arg, symbol_table)
            if not not_pointer:
                reg = register_dict(symbol_type, 0)
                self.load_word(reg, address, symbol_type, comment="Load value of pointer in %s 1" % reg)
                self.load_word(reg, "0(%s)" % reg, symbol_type, comment="Load value of pointer in %s 2" % reg)
                self.store(reg, address, symbol_type, comment="Load value of pointer in %s 2" % reg)
            if address is None:
                raise Exception('Compiler Mistake when solving print arg')
            arg_reg.append(address)
            arg_types.append(symbol_type)


        print(arg_types)
        # Check that the printed string exists
        if print_string is None:
            raise Exception("what")  # TODO

        # Split strings into parts and print each part separately
        partial_strings = re.split("%.", print_string)
        for i, partial_string in enumerate(partial_strings):
            # Print string
            self.print_string(symbol_table.get_mips_strings()[partial_string])

            # Check if a % follows this string
            if i < len(arg_reg) - 1:  # first arg is print_string => len-1
                if arg_types[i + 1] == 'int':
                    self.print_int(arg_reg[i + 1])
                elif arg_types[i + 1] == 'float':
                    self.print_float(arg_reg[i + 1])
                elif arg_types[i + 1] == 'char':
                    self.print_char(arg_reg[i + 1])
                elif arg_types[i + 1] == 'char*':
                    self.print_string(arg_reg[i + 1])

    def call_scanf(self, node: Node, symbol_table: SymbolTable):
        pass

    # Pointers
    def dereference(self, pointer_register: str, dereference_count: int, symbol_type: str) -> str:
        """
        Dereference a register
        :param pointer_register:
        :param dereference_count:
        :param symbol_type:
        :return: final address
        """
        # Load base pointer
        # self.load_word("$t0", pointer_register, "int", comment='Load pointer before dereference')
        self.load_address("$t0", pointer_register, comment='Dereference once')
        for i in range(dereference_count):
            #     # Load value that is stored address that was stored in pointer
            self.load_word("$t0", "0($t0)", symbol_type, comment='Dereference once')  # Load from address in $t0

        return "$t0"
