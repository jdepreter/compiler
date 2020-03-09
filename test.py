import sys
from antlr4 import *
from ANTLR.LLVM.grammer1Lexer import grammer1Lexer
from ANTLR.LLVM.cLexer import cLexer
from ANTLR.LLVM.grammer1Parser import grammer1Parser
from ANTLR.LLVM.cParser import cParser
from ANTLR.LLVM.grammer1Visitor import grammer1Visitor
from grammer1CustomListener import KeyPrinter
from cCustomListener import CASTGenerator
from ANTLR.LLVM.AST import ASTVisitor
from graphviz import Digraph


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = cLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = cParser(stream)
    tree = parser.c()
    printer = CASTGenerator()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    # printer.ast.to_dot(open("temp.dot", 'w'))
    visitor = ASTVisitor(printer.ast)
    # visitor.constant_folding()
    visitor.clean_tree()
    graph = printer.ast.render_dot()
    graph.save("1.txt", "output")
    graph.render("1")
    visitor.maal()
    graph = printer.ast.render_dot()
    graph.save("output.txt", "output")
    graph.render("output")

if __name__ == '__main__':
    main(sys.argv)
