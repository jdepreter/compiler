from ANTLR.LLVM.cListener import cListener
from ANTLR.LLVM.cParser import cParser
from symbolTables import SymbolTable
from AST import Node


# Depth first
class CASTGenerator(cListener):
    def __init__(self):
        self.ast = None
        self.currentNode = None
        self.id = 1
        self.symbol_table = SymbolTable()

    def create_node(self, label, node_type, parent, ctx):
        node = Node(self.id, node_type, label, parent, ctx)
        self.id += 1
        return node

    def enterC(self, ctx:cParser.CContext):
        print("enter c")
        self.ast = self.create_node("C", "C", self.currentNode, ctx)
        self.currentNode = self.ast
        self.symbol_table.open_scope()
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def enterLine(self, ctx:cParser.LineContext):
        print("enter line")
        node = self.create_node("line", "line", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitLine(self, ctx:cParser.LineContext):
        print("exit line")
        self.currentNode = self.currentNode.parent

    def enterScope(self, ctx:cParser.ScopeContext):
        print("enter scope")
        node = self.create_node("scope", "scope", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.symbol_table.open_scope()
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitScope(self, ctx:cParser.ScopeContext):
        print("exit scope")
        self.symbol_table.close_scope()
        self.currentNode = self.currentNode.parent

    def enterLvalue(self, ctx:cParser.LvalueContext):
        string = "lvalue"
        if ctx.IDENTIFIER():
            string = str(ctx.IDENTIFIER())

        node = self.create_node(string, "lvalue", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()


    def exitLvalue(self, ctx:cParser.LvalueContext):
        self.currentNode = self.currentNode.parent

    def enterRvalue(self, ctx:cParser.RvalueContext):
        string = "nothing"
        symbol_type = ""
        if ctx.INT():
            string = str(ctx.INT())
            symbol_type = "int"
        elif ctx.FLOAT():
            string = str(ctx.FLOAT())
            symbol_type = "float"
        elif ctx.IDENTIFIER():
            string = str(ctx.IDENTIFIER())
            symbol_type = "address"
        elif ctx.CHAR():
            string = str(ord(str(ctx.CHAR())[1]))
            symbol_type = "char"
        node = self.create_node(string, "rvalue", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        self.currentNode.symbol_type = symbol_type

    def exitRvalue(self, ctx:cParser.RvalueContext):
        self.currentNode = self.currentNode.parent

    def enterAddress(self, ctx:cParser.AddressContext):
        node = self.create_node("address", "address", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitAddress(self, ctx:cParser.AddressContext):
        self.currentNode = self.currentNode.parent

    def enterAssignment(self, ctx:cParser.AssignmentContext):
        node = self.create_node("assignment", "assignment", self.currentNode, ctx)
        # identifier = self.create_node(str(ctx.IDENTIFIER()), node, ctx)
        # node.children.append(identifier)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def enterAssignment2(self, ctx:cParser.Assignment2Context):
        node = self.create_node("assignment2", "assignment2", self.currentNode, ctx)
        # identifier = self.create_node(str(ctx.IDENTIFIER()), node, ctx)
        # node.children.append(identifier)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def enterDefinition(self, ctx:cParser.DefinitionContext):
        node = self.create_node("definition", "definition", self.currentNode, ctx)
        # identifier = self.create_node(str(ctx.IDENTIFIER()), node, ctx)
        # node.children.append(identifier)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def enterPointer_type(self, ctx:cParser.Pointer_typeContext):
        string = "pointer"
        if ctx.CHAR_TYPE():
            string = str(ctx.CHAR_TYPE())
            symbol_type = "char*"
        if ctx.FLOAT_TYPE():
            string = str(ctx.FLOAT_TYPE())
            symbol_type = "float*"
        if ctx.INT_TYPE():
            string = str(ctx.INT_TYPE())
            symbol_type = "int*"
        node = self.create_node(string, "pointer_type", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        self.currentNode.symbol_type = symbol_type

    def enterVar_type(self, ctx:cParser.Var_typeContext):
        string = "pointer"
        if ctx.CHAR_TYPE():
            string = str(ctx.CHAR_TYPE())
            symbol_type = "char"
        if ctx.FLOAT_TYPE():
            string = str(ctx.FLOAT_TYPE())
            symbol_type = "float"
        if ctx.INT_TYPE():
            string = str(ctx.INT_TYPE())
            symbol_type = "int"

        node = self.create_node(string, "var_type", self.currentNode, ctx)
        self.currentNode.children.insert(0, node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        self.currentNode.symbol_type = symbol_type

    def exitAssignment2(self, ctx:cParser.AssignmentContext):
        self.currentNode = self.currentNode.parent

    def exitAssignment(self, ctx:cParser.AssignmentContext):

        var = self.currentNode.children[0]
        while var.label in ['ass', 'Increment_var', 'Increment_op', 'increment']:
            var = var.children[0]
        var_type = self.symbol_table.get_symbol(var.label, ctx.start)
        if var_type.const:
            raise Exception("[Error] Line {}, Position {}: variable {} is declared const"
                            .format(ctx.start.line, ctx.start.column, var))
        self.currentNode = self.currentNode.parent

    def exitDefinition(self, ctx:cParser.DefinitionContext):
        if ctx.CONST():
            node = self.create_node("const", "const", self.currentNode, ctx)
            self.currentNode.children.insert(0, node)
            for i in range(2, len(self.currentNode.children)):
                node = self.currentNode.children[i]
                symbol = node.label
                if node.node_type == 'assignment2':
                    symbol = node.children[0].label
                self.symbol_table.add_symbol(symbol, self.currentNode.children[1].label, ctx.start, True, True)
        else:
            for i in range(1, len(self.currentNode.children)):
                node = self.currentNode.children[i]
                symbol = node.label
                if node.node_type == 'assignment2':
                    symbol = node.children[0].label
                self.symbol_table.add_symbol(symbol, self.currentNode.children[0].label, ctx.start, True)

        self.currentNode = self.currentNode.parent

    def exitPointer_type(self, ctx:cParser.Pointer_typeContext):
        self.currentNode = self.currentNode.parent

    def exitVar_type(self, ctx:cParser.Var_typeContext):
        self.currentNode = self.currentNode.parent

    # Expressions ----
    def enterBool1(self, ctx:cParser.Bool1Context):
        node = self.create_node("bool1", "bool1", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitBool1(self, ctx:cParser.Bool1Context):
        self.currentNode = self.currentNode.parent

    def enterBool2(self, ctx:cParser.Bool2Context):
        # (EQ | LT | LE | GT | GE | NE)
        string = "bool2"
        if ctx.EQ():
            string = str(ctx.EQ())
        elif ctx.LT():
            string = str(ctx.LT())
        elif ctx.LE():
            string = str(ctx.LE())
        elif ctx.GT():
            string = str(ctx.GT())
        elif ctx.GE():
            string = str(ctx.GE())
        elif ctx.NE():
            string = str(ctx.NE())

        node = self.create_node(string, "bool2", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitBool2(self, ctx:cParser.Bool2Context):
        self.currentNode = self.currentNode.parent

    def enterPlus(self, ctx:cParser.PlusContext):
        node = self.create_node("plus", "plus", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def enterNot_value(self, ctx: cParser.Not_valueContext):
        node = self.create_node(str(ctx.NOT()), "not_value", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitNot_value(self, ctx: cParser.Not_valueContext):
        self.currentNode = self.currentNode.parent

    def exitPlus(self, ctx:cParser.PlusContext):
        self.currentNode = self.currentNode.parent

    def enterVm(self, ctx:cParser.VmContext):
        node = self.create_node("vm", "vm", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitVm(self, ctx:cParser.VmContext):
        self.currentNode = self.currentNode.parent

    def enterMod(self, ctx:cParser.ModContext):
        node = self.create_node("mod", "mod", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitMod(self, ctx:cParser.ModContext):
        self.currentNode = self.currentNode.parent

    def enterNeg_sol(self, ctx:cParser.Neg_solContext):
        node = self.create_node("negsol", "negsol", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitNeg_sol(self, ctx:cParser.Neg_solContext):
        self.currentNode = self.currentNode.parent

    def enterVm_sol(self, ctx:cParser.Vm_solContext):
        node = self.create_node("vmsol", "vmsol", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitVm_sol(self, ctx:cParser.Vm_solContext):
        self.currentNode = self.currentNode.parent

    def enterValue(self, ctx:cParser.ValueContext):
        node = self.create_node("value", "value", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitValue(self, ctx:cParser.ValueContext):
        self.currentNode = self.currentNode.parent

    # def enterNeg_value(self, ctx:cParser.Neg_valueContext):
    #     node = self.create_node(str(ctx.NEG_INT()), "neg_value", self.currentNode, ctx)
    #     self.currentNode.children.append(node)
    #     self.currentNode = node
    #     self.currentNode.symbol_table = self.symbol_table.get_current_scope()
    #
    # def exitNeg_value(self, ctx:cParser.Neg_valueContext):
    #     self.currentNode = self.currentNode.parent

    def enterOperator(self, ctx:cParser.OperatorContext):
        string = ""
        if ctx.MAAL():
            string = str(ctx.MAAL())
        else:
            string = str(ctx.DEEL())
        node = self.create_node(string, string, self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitOperator(self, ctx:cParser.OperatorContext):
        self.currentNode = self.currentNode.parent

    def enterOperator2(self, ctx:cParser.Operator2Context):
        string = ""
        if ctx.PLUS():
            string = str(ctx.PLUS())
        else:
            string = str(ctx.MIN())
        node = self.create_node(string, string, self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitOperator2(self, ctx:cParser.Operator2Context):
        self.currentNode = self.currentNode.parent

    def enterBoolop(self, ctx:cParser.BoolopContext):
        string = ""
        if ctx.AND():
            string = str(ctx.AND())
        else:
            string = str(ctx.OR())
        node = self.create_node(string, "boolop", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitBoolop(self, ctx:cParser.BoolopContext):
        self.currentNode = self.currentNode.parent

    def enterVariable_identifier(self, ctx: cParser.Variable_identifierContext):
        node = self.create_node(str(ctx.IDENTIFIER()), "var", self.currentNode, ctx)

        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()



    def exitVariable_identifier(self, ctx:cParser.Variable_identifierContext):
        self.currentNode = self.currentNode.parent

    def enterMethod_call(self, ctx:cParser.Method_callContext):
        node = self.create_node("method_call", "method_call", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        id = self.create_node(str(ctx.IDENTIFIER()), "method_call_id", self.currentNode, ctx)
        self.currentNode.children.append(id)
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitMethod_call(self, ctx:cParser.Method_callContext):
        self.currentNode.children.append(self.create_node("empty arg", "arg", self.currentNode, ctx))
        self.currentNode = self.currentNode.parent

    def enterArgs(self, ctx:cParser.ArgsContext):
        node = self.create_node("args", "args", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitArgs(self, ctx:cParser.ArgsContext):
        self.currentNode = self.currentNode.parent


    def enterIncrement(self, ctx:cParser.IncrementContext):
        node = self.create_node("increment", "increment", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitIncrement(self, ctx:cParser.IncrementContext):
        self.currentNode = self.currentNode.parent

    def enterIncrement_op_first(self, ctx:cParser.Increment_op_firstContext):
        node = self.create_node("Increment_op", "Increment_op", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        string = '--'
        if ctx.PLUSPLUS():
            string = '++'

        node2 = self.create_node(string, "increment", self.currentNode, ctx)
        node1 = self.create_node(str(ctx.IDENTIFIER()), "var", self.currentNode, ctx)
        self.currentNode.children.append(node1)
        self.currentNode.children.append(node2)
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        node1.symbol_table = self.symbol_table.get_current_scope()
        node2.symbol_table = self.symbol_table.get_current_scope()
        node1.symbol_type = node1.symbol_table.get_symbol(str(ctx.IDENTIFIER()), None).symbol_type


    def exitIncrement_op_first(self, ctx:cParser.Increment_op_firstContext):
        self.currentNode = self.currentNode.parent

    def enterIncrement_var_first(self, ctx:cParser.Increment_var_firstContext):
        node = self.create_node("Increment_var", "Increment_var", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        string = '--'
        if ctx.PLUSPLUS():
            string = '++'

        node2 = self.create_node(string, "Increment_var", self.currentNode, ctx)
        node1 = self.create_node(str(ctx.IDENTIFIER()), "var", self.currentNode, ctx)
        self.currentNode.children.append(node1)
        self.currentNode.children.append(node2)
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        node1.symbol_table = self.symbol_table.get_current_scope()
        node2.symbol_table = self.symbol_table.get_current_scope()
        node1.symbol_type = node1.symbol_table.get_symbol(str(ctx.IDENTIFIER()), None).symbol_type

    def exitIncrement_var_first(self, ctx:cParser.Increment_var_firstContext):
        self.currentNode = self.currentNode.parent

    def enterUnary_min(self, ctx:cParser.Unary_minContext):
        node = self.create_node("unary min", "unary min", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        node_min = self.create_node('-', 'min', self.currentNode, ctx)
        self.currentNode.children.append(node_min)

    def exitUnary_min(self, ctx:cParser.Unary_minContext):
        self.currentNode = self.currentNode.parent

    def enterUnary_plus(self, ctx:cParser.Unary_plusContext):
        node = self.create_node("unary plus", "unary plus", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        node_min = self.create_node('+', 'plus', self.currentNode, ctx)
        self.currentNode.children.append(node_min)

    def exitUnary_plus(self, ctx:cParser.Unary_plusContext):
        self.currentNode = self.currentNode.parent




