# Generated from ./ANTLR/LLVM/grammer1.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .grammer1Parser import grammer1Parser
else:
    from grammer1Parser import grammer1Parser

# This class defines a complete listener for a parse tree produced by grammer1Parser.
class grammer1Listener(ParseTreeListener):

    # Enter a parse tree produced by grammer1Parser#gram.
    def enterGram(self, ctx:grammer1Parser.GramContext):
        pass

    # Exit a parse tree produced by grammer1Parser#gram.
    def exitGram(self, ctx:grammer1Parser.GramContext):
        pass


    # Enter a parse tree produced by grammer1Parser#line.
    def enterLine(self, ctx:grammer1Parser.LineContext):
        pass

    # Exit a parse tree produced by grammer1Parser#line.
    def exitLine(self, ctx:grammer1Parser.LineContext):
        pass


    # Enter a parse tree produced by grammer1Parser#bool1.
    def enterBool1(self, ctx:grammer1Parser.Bool1Context):
        pass

    # Exit a parse tree produced by grammer1Parser#bool1.
    def exitBool1(self, ctx:grammer1Parser.Bool1Context):
        pass


    # Enter a parse tree produced by grammer1Parser#bool2.
    def enterBool2(self, ctx:grammer1Parser.Bool2Context):
        pass

    # Exit a parse tree produced by grammer1Parser#bool2.
    def exitBool2(self, ctx:grammer1Parser.Bool2Context):
        pass


    # Enter a parse tree produced by grammer1Parser#expr.
    def enterExpr(self, ctx:grammer1Parser.ExprContext):
        pass

    # Exit a parse tree produced by grammer1Parser#expr.
    def exitExpr(self, ctx:grammer1Parser.ExprContext):
        pass


    # Enter a parse tree produced by grammer1Parser#plus.
    def enterPlus(self, ctx:grammer1Parser.PlusContext):
        pass

    # Exit a parse tree produced by grammer1Parser#plus.
    def exitPlus(self, ctx:grammer1Parser.PlusContext):
        pass


    # Enter a parse tree produced by grammer1Parser#vm.
    def enterVm(self, ctx:grammer1Parser.VmContext):
        pass

    # Exit a parse tree produced by grammer1Parser#vm.
    def exitVm(self, ctx:grammer1Parser.VmContext):
        pass


    # Enter a parse tree produced by grammer1Parser#mod.
    def enterMod(self, ctx:grammer1Parser.ModContext):
        pass

    # Exit a parse tree produced by grammer1Parser#mod.
    def exitMod(self, ctx:grammer1Parser.ModContext):
        pass


    # Enter a parse tree produced by grammer1Parser#neg_sol.
    def enterNeg_sol(self, ctx:grammer1Parser.Neg_solContext):
        pass

    # Exit a parse tree produced by grammer1Parser#neg_sol.
    def exitNeg_sol(self, ctx:grammer1Parser.Neg_solContext):
        pass


    # Enter a parse tree produced by grammer1Parser#vm_sol.
    def enterVm_sol(self, ctx:grammer1Parser.Vm_solContext):
        pass

    # Exit a parse tree produced by grammer1Parser#vm_sol.
    def exitVm_sol(self, ctx:grammer1Parser.Vm_solContext):
        pass


    # Enter a parse tree produced by grammer1Parser#neg_value.
    def enterNeg_value(self, ctx:grammer1Parser.Neg_valueContext):
        pass

    # Exit a parse tree produced by grammer1Parser#neg_value.
    def exitNeg_value(self, ctx:grammer1Parser.Neg_valueContext):
        pass


    # Enter a parse tree produced by grammer1Parser#value.
    def enterValue(self, ctx:grammer1Parser.ValueContext):
        pass

    # Exit a parse tree produced by grammer1Parser#value.
    def exitValue(self, ctx:grammer1Parser.ValueContext):
        pass



del grammer1Parser