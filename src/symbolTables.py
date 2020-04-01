from src.CustomExceptions import UndeclaredVariable, UninitializedVariable, DuplicateDeclaration
import re


class MethodType:
    def __init__(self, symbol_type, arguments, const, name, current_register, defined=True):
        self.symbol_type = symbol_type
        self.arguments = arguments
        self.const = const
        self.name = name
        self.internal_name = name + '_' + str(current_register)
        self.current_register = current_register
        self.defined = defined


class SymbolType:
    def __init__(self, symbol_type, assigned, const, current_register):
        self.symbol_type = symbol_type
        self.assigned = assigned
        self.const = const
        self.current_register = current_register
        self.used = False

    def set_reg(self, current_register):
        self.current_register = current_register


class SymbolTable:
    def __init__(self):
        self.main_defined = False
        self.table_stack = []
        self.table_list = []
        self.current_register = 0

        self.method_register = 4

        outer_method_scope = dict()
        # printf_int = MethodType('void', ['int'], False, 'printf', 0)
        # printf_int.internal_name = 'print_int'
        #
        # printf_char = MethodType('void', ['char'], False, 'printf', 1)
        # printf_char.internal_name = 'print_char'
        #
        # printf_float = MethodType('void', ['float'], False, 'printf', 2)
        # printf_float.internal_name = 'printf_float'
        #
        # main = MethodType('int', [], False, 'main', 3)
        # main.internal_name = 'main'

        outer_method_scope['printf_int'] = MethodType('void', ['int'], False, 'printf', 0)
        outer_method_scope['printf_int'].internal_name = 'print_int'
        outer_method_scope['printf_char'] = MethodType('void', ['char'], False, 'printf', 1)
        outer_method_scope['printf_char'].internal_name = 'print_char'
        outer_method_scope['printf_float'] = MethodType('void', ['float'], False, 'printf', 2)
        outer_method_scope['printf_float'].internal_name = 'print_float'
        #
        outer_method_scope['main'] = MethodType('int', [], False, 'main', 3)
        outer_method_scope['main'].internal_name = 'main'
        # outer_method_scope['printf'] = [printf_int, printf_char, printf_float]
        # outer_method_scope['main'] = [main]

        self.method_stack = [outer_method_scope]
        self.method_list = [outer_method_scope]

    def warn_unused(self):
        for table in self.table_list:
            for key in table:
                if not table[key].used:
                    warn = "Warning: {} is unused".format(key)
                    print(warn)

    def open_scope(self):
        newdict = dict()
        self.table_stack.insert(0, newdict)
        self.table_list.append(newdict)
        method_dict = dict()
        self.method_stack.insert(0, method_dict)
        self.method_list.append(method_dict)

    def close_scope(self):
        self.table_stack.pop(0)
        self.method_stack.pop(0)

    def add_symbol(self, symbol, symbol_type, error, assinged=True, const=False):
        if symbol in self.table_stack[0]:
            raise DuplicateDeclaration("[Error] Line {}, Position {}: Duplicate declaration of variable {} "
                                       .format(error.line, error.column, symbol))
        self.table_stack[0][symbol] = SymbolType(symbol_type, assinged, const, self.current_register)
        self.current_register += 1

    def get_assigned_symbol(self, symbol_name, error):
        symbol = self.get_symbol(symbol_name, error)
        if not symbol.assigned:
            raise UninitializedVariable("[Error] Line {}, Position {}: variable {} is not initialised"
                                        .format(error.line, error.column, symbol_name))

        return symbol

    def get_symbol(self, symbol, error):
        symbol = re.sub(r'\*', '', symbol)
        for scope in self.table_stack:
            if symbol in scope:
                scope[symbol].used = True
                return scope[symbol]

        raise UndeclaredVariable("[Error] Line {}, Position {}: variable {} is undeclared"
                                 .format(error.line, error.column, symbol))

    def generate_key(self, method, arg_types):
        key = method
        for arg_type in arg_types:
            key += '_' + arg_type
        return key

    def add_method(self, method, method_type, error, args, defined=True):
        if method == "main":
            if self.main_defined:
                raise Exception("multiple definitions of main")
            self.main_defined = True
            return

        if method in self.method_stack[0]:
            if self.method_stack[0][method].defined:
                raise DuplicateDeclaration("[Error] Line {}, Position {}: Duplicate declaration of method {} "
                                           .format(error.line, error.column, method))
            else:
                if args != self.method_stack[0][method].arguments:
                    raise Exception("[Error] Line {}: Conflicting types for {} "
                                    .format(error.line, method))
        self.method_stack[0][method] = MethodType(method_type, args, False, method, self.method_register, defined)
        self.method_register += 1

    def get_method(self, method, arg_types, error):
        # key = self.generate_key(method, arg_types)
        if method == 'printf':
            try:
                return self.method_stack[-1]["printf_{}".format(arg_types[0])]
            except:
                raise UndeclaredVariable("[Error] Line {}, Position {}: method {}({}) is undeclared"
                                         .format(error.line, error.column, method, ','.join(arg_types)))

        for scope in self.method_stack:
            if method in scope:
                return scope[method]

        raise UndeclaredVariable("[Error] Line {}, Position {}: method {}({}) is undeclared"
                                 .format(error.line, error.column, method, ','.join(arg_types)))

    def get_current_scope(self):
        s = SymbolTable()
        s.table_stack = list(self.table_stack)
        s.method_stack = list(self.method_stack)
        s.table_list = self.table_list
        s.method_list = self.method_list
        return s
