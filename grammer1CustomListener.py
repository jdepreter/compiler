from antlr4 import *
from ANTLR.LLVM.grammer1Listener import grammer1Listener
from ANTLR.LLVM.grammer1Parser import grammer1Parser

from ANTLR.LLVM.AST import Node


# Depth first
class KeyPrinter(grammer1Listener):
    def __init__(self, file):
        self.ast = Node(0, "ast", None, [])
        self.currentNode = None
        self.id = 1

    def create_node(self, label, parent):
        node = Node(self.id, label, parent)
        self.id += 1
        return node

    def enterLine(self, ctx:grammer1Parser.LineContext):
        print("enter line")
        node = self.create_node("line", self.ast)
        self.ast.children.append(node)
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
        node = self.create_node("Bool-2", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitBool2(self, ctx:grammer1Parser.Bool2Context):
        self.currentNode = self.currentNode.parent

    def enterPlus(self, ctx:grammer1Parser.PlusContext):
        node = self.create_node("plus", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitPlus(self, ctx:grammer1Parser.PlusContext):
        self.currentNode = self.currentNode.parent

    def enterVm(self, ctx:grammer1Parser.VmContext):
        node = self.create_node("vm", self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitVm(self, ctx:grammer1Parser.VmContext):
        self.currentNode = self.currentNode.parent

    def enterValue(self, ctx:grammer1Parser.ValueContext):
        node = self.create_node(str(ctx.INT()), self.currentNode)
        self.currentNode.children.append(node)
        self.currentNode = node

    def exitValue(self, ctx:grammer1Parser.ValueContext):
        self.currentNode = self.currentNode.parent