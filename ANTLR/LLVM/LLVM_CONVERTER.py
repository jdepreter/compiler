class LLVM_Converter:
    def __init__(self, ast):
        self.ast = ast
        self.stack = []
        self.register = 0

    def to_llvm(self):
        self.stack.insert(0, self.ast.startnode)
        current_symbol_table = self.ast.startnode.symbol_table



    def solve_llvm_node(self, node, symbol_table):
        ...






