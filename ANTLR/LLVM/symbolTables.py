
class SymbolTable:
    def __init__(self):
        self.table_stack = []
        self.table_list = []

    def open_scope(self):
        newdict = dict()
        self.table_stack.insert(0, newdict)
        self.table_list.append(newdict)

    def close_scope(self):
        self.table_stack.pop(0)

    def add_symbol(self, symbol, symbol_type):
        self.table_stack[0][symbol] = symbol_type

    def get_symbol(self, symbol):
        for scope in self.table_stack:
            if symbol in scope:
                return scope[symbol]

        return None


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



