from ANTLR.LLVM.cListener import cListener
from ANTLR.LLVM.cParser import cParser
from src.symbolTables import SymbolTable
from src.AST import Node
from src.CustomExceptions import ConstAssignment


# Depth first
class CASTGenerator(cListener):
    def __init__(self):
        self.ast = None
        self.currentNode = None
        self.id = 1
        self.symbol_table = SymbolTable()

    def create_node(self, label, node_type, parent, ctx):
        node = Node(self.id, node_type, label, parent, ctx)
        self.id += 1
        return node

    def enterC(self, ctx:cParser.CContext):
        # print("enter c")
        self.ast = self.create_node("C", "C", self.currentNode, ctx)
        self.currentNode = self.ast
        self.symbol_table.open_scope()
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def enterLine(self, ctx:cParser.LineContext):
        # print("enter line")
        node = self.create_node("line", "line", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitLine(self, ctx:cParser.LineContext):
        # print("exit line")
        self.currentNode = self.currentNode.parent

    def enterScope(self, ctx:cParser.ScopeContext):
        # print("enter scope")
        node = self.create_node("scope", "scope", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.symbol_table.open_scope()
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitScope(self, ctx:cParser.ScopeContext):
        # print("exit scope")
        self.symbol_table.close_scope()
        self.currentNode = self.currentNode.parent

    def enterLvalue(self, ctx:cParser.LvalueContext):
        string = ""
        if ctx.IDENTIFIER():
            string = str(ctx.IDENTIFIER())

        node = self.create_node(string, "lvalue", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        if string != "":
            self.currentNode.symbol_type = self.currentNode.symbol_table.get_symbol(string, ctx.start)

    def exitLvalue(self, ctx:cParser.LvalueContext):
        if self.currentNode.label == "":
            self.currentNode.children[0].parent = self.currentNode.parent
            index = self.currentNode.parent.children.index(self.currentNode)
            self.currentNode.parent.children[index] = self.currentNode.children[0]

        temp = self.currentNode
        self.currentNode = self.currentNode.parent
        del temp

    def enterRvalue(self, ctx:cParser.RvalueContext):
        string = "nothing"
        symbol_type = ""
        if ctx.INT():
            string = str(ctx.INT())
            symbol_type = "int"
        elif ctx.FLOAT():
            string = str(ctx.FLOAT())
            symbol_type = "float"
        elif ctx.IDENTIFIER():
            string = str(ctx.IDENTIFIER())
            # symbol_type = "address"
            symbol_type = "&" + self.symbol_table.get_symbol(string, None).symbol_type
        elif ctx.CHAR():
            string = str(ord(str(ctx.CHAR())[1]))
            symbol_type = "char"
        node = self.create_node(string, "rvalue", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        self.currentNode.symbol_type = symbol_type

    def exitRvalue(self, ctx:cParser.RvalueContext):
        self.currentNode = self.currentNode.parent

    def enterDereference(self, ctx:cParser.DereferenceContext):
        string = "lvalue"
        if ctx.IDENTIFIER():
            string = str(ctx.IDENTIFIER())

        star_count = len(ctx.MAAL())
        for i in range(star_count):
            string = '*' + string

        node = self.create_node(string, "lvalue", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        self.currentNode.symbol_type = self.currentNode.symbol_table.get_symbol(string, ctx.start)

    def exitDereference(self, ctx:cParser.DereferenceContext):
        self.currentNode = self.currentNode.parent

    def enterAddress(self, ctx:cParser.AddressContext):
        node = self.create_node("address", "address", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitAddress(self, ctx:cParser.AddressContext):
        self.currentNode = self.currentNode.parent

    def enterAssignment(self, ctx:cParser.AssignmentContext):
        node = self.create_node("assignment", "assignment", self.currentNode, ctx)
        # identifier = self.create_node(str(ctx.IDENTIFIER()), node, ctx)
        # node.children.append(identifier)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def enterAssignment2(self, ctx:cParser.Assignment2Context):
        node = self.create_node("assignment2", "assignment2", self.currentNode, ctx)
        # identifier = self.create_node(str(ctx.IDENTIFIER()), node, ctx)
        # node.children.append(identifier)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

        node = self.create_node(str(ctx.IDENTIFIER()), "var", self.currentNode, ctx)

        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        self.currentNode = self.currentNode.parent

    def enterDefinition(self, ctx:cParser.DefinitionContext):
        node = self.create_node("definition", "definition", self.currentNode, ctx)
        # identifier = self.create_node(str(ctx.IDENTIFIER()), node, ctx)
        # node.children.append(identifier)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def enterPointer_type(self, ctx:cParser.Pointer_typeContext):
        string = "pointer"
        symbol_type = ""
        if ctx.CHAR_TYPE():
            string = str(ctx.CHAR_TYPE())
            symbol_type = "char"
        if ctx.FLOAT_TYPE():
            string = str(ctx.FLOAT_TYPE())
            symbol_type = "float"
        if ctx.INT_TYPE():
            string = str(ctx.INT_TYPE())
            symbol_type = "int"
        for i in range(len(ctx.MAAL())):
            string += '*'
            symbol_type += '*'
        node = self.create_node(string, "pointer_type", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        self.currentNode.symbol_type = symbol_type

    def enterVar_type(self, ctx:cParser.Var_typeContext):
        string = "pointer"
        symbol_type = "pointer"
        if ctx.CHAR_TYPE():
            string = str(ctx.CHAR_TYPE())
            symbol_type = "char"
        if ctx.FLOAT_TYPE():
            string = str(ctx.FLOAT_TYPE())
            symbol_type = "float"
        if ctx.INT_TYPE():
            string = str(ctx.INT_TYPE())
            symbol_type = "int"

        node = self.create_node(string, "var_type", self.currentNode, ctx)
        self.currentNode.children.insert(0, node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        self.currentNode.symbol_type = symbol_type

    def exitAssignment2(self, ctx:cParser.AssignmentContext):
        self.currentNode = self.currentNode.parent

    def exitAssignment(self, ctx:cParser.AssignmentContext):

        var = self.currentNode.children[0]
        while var.label in ['ass', 'Increment_var', 'Increment_op', 'increment']:
            var = var.children[0]
        var_type = self.symbol_table.get_symbol(var.label, ctx.start)
        if var_type.const:
            raise ConstAssignment("[Error] Line {}, Position {}: variable {} is declared const"
                                  .format(ctx.start.line, ctx.start.column, var))
        self.currentNode = self.currentNode.parent

    def exitDefinition(self, ctx:cParser.DefinitionContext):
        if ctx.CONST():
            node = self.create_node("const", "const", self.currentNode, ctx)
            self.currentNode.children.insert(0, node)
            for i in range(2, len(self.currentNode.children)):
                node = self.currentNode.children[i]
                symbol = node.label
                assigned = node.node_type == 'assignment2'
                if assigned:
                    symbol = node.children[0].label
                self.symbol_table.add_symbol(symbol, self.currentNode.children[1].label, ctx.start, assigned, True)
        else:
            for i in range(1, len(self.currentNode.children)):
                node = self.currentNode.children[i]
                symbol = node.label
                assigned = node.node_type == 'assignment2'
                if assigned:
                    symbol = node.children[0].label
                self.symbol_table.add_symbol(symbol, self.currentNode.children[0].label, ctx.start, assigned, False)

        self.currentNode = self.currentNode.parent

    def exitPointer_type(self, ctx:cParser.Pointer_typeContext):
        self.currentNode = self.currentNode.parent

    def exitVar_type(self, ctx:cParser.Var_typeContext):
        if self.currentNode.label == 'pointer':
            self.currentNode.children[0].parent = self.currentNode.parent
            self.currentNode.parent.children[0] = self.currentNode.children[0]
        temp = self.currentNode
        self.currentNode = self.currentNode.parent
        del temp


    # Expressions ----
    def enterBool1(self, ctx:cParser.Bool1Context):
        node = self.create_node("bool1", "bool1", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitBool1(self, ctx:cParser.Bool1Context):
        self.currentNode = self.currentNode.parent

    def enterBool2(self, ctx:cParser.Bool2Context):
        # (EQ | LT | LE | GT | GE | NE)
        string = "bool2"
        if ctx.EQ():
            string = str(ctx.EQ())
        elif ctx.LT():
            string = str(ctx.LT())
        elif ctx.LE():
            string = str(ctx.LE())
        elif ctx.GT():
            string = str(ctx.GT())
        elif ctx.GE():
            string = str(ctx.GE())
        elif ctx.NE():
            string = str(ctx.NE())

        node = self.create_node(string, "bool2", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitBool2(self, ctx:cParser.Bool2Context):
        self.currentNode = self.currentNode.parent

    def enterPlus(self, ctx:cParser.PlusContext):
        node = self.create_node("plus", "plus", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def enterNot_value(self, ctx: cParser.Not_valueContext):
        node = self.create_node(str(ctx.NOT()), "not_value", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitNot_value(self, ctx: cParser.Not_valueContext):
        self.currentNode = self.currentNode.parent

    def exitPlus(self, ctx:cParser.PlusContext):
        self.currentNode = self.currentNode.parent

    def enterVm(self, ctx:cParser.VmContext):
        node = self.create_node("vm", "vm", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitVm(self, ctx:cParser.VmContext):
        self.currentNode = self.currentNode.parent

    def enterMod(self, ctx:cParser.ModContext):
        node = self.create_node("%", "mod", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitMod(self, ctx:cParser.ModContext):
        self.currentNode = self.currentNode.parent

    def enterNeg_sol(self, ctx:cParser.Neg_solContext):
        node = self.create_node("negsol", "negsol", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitNeg_sol(self, ctx:cParser.Neg_solContext):
        self.currentNode = self.currentNode.parent

    def enterVm_sol(self, ctx:cParser.Vm_solContext):
        node = self.create_node("vmsol", "vmsol", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitVm_sol(self, ctx:cParser.Vm_solContext):
        self.currentNode = self.currentNode.parent

    def enterValue(self, ctx:cParser.ValueContext):
        node = self.create_node("value", "value", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitValue(self, ctx:cParser.ValueContext):
        self.currentNode = self.currentNode.parent

    # def enterNeg_value(self, ctx:cParser.Neg_valueContext):
    #     node = self.create_node(str(ctx.NEG_INT()), "neg_value", self.currentNode, ctx)
    #     self.currentNode.children.append(node)
    #     self.currentNode = node
    #     self.currentNode.symbol_table = self.symbol_table.get_current_scope()
    #
    # def exitNeg_value(self, ctx:cParser.Neg_valueContext):
    #     self.currentNode = self.currentNode.parent

    def enterOperator(self, ctx:cParser.OperatorContext):
        string = ""
        if ctx.MAAL():
            string = str(ctx.MAAL())
        else:
            string = str(ctx.DEEL())
        node = self.create_node(string, string, self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitOperator(self, ctx:cParser.OperatorContext):
        self.currentNode = self.currentNode.parent

    def enterOperator2(self, ctx:cParser.Operator2Context):
        string = ""
        if ctx.PLUS():
            string = str(ctx.PLUS())
        else:
            string = str(ctx.MIN())
        node = self.create_node(string, string, self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitOperator2(self, ctx:cParser.Operator2Context):
        self.currentNode = self.currentNode.parent

    def enterBoolop(self, ctx:cParser.BoolopContext):
        string = ""
        if ctx.AND():
            string = str(ctx.AND())
        else:
            string = str(ctx.OR())
        node = self.create_node(string, "boolop", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitBoolop(self, ctx:cParser.BoolopContext):
        self.currentNode = self.currentNode.parent

    def enterVariable_identifier(self, ctx: cParser.Variable_identifierContext):
        node = self.create_node(str(ctx.IDENTIFIER()), "var", self.currentNode, ctx)

        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitVariable_identifier(self, ctx:cParser.Variable_identifierContext):
        self.currentNode = self.currentNode.parent

    def enterMethod_call(self, ctx:cParser.Method_callContext):
        node = self.create_node("method_call", "method_call", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        id = self.create_node(str(ctx.IDENTIFIER()), "method_call_id", self.currentNode, ctx)
        self.currentNode.children.append(id)
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitMethod_call(self, ctx:cParser.Method_callContext):
        self.currentNode.children.append(self.create_node("empty arg", "arg", self.currentNode, ctx))
        self.currentNode = self.currentNode.parent

    def enterMethod_definition(self, ctx:cParser.Method_definitionContext):
        node = self.create_node("method_definition", "method_definition", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        id = self.create_node(str(ctx.IDENTIFIER()), "method_call_id", self.currentNode, ctx)
        self.currentNode.children.append(id)
        self.symbol_table.open_scope()
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitMethod_definition(self, ctx:cParser.Method_definitionContext):
        self.symbol_table.close_scope()
        # const = False
        # if ctx.CONST():
        #     const = True
        if ctx.VOID():
            node = self.create_node('void', 'var_type', self.currentNode, ctx)
            self.currentNode.children.insert(0, node)

        args = []
        if len(self.currentNode.children) == 4:

            for arg in self.currentNode.children[2].children:
                args.append(arg.children[0].label)

        self.symbol_table.add_method(str(ctx.IDENTIFIER()), self.currentNode.children[0].label, ctx.start, args, True)

        self.currentNode = self.currentNode.parent

    def enterDef_args(self, ctx:cParser.Def_argsContext):
        node = self.create_node("def_args", "def_args", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitDef_args(self, ctx:cParser.Def_argsContext):
        self.currentNode = self.currentNode.parent

    def enterArg_definition(self, ctx:cParser.Arg_definitionContext):
        node = self.create_node("Arg_definition", "Arg_definition", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node

        id = self.create_node(str(ctx.IDENTIFIER()), "Arg_definition_id", self.currentNode, ctx)
        self.currentNode.children.append(id)
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitArg_definition(self, ctx:cParser.Arg_definitionContext):
        indentifier = str(ctx.IDENTIFIER())
        const = False
        if ctx.CONST():
            const = True

        self.symbol_table.add_symbol(indentifier, self.currentNode.children[0].label, ctx, True, const)

        self.currentNode = self.currentNode.parent

    def enterMethod_declaration(self, ctx:cParser.Method_declarationContext):
        node = self.create_node("method_declaration", "method_declaration", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        id = self.create_node(str(ctx.IDENTIFIER()), "method_call_id", self.currentNode, ctx)
        self.currentNode.children.append(id)
        self.symbol_table.open_scope()
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitMethod_declaration(self, ctx:cParser.Method_declarationContext):
        self.symbol_table.close_scope()
        const = False
        if ctx.CONST():
            const = True

        if ctx.VOID():
            node = self.create_node('void', 'var_type', self.currentNode, ctx)
            self.currentNode.children.insert(0, node)

        args = []
        if len(self.currentNode.children) == 4:

            for arg in self.currentNode.children[3]:
                args.append(arg.children[0].label)

        self.symbol_table.add_method(str(ctx.IDENTIFIER()), self.currentNode.children[0], ctx.start, args, False)
        self.currentNode = self.currentNode.parent

    def enterReturn_line(self, ctx:cParser.Return_lineContext):
        node = self.create_node("return", "return", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitReturn_line(self, ctx:cParser.Return_lineContext):
        self.currentNode = self.currentNode.parent

    def enterArgs(self, ctx:cParser.ArgsContext):
        node = self.create_node("args", "args", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitArgs(self, ctx:cParser.ArgsContext):
        self.currentNode = self.currentNode.parent

    def enterIncrement(self, ctx:cParser.IncrementContext):
        node = self.create_node("increment", "increment", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitIncrement(self, ctx:cParser.IncrementContext):
        self.currentNode = self.currentNode.parent

    def enterIncrement_op_first(self, ctx:cParser.Increment_op_firstContext):
        node = self.create_node("Increment_op", "Increment_op", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        string = '--'
        if ctx.PLUSPLUS():
            string = '++'

        node2 = self.create_node(string, "increment", self.currentNode, ctx)
        node1 = self.create_node(str(ctx.IDENTIFIER()), "var", self.currentNode, ctx)
        self.currentNode.children.append(node1)
        self.currentNode.children.append(node2)
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        node1.symbol_table = self.symbol_table.get_current_scope()
        node2.symbol_table = self.symbol_table.get_current_scope()
        node1.symbol_type = node1.symbol_table.get_symbol(str(ctx.IDENTIFIER()), ctx.start).symbol_type

    def exitIncrement_op_first(self, ctx:cParser.Increment_op_firstContext):
        self.currentNode = self.currentNode.parent

    def enterIncrement_var_first(self, ctx:cParser.Increment_var_firstContext):
        node = self.create_node("Increment_var", "Increment_var", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        string = '--'
        if ctx.PLUSPLUS():
            string = '++'

        node2 = self.create_node(string, "Increment_var", self.currentNode, ctx)
        node1 = self.create_node(str(ctx.IDENTIFIER()), "var", self.currentNode, ctx)
        self.currentNode.children.append(node1)
        self.currentNode.children.append(node2)
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        node1.symbol_table = self.symbol_table.get_current_scope()
        node2.symbol_table = self.symbol_table.get_current_scope()
        node1.symbol_type = node1.symbol_table.get_symbol(str(ctx.IDENTIFIER()), ctx.start).symbol_type

    def exitIncrement_var_first(self, ctx:cParser.Increment_var_firstContext):
        self.currentNode = self.currentNode.parent

    def enterUnary_min(self, ctx:cParser.Unary_minContext):
        node = self.create_node("unary min", "unary min", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        node_min = self.create_node('-', '-', self.currentNode, ctx)
        self.currentNode.children.append(node_min)

    def exitUnary_min(self, ctx:cParser.Unary_minContext):
        self.currentNode = self.currentNode.parent

    def enterUnary_plus(self, ctx:cParser.Unary_plusContext):
        node = self.create_node("unary plus", "unary plus", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        node_min = self.create_node('+', '+', self.currentNode, ctx)
        self.currentNode.children.append(node_min)

    def exitUnary_plus(self, ctx:cParser.Unary_plusContext):
        self.currentNode = self.currentNode.parent

    # LOOPS
    def enterFor_loop(self, ctx:cParser.For_loopContext):
        node = self.create_node("for", "for", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.symbol_table.open_scope()
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitFor_loop(self, ctx:cParser.For_loopContext):
        self.currentNode = self.currentNode.parent
        self.symbol_table.close_scope()

    def enterFor_initial(self, ctx:cParser.For_initialContext):
        node = self.create_node("for initial", "for initial", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitFor_initial(self, ctx:cParser.For_initialContext):
        self.currentNode = self.currentNode.parent

    def enterFor_update(self, ctx:cParser.For_updateContext):
        node = self.create_node("for update", "for update", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitFor_update(self, ctx:cParser.For_updateContext):
        self.currentNode = self.currentNode.parent

    def enterBreak_line(self, ctx:cParser.Break_lineContext):
        node = self.create_node("for break", "for break", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitBreak_line(self, ctx:cParser.Break_lineContext):
        self.currentNode = self.currentNode.parent

    def enterContinue_line(self, ctx:cParser.Continue_lineContext):
        node = self.create_node("for continue", "for continue", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitContinue_line(self, ctx:cParser.Continue_lineContext):
        self.currentNode = self.currentNode.parent

    def enterWhile_loop(self, ctx:cParser.While_loopContext):
        node = self.create_node("for", "for", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitWhile_loop(self, ctx:cParser.While_loopContext):
        self.currentNode = self.currentNode.parent

    def enterDo_block(self, ctx:cParser.Do_blockContext):
        node = self.create_node("for do", "for do", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitDo_block(self, ctx:cParser.Do_blockContext):
        self.currentNode = self.currentNode.parent

    # IF ELSE
    def enterCondition(self, ctx:cParser.ConditionContext):
        """
        Ook gebruikt voor loops
        :param ctx:
        :return: nothing
        """
        node = self.create_node("condition", "condition", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitCondition(self, ctx:cParser.ConditionContext):
        self.currentNode = self.currentNode.parent

    def enterIfelse(self, ctx:cParser.IfelseContext):
        node = self.create_node("ifelse", "ifelse", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitIfelse(self, ctx:cParser.IfelseContext):
        self.currentNode = self.currentNode.parent


    def enterSwitchcase(self, ctx:cParser.SwitchcaseContext):
        node = self.create_node("switch", "switch", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.symbol_table.open_scope()
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()


    def exitSwitchcase(self, ctx:cParser.SwitchcaseContext):
        self.currentNode = self.currentNode.parent
        self.symbol_table.close_scope()

    def enterCase(self, ctx:cParser.CaseContext):
        string = ""
        if ctx.CHAR():
            string = str(ctx.CHAR())
            symbol_type = "char"

        if ctx.INT():
            string = str(ctx.INT())
            symbol_type = "int"
        node = self.create_node(string, "case", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()
        self.currentNode.symbol_type = symbol_type

    def exitCase(self, ctx:cParser.CaseContext):
        self.currentNode = self.currentNode.parent

    def enterDefault(self, ctx:cParser.DefaultContext):
        node = self.create_node("default", "default case", self.currentNode, ctx)
        self.currentNode.children.append(node)
        self.currentNode = node
        self.currentNode.symbol_table = self.symbol_table.get_current_scope()

    def exitDefault(self, ctx:cParser.DefaultContext):
        self.currentNode = self.currentNode.parent
