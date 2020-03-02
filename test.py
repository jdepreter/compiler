import sys
from antlr4 import *
from ANTLR.LLVM.grammer1Lexer import grammer1Lexer
from ANTLR.LLVM.grammer1Parser import grammer1Parser
from ANTLR.LLVM.grammer1Visitor import grammer1Visitor
from grammer1CustomListener import KeyPrinter
from ANTLR.LLVM.AST import ASTVisitor
from graphviz import Digraph


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = grammer1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammer1Parser(stream)
    tree = parser.gram()
    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    # printer.ast.to_dot(open("temp.dot", 'w'))
    visitor = ASTVisitor(printer.ast)
    visitor.constant_folding()
    graph = printer.ast.render_dot()
    graph.save("output.txt", "output")
    graph.render("output.txt")

if __name__ == '__main__':
    main(sys.argv)
