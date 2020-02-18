from antlr4 import *
from ANTLR.LLVM.grammer1Listener import grammer1Listener
from ANTLR.LLVM.grammer1Parser import grammer1Parser


class KeyPrinter(grammer1Listener):
    def enterLine(self, ctx:grammer1Parser.LineContext):
        print("enter line")

    def exitLine(self, ctx:grammer1Parser.LineContext):
        print("exit line")

