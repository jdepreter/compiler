from antlr4 import *
from ANTLR.LLVM.grammer1Listener import grammer1Listener
from ANTLR.LLVM.grammer1Parser import grammer1Parser

from ANTLR.LLVM.AST import Node


# Depth first
class KeyPrinter(grammer1Listener):
    def __init__(self):
        self.ast = None
        self.currentNode = None
        self.id = 1

    def create_node(self, label, parent):
        node = Node(self.id, label, parent)
        self.id += 1
        return node

    def enterGram(self, ctx:grammer1Parser.GramContext):
        print("enter gram")
        self.ast = self.create_node("gram", self.ast)
        self.currentNode = self.ast

    def enterLine(self, ctx:grammer1Parser.LineContext):
        print("enter line")
        node = self.create_node("line", self.ast)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitLine(self, ctx:grammer1Parser.LineContext):
        print("exit line")
        self.currentNode = self.currentNode.parent

    def enterBool1(self, ctx:grammer1Parser.Bool1Context):
        node = self.create_node("Bool-1", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitBool1(self, ctx:grammer1Parser.Bool1Context):
        self.currentNode = self.currentNode.parent

    def enterBool2(self, ctx:grammer1Parser.Bool2Context):
        node = self.create_node("Bool2", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitBool2(self, ctx:grammer1Parser.Bool2Context):
        self.currentNode = self.currentNode.parent

    def enterExpr(self, ctx:grammer1Parser.ExprContext):
        node = self.create_node("expr", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitExpr(self, ctx:grammer1Parser.ExprContext):
        self.currentNode = self.currentNode.parent

    def enterPlus(self, ctx:grammer1Parser.PlusContext):
        if len(ctx.PLUS()) > 0:
            node = self.create_node("+", self.currentNode)
        else:
            node = self.create_node("-", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitPlus(self, ctx:grammer1Parser.PlusContext):
        self.currentNode = self.currentNode.parent

    def enterVm(self, ctx:grammer1Parser.VmContext):
        if len(ctx.MAAL()) > 0:
            node = self.create_node("*", self.currentNode)
        else:
            node = self.create_node("/", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitVm(self, ctx:grammer1Parser.VmContext):
        self.currentNode = self.currentNode.parent

    def enterMod(self, ctx:grammer1Parser.ModContext):
        node = self.create_node("mod", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitMod(self, ctx:grammer1Parser.ModContext):
        self.currentNode = self.currentNode.parent

    def enterNeg_sol(self, ctx:grammer1Parser.Neg_solContext):
        node = self.create_node("negsol", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitNeg_sol(self, ctx:grammer1Parser.Neg_solContext):
        self.currentNode = self.currentNode.parent

    def enterVm_sol(self, ctx:grammer1Parser.Vm_solContext):
        node = self.create_node("vmsol", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitVm_sol(self, ctx:grammer1Parser.Vm_solContext):
        self.currentNode = self.currentNode.parent

    def enterValue(self, ctx:grammer1Parser.ValueContext):
        node = self.create_node(str(ctx.INT()), self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitValue(self, ctx:grammer1Parser.ValueContext):
        self.currentNode = self.currentNode.parent

    def enterNeg_value(self, ctx:grammer1Parser.Neg_valueContext):
        node = self.create_node(str(ctx.NEG_INT()), self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitNeg_value(self, ctx:grammer1Parser.Neg_valueContext):
        self.currentNode = self.currentNode.parent
