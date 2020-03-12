class LLVM_Converter:
    def __init__(self, ast, file):
        self.ast = ast
        self.stack = []
        self.register = 0
        self.file = file
        self.format_dict = {'int': 'i32', 'float': 'float'}
        self.optype ={'+':{'int':'add', 'float': 'fadd'},
                      '-':{'int':'sub', 'float': 'fsub'},
                      '*': {'int':'mul', 'float': 'fmul'},
                      '/':{'int':'sdiv', 'float': 'fdiv'},
                      '%': {'int':'srem', 'float': 'frem'}}

    def to_llvm(self):
        # self.stack.insert(0, self.ast.startnode)
        current_symbol_table = self.ast.startnode.symbol_table
        self.solve_llvm_node(self.ast.startnode, current_symbol_table)


    # helpermethod to write used for declaration or definition
    def allocate_node(self, node, symbol_table):

        self.file.write("%a" + str(symbol_table.get_symbol(str(node.children[1].label), None).current_register) + " = alloca "
                         + self.format_dict[str(node.children[0].label)] + "\n")

    def solve_llvm_node(self, node, symbol_table):
        # TODO x++ & ++x staan nog ni ok in den boom && add char / double && maybe arrays && typeswitching + warnings
        if node.symbol_table != None:
            symbol_table = node.symbol_table

        if node.label == 'dec':
            self.allocate_node(node, symbol_table)
        elif node.label == 'def':
            self.allocate_node(node, symbol_table)
            self.solve_math(node.children[2], symbol_table, 'int')
        elif node.label == 'ass':
            self.solve_math(node.children[1], symbol_table, 'int')




        for child in node.children:

            if node.symbol_table != None:
                symbol_table = node.symbol_table

            self.solve_llvm_node(child, symbol_table)
    def load_symbol(self,SymbolType):
        reg = self.register
        self.register += 1
        string = '%r'+str(reg)+' = load '+self.format_dict[SymbolType.symbol_type]+'* %a'+str(SymbolType.current_register)+ '\n'
        self.file.write(string)
        return '%r'+str(reg)

    def solve_math(self, node, symbol_table, type):
        string = ''
        if node.label in ['+','-','*','/', '%']:
            reg = self.register
            self.register += 1
            string = '%r' + str(reg) + ' = '+self.optype[node.label][type] +' ' + self.format_dict[type] +' '+ \
                     self.solve_math(node.children[0], symbol_table, type)+', '+self.solve_math(node.children[1], symbol_table, type) + '\n'

            self.file.write(string)
            return '%r' + str(reg)

        elif node.label == '&&':
            ...
        elif node.label == '||':
            ...
        else:
            try:
                newval = int(node.label)
                return str(newval)
            except:
                #assume we'll have a symbol
                sym = symbol_table.get_symbol(node.label, None)
                return self.load_symbol(sym)



















