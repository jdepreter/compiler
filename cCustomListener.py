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

    def create_node(self, label, parent):
        node = Node(self.id, label, parent)
        self.id += 1
        return node

    def enterC(self, ctx:cParser.CContext):
        print("enter c")
        self.ast = self.create_node("C", self.currentNode)
        self.currentNode = self.ast
        self.symbol_table.open_scope()

    def enterLine(self, ctx:cParser.LineContext):
        print("enter line")
        node = self.create_node("line", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitLine(self, ctx:cParser.LineContext):
        print("exit line")
        self.currentNode = self.currentNode.parent

    def enterAssignment(self, ctx:cParser.AssignmentContext):
        node = self.create_node("ass", self.currentNode)
        identifier = self.create_node(str(ctx.IDENTIFIER()), node)
        node.children.append(identifier)
        self.currentNode.children.append(node)
        self.currentNode = node

    def enterDeclaration(self, ctx:cParser.DeclarationContext):
        node = self.create_node("dec", self.currentNode)
        identifier = self.create_node(str(ctx.IDENTIFIER()), node)
        node.children.append(identifier)
        self.currentNode.children.append(node)
        self.currentNode = node


    def enterDefinition(self, ctx:cParser.DefinitionContext):
        node = self.create_node("def", self.currentNode)
        identifier = self.create_node(str(ctx.IDENTIFIER()), node)
        node.children.append(identifier)
        self.currentNode.children.append(node)
        self.currentNode = node

    def enterPointer_type(self, ctx:cParser.Pointer_typeContext):
        string = "pointer"
        if ctx.CHAR_TYPE():
            string = str(ctx.CHAR_TYPE())
        if ctx.FLOAT_TYPE():
            string = str(ctx.FLOAT_TYPE())
        if ctx.INT_TYPE():
            string = str(ctx.INT_TYPE())
        node = self.create_node(string, self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def enterVar_type(self, ctx:cParser.Var_typeContext):
        string = "pointer"
        if ctx.CHAR_TYPE():
            string = str(ctx.CHAR_TYPE())
        if ctx.FLOAT_TYPE():
            string = str(ctx.FLOAT_TYPE())
        if ctx.INT_TYPE():
            string = str(ctx.INT_TYPE())

        node = self.create_node(string, self.currentNode)
        self.currentNode.children.insert(0, node)
        self.currentNode = node

    def exitAssignment(self, ctx:cParser.AssignmentContext):
        self.symbol_table.get_symbol(self.currentNode.children[0].label)
        self.currentNode = self.currentNode.parent

    def exitDeclaration(self, ctx:cParser.DeclarationContext):
        self.symbol_table.add_symbol(self.currentNode.children[1].label, self.currentNode.children[0].label, False)
        self.currentNode = self.currentNode.parent

    def exitDefinition(self, ctx:cParser.DefinitionContext):
        if ctx.CONST():
            node = self.create_node("const", self.currentNode)
            self.currentNode.children.insert(0, node)
            self.symbol_table.add_symbol(self.currentNode.children[2].label, self.currentNode.children[1].label, True, True)
        else:
            self.symbol_table.add_symbol(self.currentNode.children[1].label, self.currentNode.children[0].label, True)

        self.currentNode = self.currentNode.parent

    def exitPointer_type(self, ctx:cParser.Pointer_typeContext):
        self.currentNode = self.currentNode.parent

    def exitVar_type(self, ctx:cParser.Var_typeContext):
        self.currentNode = self.currentNode.parent

    # Expressions ----
    def enterBool1(self, ctx:cParser.Bool1Context):
        node = self.create_node("Bool1", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitBool1(self, ctx:cParser.Bool1Context):
        self.currentNode = self.currentNode.parent

    def enterBool2(self, ctx:cParser.Bool2Context):
        node = self.create_node("Bool2", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitBool2(self, ctx:cParser.Bool2Context):
        self.currentNode = self.currentNode.parent

    def enterPlus(self, ctx:cParser.PlusContext):
        node = self.create_node("plus", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitPlus(self, ctx:cParser.PlusContext):
        self.currentNode = self.currentNode.parent

    def enterVm(self, ctx:cParser.VmContext):
        node = self.create_node("vm", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitVm(self, ctx:cParser.VmContext):
        self.currentNode = self.currentNode.parent

    def enterMod(self, ctx:cParser.ModContext):
        print("entermod")
        node = self.create_node("mod", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitMod(self, ctx:cParser.ModContext):
        print("exitmod")
        self.currentNode = self.currentNode.parent

    def enterNeg_sol(self, ctx:cParser.Neg_solContext):
        node = self.create_node("negsol", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitNeg_sol(self, ctx:cParser.Neg_solContext):
        self.currentNode = self.currentNode.parent

    def enterVm_sol(self, ctx:cParser.Vm_solContext):
        node = self.create_node("vmsol", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitVm_sol(self, ctx:cParser.Vm_solContext):
        self.currentNode = self.currentNode.parent

    def enterValue(self, ctx:cParser.ValueContext):
        string = "nothing"
        if ctx.INT():
            string = str(ctx.INT())
        elif ctx.IDENTIFIER():
            string = ctx.IDENTIFIER()
        node = self.create_node(string, self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitValue(self, ctx:cParser.ValueContext):
        self.currentNode = self.currentNode.parent

    def enterNeg_value(self, ctx:cParser.Neg_valueContext):
        node = self.create_node(str(ctx.NEG_INT()), self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitNeg_value(self, ctx:cParser.Neg_valueContext):
        self.currentNode = self.currentNode.parent

    def enterOperator(self, ctx:cParser.OperatorContext):
        print("enterop")
        string = ""
        if ctx.MAAL():
            string = str(ctx.MAAL())
        else:
            string = str(ctx.DEEL())
        node = self.create_node(string, self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitOperator(self, ctx:cParser.OperatorContext):
        print('exitop')
        self.currentNode = self.currentNode.parent

    def enterOperator2(self, ctx:cParser.Operator2Context):
        print("enterop")
        string = ""
        if ctx.PLUS():
            string = str(ctx.PLUS())
        else:
            string = str(ctx.MIN())
        node = self.create_node(string, self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitOperator2(self, ctx:cParser.Operator2Context):
        print('exitop')
        self.currentNode = self.currentNode.parent