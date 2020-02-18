# Generated from ./ANTLR/LLVM/grammer1.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .grammer1Parser import grammer1Parser
else:
    from grammer1Parser import grammer1Parser

# This class defines a complete generic visitor for a parse tree produced by grammer1Parser.

class grammer1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by grammer1Parser#gram.
    def visitGram(self, ctx:grammer1Parser.GramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammer1Parser#line.
    def visitLine(self, ctx:grammer1Parser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammer1Parser#bool1.
    def visitBool1(self, ctx:grammer1Parser.Bool1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammer1Parser#bool2.
    def visitBool2(self, ctx:grammer1Parser.Bool2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammer1Parser#expr.
    def visitExpr(self, ctx:grammer1Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammer1Parser#plus.
    def visitPlus(self, ctx:grammer1Parser.PlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammer1Parser#vm.
    def visitVm(self, ctx:grammer1Parser.VmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammer1Parser#mod.
    def visitMod(self, ctx:grammer1Parser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammer1Parser#neg_sol.
    def visitNeg_sol(self, ctx:grammer1Parser.Neg_solContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammer1Parser#vm_sol.
    def visitVm_sol(self, ctx:grammer1Parser.Vm_solContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammer1Parser#neg_value.
    def visitNeg_value(self, ctx:grammer1Parser.Neg_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammer1Parser#value.
    def visitValue(self, ctx:grammer1Parser.ValueContext):
        return self.visitChildren(ctx)



del grammer1Parser