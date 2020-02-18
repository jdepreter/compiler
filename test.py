import sys
from antlr4 import *
from ANTLR.LLVM.grammer1Lexer import grammer1Lexer
from ANTLR.LLVM.grammer1Parser import grammer1Parser
from grammer1CustomListener import KeyPrinter


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = grammer1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammer1Parser(stream)
    tree = parser.gram()
    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main(sys.argv)
