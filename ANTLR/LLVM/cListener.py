# Generated from ./ANTLR/LLVM/c.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cParser import cParser
else:
    from ANTLR.LLVM.cParser import cParser

# This class defines a complete listener for a parse tree produced by cParser.
class cListener(ParseTreeListener):

    # Enter a parse tree produced by cParser#c.
    def enterC(self, ctx:cParser.CContext):
        pass

    # Exit a parse tree produced by cParser#c.
    def exitC(self, ctx:cParser.CContext):
        pass


    # Enter a parse tree produced by cParser#line.
    def enterLine(self, ctx:cParser.LineContext):
        pass

    # Exit a parse tree produced by cParser#line.
    def exitLine(self, ctx:cParser.LineContext):
        pass


    # Enter a parse tree produced by cParser#scope.
    def enterScope(self, ctx:cParser.ScopeContext):
        pass

    # Exit a parse tree produced by cParser#scope.
    def exitScope(self, ctx:cParser.ScopeContext):
        pass


    # Enter a parse tree produced by cParser#ifelse.
    def enterIfelse(self, ctx:cParser.IfelseContext):
        pass

    # Exit a parse tree produced by cParser#ifelse.
    def exitIfelse(self, ctx:cParser.IfelseContext):
        pass


    # Enter a parse tree produced by cParser#for_loop.
    def enterFor_loop(self, ctx:cParser.For_loopContext):
        pass

    # Exit a parse tree produced by cParser#for_loop.
    def exitFor_loop(self, ctx:cParser.For_loopContext):
        pass


    # Enter a parse tree produced by cParser#while_loop.
    def enterWhile_loop(self, ctx:cParser.While_loopContext):
        pass

    # Exit a parse tree produced by cParser#while_loop.
    def exitWhile_loop(self, ctx:cParser.While_loopContext):
        pass


    # Enter a parse tree produced by cParser#for_initial.
    def enterFor_initial(self, ctx:cParser.For_initialContext):
        pass

    # Exit a parse tree produced by cParser#for_initial.
    def exitFor_initial(self, ctx:cParser.For_initialContext):
        pass


    # Enter a parse tree produced by cParser#condition.
    def enterCondition(self, ctx:cParser.ConditionContext):
        pass

    # Exit a parse tree produced by cParser#condition.
    def exitCondition(self, ctx:cParser.ConditionContext):
        pass


    # Enter a parse tree produced by cParser#for_update.
    def enterFor_update(self, ctx:cParser.For_updateContext):
        pass

    # Exit a parse tree produced by cParser#for_update.
    def exitFor_update(self, ctx:cParser.For_updateContext):
        pass


    # Enter a parse tree produced by cParser#break_line.
    def enterBreak_line(self, ctx:cParser.Break_lineContext):
        pass

    # Exit a parse tree produced by cParser#break_line.
    def exitBreak_line(self, ctx:cParser.Break_lineContext):
        pass


    # Enter a parse tree produced by cParser#do_block.
    def enterDo_block(self, ctx:cParser.Do_blockContext):
        pass

    # Exit a parse tree produced by cParser#do_block.
    def exitDo_block(self, ctx:cParser.Do_blockContext):
        pass


    # Enter a parse tree produced by cParser#switchcase.
    def enterSwitchcase(self, ctx:cParser.SwitchcaseContext):
        pass

    # Exit a parse tree produced by cParser#switchcase.
    def exitSwitchcase(self, ctx:cParser.SwitchcaseContext):
        pass


    # Enter a parse tree produced by cParser#method_call.
    def enterMethod_call(self, ctx:cParser.Method_callContext):
        pass

    # Exit a parse tree produced by cParser#method_call.
    def exitMethod_call(self, ctx:cParser.Method_callContext):
        pass


    # Enter a parse tree produced by cParser#args.
    def enterArgs(self, ctx:cParser.ArgsContext):
        pass

    # Exit a parse tree produced by cParser#args.
    def exitArgs(self, ctx:cParser.ArgsContext):
        pass


    # Enter a parse tree produced by cParser#definition.
    def enterDefinition(self, ctx:cParser.DefinitionContext):
        pass

    # Exit a parse tree produced by cParser#definition.
    def exitDefinition(self, ctx:cParser.DefinitionContext):
        pass


    # Enter a parse tree produced by cParser#variable_identifier.
    def enterVariable_identifier(self, ctx:cParser.Variable_identifierContext):
        pass

    # Exit a parse tree produced by cParser#variable_identifier.
    def exitVariable_identifier(self, ctx:cParser.Variable_identifierContext):
        pass


    # Enter a parse tree produced by cParser#assignment_line.
    def enterAssignment_line(self, ctx:cParser.Assignment_lineContext):
        pass

    # Exit a parse tree produced by cParser#assignment_line.
    def exitAssignment_line(self, ctx:cParser.Assignment_lineContext):
        pass


    # Enter a parse tree produced by cParser#assignment.
    def enterAssignment(self, ctx:cParser.AssignmentContext):
        pass

    # Exit a parse tree produced by cParser#assignment.
    def exitAssignment(self, ctx:cParser.AssignmentContext):
        pass


    # Enter a parse tree produced by cParser#assignment2.
    def enterAssignment2(self, ctx:cParser.Assignment2Context):
        pass

    # Exit a parse tree produced by cParser#assignment2.
    def exitAssignment2(self, ctx:cParser.Assignment2Context):
        pass


    # Enter a parse tree produced by cParser#var_type.
    def enterVar_type(self, ctx:cParser.Var_typeContext):
        pass

    # Exit a parse tree produced by cParser#var_type.
    def exitVar_type(self, ctx:cParser.Var_typeContext):
        pass


    # Enter a parse tree produced by cParser#increment.
    def enterIncrement(self, ctx:cParser.IncrementContext):
        pass

    # Exit a parse tree produced by cParser#increment.
    def exitIncrement(self, ctx:cParser.IncrementContext):
        pass


    # Enter a parse tree produced by cParser#increment_var_first.
    def enterIncrement_var_first(self, ctx:cParser.Increment_var_firstContext):
        pass

    # Exit a parse tree produced by cParser#increment_var_first.
    def exitIncrement_var_first(self, ctx:cParser.Increment_var_firstContext):
        pass


    # Enter a parse tree produced by cParser#increment_op_first.
    def enterIncrement_op_first(self, ctx:cParser.Increment_op_firstContext):
        pass

    # Exit a parse tree produced by cParser#increment_op_first.
    def exitIncrement_op_first(self, ctx:cParser.Increment_op_firstContext):
        pass


    # Enter a parse tree produced by cParser#pointer_type.
    def enterPointer_type(self, ctx:cParser.Pointer_typeContext):
        pass

    # Exit a parse tree produced by cParser#pointer_type.
    def exitPointer_type(self, ctx:cParser.Pointer_typeContext):
        pass


    # Enter a parse tree produced by cParser#bool1.
    def enterBool1(self, ctx:cParser.Bool1Context):
        pass

    # Exit a parse tree produced by cParser#bool1.
    def exitBool1(self, ctx:cParser.Bool1Context):
        pass


    # Enter a parse tree produced by cParser#bool2.
    def enterBool2(self, ctx:cParser.Bool2Context):
        pass

    # Exit a parse tree produced by cParser#bool2.
    def exitBool2(self, ctx:cParser.Bool2Context):
        pass


    # Enter a parse tree produced by cParser#boolop.
    def enterBoolop(self, ctx:cParser.BoolopContext):
        pass

    # Exit a parse tree produced by cParser#boolop.
    def exitBoolop(self, ctx:cParser.BoolopContext):
        pass


    # Enter a parse tree produced by cParser#not_value.
    def enterNot_value(self, ctx:cParser.Not_valueContext):
        pass

    # Exit a parse tree produced by cParser#not_value.
    def exitNot_value(self, ctx:cParser.Not_valueContext):
        pass


    # Enter a parse tree produced by cParser#plus.
    def enterPlus(self, ctx:cParser.PlusContext):
        pass

    # Exit a parse tree produced by cParser#plus.
    def exitPlus(self, ctx:cParser.PlusContext):
        pass


    # Enter a parse tree produced by cParser#vm.
    def enterVm(self, ctx:cParser.VmContext):
        pass

    # Exit a parse tree produced by cParser#vm.
    def exitVm(self, ctx:cParser.VmContext):
        pass


    # Enter a parse tree produced by cParser#mod.
    def enterMod(self, ctx:cParser.ModContext):
        pass

    # Exit a parse tree produced by cParser#mod.
    def exitMod(self, ctx:cParser.ModContext):
        pass


    # Enter a parse tree produced by cParser#neg_sol.
    def enterNeg_sol(self, ctx:cParser.Neg_solContext):
        pass

    # Exit a parse tree produced by cParser#neg_sol.
    def exitNeg_sol(self, ctx:cParser.Neg_solContext):
        pass


    # Enter a parse tree produced by cParser#vm_sol.
    def enterVm_sol(self, ctx:cParser.Vm_solContext):
        pass

    # Exit a parse tree produced by cParser#vm_sol.
    def exitVm_sol(self, ctx:cParser.Vm_solContext):
        pass


    # Enter a parse tree produced by cParser#value.
    def enterValue(self, ctx:cParser.ValueContext):
        pass

    # Exit a parse tree produced by cParser#value.
    def exitValue(self, ctx:cParser.ValueContext):
        pass


    # Enter a parse tree produced by cParser#rvalue.
    def enterRvalue(self, ctx:cParser.RvalueContext):
        pass

    # Exit a parse tree produced by cParser#rvalue.
    def exitRvalue(self, ctx:cParser.RvalueContext):
        pass


    # Enter a parse tree produced by cParser#lvalue.
    def enterLvalue(self, ctx:cParser.LvalueContext):
        pass

    # Exit a parse tree produced by cParser#lvalue.
    def exitLvalue(self, ctx:cParser.LvalueContext):
        pass


    # Enter a parse tree produced by cParser#dereference.
    def enterDereference(self, ctx:cParser.DereferenceContext):
        pass

    # Exit a parse tree produced by cParser#dereference.
    def exitDereference(self, ctx:cParser.DereferenceContext):
        pass


    # Enter a parse tree produced by cParser#address.
    def enterAddress(self, ctx:cParser.AddressContext):
        pass

    # Exit a parse tree produced by cParser#address.
    def exitAddress(self, ctx:cParser.AddressContext):
        pass


    # Enter a parse tree produced by cParser#operator.
    def enterOperator(self, ctx:cParser.OperatorContext):
        pass

    # Exit a parse tree produced by cParser#operator.
    def exitOperator(self, ctx:cParser.OperatorContext):
        pass


    # Enter a parse tree produced by cParser#operator2.
    def enterOperator2(self, ctx:cParser.Operator2Context):
        pass

    # Exit a parse tree produced by cParser#operator2.
    def exitOperator2(self, ctx:cParser.Operator2Context):
        pass


    # Enter a parse tree produced by cParser#unary_min.
    def enterUnary_min(self, ctx:cParser.Unary_minContext):
        pass

    # Exit a parse tree produced by cParser#unary_min.
    def exitUnary_min(self, ctx:cParser.Unary_minContext):
        pass


    # Enter a parse tree produced by cParser#unary_plus.
    def enterUnary_plus(self, ctx:cParser.Unary_plusContext):
        pass

    # Exit a parse tree produced by cParser#unary_plus.
    def exitUnary_plus(self, ctx:cParser.Unary_plusContext):
        pass



del cParser