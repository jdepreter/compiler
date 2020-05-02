from src.CustomExceptions import *
from src.helperfuncs import get_type_and_stars


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
                self.allocate_node(node.children[i], symbol_table, typing.label)
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

    def allocate_node(self, node, symbol_table, symbol_type):
        variable = node.label
        if node.node_type in ['assignment2', 'array']:
            variable = node.children[0].label

        # if node.node_type == 'Arg_definition':
        #     variable = node.children[1].label

        symbol = symbol_table.get_symbol(variable, node.ctx.start)
        sym_type, stars = get_type_and_stars(symbol_type)

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
            
        self.allocate_mem(symbol, symbol_table)  # Remove L8er

        if node.node_type == 'assignment2':
            value = None
            if node.children[1].node_type == 'assignment':
                register = self.assign_node(node.children[1], symbol_table)
            else:
                register = self.solve_math(node.children[1], symbol_table)
            self.store_symbol(symbol, value)

        return symbol, symbol_type

    def allocate_mem(self, symbol, symbol_table):
        """
        Create space for variable
        Stack grows downwards
        to use this mem spot access ($sp)
        to use previous mem spot 4($sp)
        :return:
        """
        string = "addiu $sp, $sp, -4"   # Reserve word on stack
        self.write_to_instruction(string, 2)
        # Increase offset of previous variables in stack (offset can never be < 0)
        symbol_table.increase_offset(4)
        symbol.written = True

    def deallocate_mem(self, amount, symbol_table):
        """
        When closing scope, deallocate space used in this scope
        :param amount: amount of variables in this scope
        :return:
        """
        string = "addiu $sp, $sp, %d" % amount * 4  # Reserve word on stack
        self.write_to_instruction(string, 2)
        # Decrease offset of previous variables in stack
        symbol_table.decrease_offset(amount * 4)

    def store_symbol(self, value, symbol):
        offset = "" if symbol.offset == 0 else str(symbol.offset)
        string = "li %s($fp), %s" % (offset, str(value))
        self.write_to_instruction(string, 2)

    def assign_node(self, node, symbol_table):
        pass


