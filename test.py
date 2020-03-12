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
from ANTLR.LLVM.LLVM_CONVERTER import LLVM_Converter

from cErrorListener import CErrorListener


def to_llvm(filename):
    input_stream = FileStream(filename)
    lexer = cLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(CErrorListener())
    stream = CommonTokenStream(lexer)
    parser = cParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CErrorListener())
    tree = parser.c()
    printer = CASTGenerator()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    # printer.ast.to_dot(open("temp.dot", 'w'))
    visitor = ASTVisitor(printer.ast)
    visitor.clean_tree()
    visitor.fold_not()
    # TODO add simple clean to fold_not so it doesn't need to be rerun
    visitor.clean_tree()
    graph = printer.ast.render_dot()
    graph.save("1.txt", "output")
    graph.render("1")
    visitor.maal()
    visitor.constant_folding()
    graph = printer.ast.render_dot()
    graph.save("output-{}".format(filename), "output")
    graph.render("output-{}".format(filename))
    f = open('llvm-{}.llvm'.format(filename), 'w')
    converter = LLVM_Converter(visitor, f)
    converter.to_llvm()
    f.close()


def main(argv):
    to_llvm(argv[1])


if __name__ == '__main__':
    main(sys.argv)
