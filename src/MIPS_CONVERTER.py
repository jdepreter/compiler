

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
            self.file.write(indent + string + "\n")
