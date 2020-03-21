import struct
import sys
from antlr4 import *
from ANTLR.LLVM.cLexer import cLexer
from ANTLR.LLVM.cParser import cParser
from cCustomListener import CASTGenerator
from AST import ASTVisitor
from LLVM_CONVERTER import LLVM_Converter

from cErrorListener import CErrorListener

import os, platform
from subprocess import check_output


def to_llvm(filename, outputname ):
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
    graph = printer.ast.render_dot()
    graph.save("1.txt", "output")
    graph.render("1")
    visitor.startnode.symbol_table.warn_unused()
    visitor.clean_tree()
    visitor.fold_not()
    # TODO add simple clean to fold_not so it doesn't need to be rerun
    visitor.clean_tree()
    visitor.unary_fold()
    visitor.maal()
    visitor.constant_folding()
    graph = printer.ast.render_dot()
    graph.save("output-{}".format(outputname), "output")
    graph.render("output-{}".format(outputname))
    f = open('llvm-{}.ll'.format(outputname), 'w')
    converter = LLVM_Converter(visitor, f)
    converter.to_llvm()
    f.close()

    if platform.system() == 'Linux':
        result = check_output("clang llvm-{}.ll -o {} && ./{}".format(outputname, outputname, outputname), shell=True)\
            .decode("utf-8")
        return result


def double_to_hex(f):
    hex_string = hex(struct.unpack('<Q', struct.pack('<d', f))[0])
    hex_string = hex_string[:11]
    hex_string += "0000000"
    return hex_string


def main(argv):
    # print(double_to_hex(12.99))
    print(to_llvm(argv[1], argv[2]))


if __name__ == '__main__':
    main(sys.argv)
