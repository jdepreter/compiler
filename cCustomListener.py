from antlr4 import *
from ANTLR.LLVM.cListener import cListener
from ANTLR.LLVM.cParser import cParser
from ANTLR.LLVM.symbolTables import SymbolTable
from ANTLR.LLVM.AST import Node


# Depth first
class CASTGenerator(cListener):
    def __init__(self):
        self.ast = None
        self.currentNode = None
        self.id = 1
        self.symbol_table = SymbolTable()

    def create_node(self, label, parent, ctx):
        node = Node(self.id, label, parent, ctx)
        self.id += 1
        return node

    def enterC(self, ctx:cParser.CContext):
        print("enter c")
        self.ast = self.create_node("C", self.currentNode, ctx)
        self.currentNode = self.ast
        self.symbol_table.open_scope()
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def enterLine(self, ctx:cParser.LineContext):
        print("enter line")
        node = self.create_node("line", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitLine(self, ctx:cParser.LineContext):
        print("exit line")
        self.currentNode = self.currentNode.parent

    def enterScope(self, ctx:cParser.ScopeContext):
        print("enter scope")
        node = self.create_node("scope", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.symbol_table.open_scope()
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitScope(self, ctx:cParser.ScopeContext):
        print("exit scope")
        self.symbol_table.close_scope()
        self.currentNode = self.currentNode.parent

    def enterLvalue(self, ctx:cParser.LvalueContext):
        string = "lvalue"
        if ctx.IDENTIFIER():
            string = str(ctx.IDENTIFIER())
        node = self.create_node(string, self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitLvalue(self, ctx:cParser.LvalueContext):
        self.currentNode = self.currentNode.parent

    def enterRvalue(self, ctx:cParser.RvalueContext):
        string = "nothing"
        if ctx.INT():
            string = str(ctx.INT())
        elif ctx.FLOAT():
            string = str(ctx.FLOAT())
        elif ctx.IDENTIFIER():
            string = str(ctx.IDENTIFIER())
        elif ctx.CHAR():
            string = str(ord(str(ctx.CHAR())[1]))
        node = self.create_node(string, self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitRvalue(self, ctx:cParser.RvalueContext):
        self.currentNode = self.currentNode.parent

    def enterAddress(self, ctx:cParser.AddressContext):
        node = self.create_node("address", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitAddress(self, ctx:cParser.AddressContext):
        self.currentNode = self.currentNode.parent

    def enterAssignment(self, ctx:cParser.AssignmentContext):
        node = self.create_node("ass", self.currentNode, ctx)
        # identifier = self.create_node(str(ctx.IDENTIFIER()), node, ctx)
        # node.children.append(identifier)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def enterDeclaration(self, ctx:cParser.DeclarationContext):
        node = self.create_node("dec", self.currentNode, ctx)
        identifier = self.create_node(str(ctx.IDENTIFIER()), node, ctx)
        node.children.append(identifier)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def enterDefinition(self, ctx:cParser.DefinitionContext):
        node = self.create_node("def", self.currentNode, ctx)
        identifier = self.create_node(str(ctx.IDENTIFIER()), node, ctx)
        node.children.append(identifier)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def enterPointer_type(self, ctx:cParser.Pointer_typeContext):
        string = "pointer"
        if ctx.CHAR_TYPE():
            string = str(ctx.CHAR_TYPE())
        if ctx.FLOAT_TYPE():
            string = str(ctx.FLOAT_TYPE())
        if ctx.INT_TYPE():
            string = str(ctx.INT_TYPE())
        node = self.create_node(string, self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def enterVar_type(self, ctx:cParser.Var_typeContext):
        string = "pointer"
        if ctx.CHAR_TYPE():
            string = str(ctx.CHAR_TYPE())
        if ctx.FLOAT_TYPE():
            string = str(ctx.FLOAT_TYPE())
        if ctx.INT_TYPE():
            string = str(ctx.INT_TYPE())

        node = self.create_node(string, self.currentNode, ctx)
        self.currentNode.children.insert(0, node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitAssignment(self, ctx:cParser.AssignmentContext):

        var = self.currentNode.children[0]
        while var.label in ['ass', 'Increment_var', 'Increment_op', 'increment']:
            var = var.children[0]
        var_type = self.symbol_table.get_symbol(var.label, ctx.start)
        if var_type.const:
            raise Exception("[Error] Line {}, Position {}: variable {} is declared const"
                            .format(ctx.start.line, ctx.start.column, var))
        self.currentNode = self.currentNode.parent


    def exitDeclaration(self, ctx:cParser.DeclarationContext):
        self.symbol_table.add_symbol(self.currentNode.children[1].label, self.currentNode.children[0].label, ctx.start, False)
        self.currentNode = self.currentNode.parent

    def exitDefinition(self, ctx:cParser.DefinitionContext):
        if ctx.CONST():
            node = self.create_node("const", self.currentNode, ctx)
            self.currentNode.children.insert(0, node)
            self.symbol_table.add_symbol(self.currentNode.children[2].label, self.currentNode.children[1].label, ctx.start, True, True)
        else:
            self.symbol_table.add_symbol(self.currentNode.children[1].label, self.currentNode.children[0].label, ctx.start, True)

        self.currentNode = self.currentNode.parent

    def exitPointer_type(self, ctx:cParser.Pointer_typeContext):
        self.currentNode = self.currentNode.parent

    def exitVar_type(self, ctx:cParser.Var_typeContext):
        self.currentNode = self.currentNode.parent

    # Expressions ----
    def enterBool1(self, ctx:cParser.Bool1Context):
        node = self.create_node("bool1", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitBool1(self, ctx:cParser.Bool1Context):
        self.currentNode = self.currentNode.parent

    def enterBool2(self, ctx:cParser.Bool2Context):
        # (EQ | LT | LE | GT | GE | NE)
        string = "Bool2"
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

        node = self.create_node(string, self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitBool2(self, ctx:cParser.Bool2Context):
        self.currentNode = self.currentNode.parent

    def enterPlus(self, ctx:cParser.PlusContext):
        node = self.create_node("plus", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def enterNot_value(self, ctx: cParser.Not_valueContext):
        node = self.create_node(str(ctx.NOT()), self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitNot_value(self, ctx: cParser.Not_valueContext):
        self.currentNode = self.currentNode.parent

    def exitPlus(self, ctx:cParser.PlusContext):
        self.currentNode = self.currentNode.parent

    def enterVm(self, ctx:cParser.VmContext):
        node = self.create_node("vm", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitVm(self, ctx:cParser.VmContext):
        self.currentNode = self.currentNode.parent

    def enterMod(self, ctx:cParser.ModContext):
        node = self.create_node("mod", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitMod(self, ctx:cParser.ModContext):
        self.currentNode = self.currentNode.parent

    def enterNeg_sol(self, ctx:cParser.Neg_solContext):
        node = self.create_node("negsol", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitNeg_sol(self, ctx:cParser.Neg_solContext):
        self.currentNode = self.currentNode.parent

    def enterVm_sol(self, ctx:cParser.Vm_solContext):
        node = self.create_node("vmsol", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitVm_sol(self, ctx:cParser.Vm_solContext):
        self.currentNode = self.currentNode.parent

    def enterValue(self, ctx:cParser.ValueContext):
        node = self.create_node("value", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitValue(self, ctx:cParser.ValueContext):
        self.currentNode = self.currentNode.parent

    def enterNeg_value(self, ctx:cParser.Neg_valueContext):
        node = self.create_node(str(ctx.NEG_INT()), self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitNeg_value(self, ctx:cParser.Neg_valueContext):
        self.currentNode = self.currentNode.parent

    def enterOperator(self, ctx:cParser.OperatorContext):
        string = ""
        if ctx.MAAL():
            string = str(ctx.MAAL())
        else:
            string = str(ctx.DEEL())
        node = self.create_node(string, self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitOperator(self, ctx:cParser.OperatorContext):
        self.currentNode = self.currentNode.parent

    def enterOperator2(self, ctx:cParser.Operator2Context):
        string = ""
        if ctx.PLUS():
            string = str(ctx.PLUS())
        else:
            string = str(ctx.MIN())
        node = self.create_node(string, self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitOperator2(self, ctx:cParser.Operator2Context):
        self.currentNode = self.currentNode.parent

    def enterBoolop(self, ctx:cParser.BoolopContext):
        string = ""
        if ctx.AND():
            string = str(ctx.AND())
        else:
            string = str(ctx.OR())
        node = self.create_node(string, self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitBoolop(self, ctx:cParser.BoolopContext):
        self.currentNode = self.currentNode.parent

    def enterIncrement(self, ctx:cParser.IncrementContext):
        node = self.create_node("increment", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()

    def exitIncrement(self, ctx:cParser.IncrementContext):
        self.currentNode = self.currentNode.parent

    def enterIncrement_op_first(self, ctx:cParser.Increment_op_firstContext):
        node = self.create_node("Increment_op", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        string = '--'
        if ctx.PLUSPLUS():
            string = '++'

        node2 = self.create_node(string, self.currentNode, ctx)
        node1 = self.create_node(str(ctx.IDENTIFIER()), self.currentNode, ctx)
        self.currentNode.children.append(node1)
        self.currentNode.children.append(node2)
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()
        node1.symbol_table = self.symbol_table.get_currentScope()
        node2.symbol_table = self.symbol_table.get_currentScope()


    def exitIncrement_op_first(self, ctx:cParser.Increment_op_firstContext):
        self.currentNode = self.currentNode.parent

    def enterIncrement_var_first(self, ctx:cParser.Increment_var_firstContext):
        node = self.create_node("Increment_var", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        string = '--'
        if ctx.PLUSPLUS():
            string = '++'

        node2 = self.create_node(string, self.currentNode, ctx)
        node1 = self.create_node(str(ctx.IDENTIFIER()), self.currentNode, ctx)
        self.currentNode.children.append(node1)
        self.currentNode.children.append(node2)
        self.currentNode.symbol_table = self.symbol_table.get_currentScope()
        node1.symbol_table = self.symbol_table.get_currentScope()
        node2.symbol_table = self.symbol_table.get_currentScope()

    def exitIncrement_var_first(self, ctx:cParser.Increment_var_firstContext):
        self.currentNode = self.currentNode.parent

