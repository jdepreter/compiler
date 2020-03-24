# Generated from ./ANTLR/LLVM/c.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cParser import cParser
else:
    from cParser import cParser

# This class defines a complete generic visitor for a parse tree produced by cParser.

class cVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cParser#c.
    def visitC(self, ctx:cParser.CContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#line.
    def visitLine(self, ctx:cParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#line_no_def.
    def visitLine_no_def(self, ctx:cParser.Line_no_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#scope.
    def visitScope(self, ctx:cParser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#ifelse.
    def visitIfelse(self, ctx:cParser.IfelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#for_loop.
    def visitFor_loop(self, ctx:cParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#while_loop.
    def visitWhile_loop(self, ctx:cParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#for_initial.
    def visitFor_initial(self, ctx:cParser.For_initialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#condition.
    def visitCondition(self, ctx:cParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#for_update.
    def visitFor_update(self, ctx:cParser.For_updateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#break_line.
    def visitBreak_line(self, ctx:cParser.Break_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#do_block.
    def visitDo_block(self, ctx:cParser.Do_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#switchcase.
    def visitSwitchcase(self, ctx:cParser.SwitchcaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#case.
    def visitCase(self, ctx:cParser.CaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#default.
    def visitDefault(self, ctx:cParser.DefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#method_call.
    def visitMethod_call(self, ctx:cParser.Method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#args.
    def visitArgs(self, ctx:cParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#definition.
    def visitDefinition(self, ctx:cParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#variable_identifier.
    def visitVariable_identifier(self, ctx:cParser.Variable_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#assignment_line.
    def visitAssignment_line(self, ctx:cParser.Assignment_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#assignment.
    def visitAssignment(self, ctx:cParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#assignment2.
    def visitAssignment2(self, ctx:cParser.Assignment2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#var_type.
    def visitVar_type(self, ctx:cParser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#increment.
    def visitIncrement(self, ctx:cParser.IncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#increment_var_first.
    def visitIncrement_var_first(self, ctx:cParser.Increment_var_firstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#increment_op_first.
    def visitIncrement_op_first(self, ctx:cParser.Increment_op_firstContext):
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


    # Visit a parse tree produced by cParser#boolop.
    def visitBoolop(self, ctx:cParser.BoolopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#not_value.
    def visitNot_value(self, ctx:cParser.Not_valueContext):
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


    # Visit a parse tree produced by cParser#value.
    def visitValue(self, ctx:cParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#rvalue.
    def visitRvalue(self, ctx:cParser.RvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#lvalue.
    def visitLvalue(self, ctx:cParser.LvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#dereference.
    def visitDereference(self, ctx:cParser.DereferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#address.
    def visitAddress(self, ctx:cParser.AddressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#operator.
    def visitOperator(self, ctx:cParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#operator2.
    def visitOperator2(self, ctx:cParser.Operator2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#unary_min.
    def visitUnary_min(self, ctx:cParser.Unary_minContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cParser#unary_plus.
    def visitUnary_plus(self, ctx:cParser.Unary_plusContext):
        return self.visitChildren(ctx)



del cParser