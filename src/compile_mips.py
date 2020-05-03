import struct
import sys
from antlr4 import *
from ANTLR.LLVM.cLexer import cLexer
from ANTLR.LLVM.cParser import cParser
from src.cCustomListener import CASTGenerator
from src.AST import ASTVisitor
from src.LLVM_CONVERTER import LLVM_Converter
from src.MIPS_CONVERTER import MIPS_Converter

from src.cErrorListener import CErrorListener

import platform
from subprocess import check_output, CalledProcessError
from pathlib import Path
from src.symbolTables import SymbolTable


def to_llvm(filename, outputname):
    SymbolTable.main_defined = False
    Path("llvm").mkdir(parents=True, exist_ok=True)
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
    graph.save("{}-before".format(outputname), "trees")
    graph.render("{}-before".format(outputname))
    visitor.startnode.symbol_table.no_main()
    visitor.startnode.symbol_table.warn_unused()
    visitor.clean_tree()
    visitor.fold_not()
    # TODO add simple clean to fold_not so it doesn't need to be rerun
    visitor.clean_tree()
    visitor.unary_fold()
    visitor.maal()
    visitor.constant_folding()

    graph = printer.ast.render_dot()
    graph.save("{}".format(outputname), "trees")
    graph.render("{}".format(outputname))
    f = open('./asm/{}.asm'.format(outputname), 'w')
    converter = MIPS_Converter(visitor, f)
    converter.to_mips()
    f.close()

    if platform.system() == 'Linux':
        result = ''
        try:
            result = check_output(
                "spim -file ./asm/{}.asm ".format(outputname, outputname, outputname),
                shell=True).decode("utf-8")
        except CalledProcessError as e:
            if e.returncode != 1:
                raise e
            else:
                result = e.output.decode("utf-8")
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
