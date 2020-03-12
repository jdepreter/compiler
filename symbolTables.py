from CustomExceptions import UndeclaredVariable, UninitializedVariable, DuplicateDeclaration


class SymbolType:
    def __init__(self, symbol_type, assigned, const,current_register):
        self.symbol_type = symbol_type
        self.assigned = assigned
        self.const = const
        self.current_register = current_register

    def set_reg(self, current_register):
        self.current_register = current_register


class SymbolTable:
    def __init__(self):
        self.table_stack = []
        self.table_list = []
        self.current_register = 0

    def open_scope(self):
        newdict = dict()
        self.table_stack.insert(0, newdict)
        self.table_list.append(newdict)

    def close_scope(self):
        self.table_stack.pop(0)

    def add_symbol(self, symbol, symbol_type, error, assinged=True, const=False):
        if symbol in self.table_stack[0]:
            raise DuplicateDeclaration("[Error] Line {}, Position {}: Duplicate declaration of variable {} "
                                       .format(error.line, error.column, symbol))
        self.table_stack[0][symbol] = SymbolType(symbol_type, assinged, const, self.current_register)
        self.current_register += 1

    def get_symbol(self, symbol, error):
        for scope in self.table_stack:
            if symbol in scope:
                return scope[symbol]

        raise UndeclaredVariable("[Error] Line {}, Position {}: variable {} is undeclared"
                                 .format(error.line, error.column, symbol))

    def get_current_scope(self):
        s = SymbolTable()
        s.table_stack = list(self.table_stack)
        return s
# class SymbolTableCreator:
#     def __init__(self, ast):
#         self.ast = ast
#         self.symbol_table = SymbolTable()
#
#
#     def create(self):
#         queue = [self.ast.startnode]
#         visited = []
#         while len(queue) > 0:
#             current_node = queue[0]
#             queue = queue[1:]
#             if current_node.id in visited:
#                 continue
#             visited.append(current_node.id)
#             queue = current_node.children + queue
#
#             if current_node.label in ['dec', 'def']:
#                 self.symbol_table.add_symbol(current_node.children[1], current_node.children[0])
#
#             elif current_node.label == 'open_scope':
#
#
#



