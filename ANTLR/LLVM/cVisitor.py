# Generated from ./ANTLR/LLVM/c.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cParser import cParser
else:
    from ANTLR.LLVM.cParser import cParser

# This class defines a complete generic visitor for a parse tree produced by cParser.

class cVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cParser#c.
    def visitC(self, ctx:cParser.CContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#line.
    def visitLine(self, ctx:cParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#scope.
    def visitScope(self, ctx:cParser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#definition.
    def visitDefinition(self, ctx:cParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#declaration.
    def visitDeclaration(self, ctx:cParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#assignment.
    def visitAssignment(self, ctx:cParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#var_type.
    def visitVar_type(self, ctx:cParser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#pointer_type.
    def visitPointer_type(self, ctx:cParser.Pointer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#bool1.
    def visitBool1(self, ctx:cParser.Bool1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#bool2.
    def visitBool2(self, ctx:cParser.Bool2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#plus.
    def visitPlus(self, ctx:cParser.PlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#vm.
    def visitVm(self, ctx:cParser.VmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#mod.
    def visitMod(self, ctx:cParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#neg_sol.
    def visitNeg_sol(self, ctx:cParser.Neg_solContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#vm_sol.
    def visitVm_sol(self, ctx:cParser.Vm_solContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#neg_value.
    def visitNeg_value(self, ctx:cParser.Neg_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#value.
    def visitValue(self, ctx:cParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#operator.
    def visitOperator(self, ctx:cParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#operator2.
    def visitOperator2(self, ctx:cParser.Operator2Context):
        return self.visitChildren(ctx)



del cParser