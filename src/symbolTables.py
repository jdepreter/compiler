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
        self.written = False


class SymbolType:
    def __init__(self, name, symbol_type, assigned, const, current_register, _global=False, array_size_node=None):
        self.name = name
        self.symbol_type = symbol_type
        self.assigned = assigned
        self.const = const
        self.used = False
        self.is_global = _global
        self.array_size_node = array_size_node
        self.size = array_size_node is not None
        self.written = False

        # LLVM
        self.reg = current_register
        if _global:
            self.current_register = '@x_' + str(current_register)
        else:
            self.current_register = '%a' + str(current_register)

        # MIPS
        self.offset = 0

    def set_reg(self, current_register):
        self.current_register = current_register

    def is_array(self):
        return self.size > 0


class SymbolTable:
    main_defined = False
    def __init__(self):

        self.table_stack = []
        self.table_list = []
        self.var_counter = 0

        self.method_register = 0

        self.strings = dict()
        self.mips_strings = dict()
        self.restrings = dict()
        self.strings_nr = 0

        # outer_method_scope = dict()
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

        # outer_method_scope['printf_int'] = MethodType('void', ['int'], False, 'printf', 0)
        # outer_method_scope['printf_int'].internal_name = 'print_int'
        # outer_method_scope['printf_char'] = MethodType('void', ['char'], False, 'printf', 1)
        # outer_method_scope['printf_char'].internal_name = 'print_char'
        # outer_method_scope['printf_float'] = MethodType('void', ['float'], False, 'printf', 2)
        # outer_method_scope['printf_float'].internal_name = 'print_float'

        # #
        # outer_method_scope['main'] = MethodType('int', [], False, 'main', 3)
        # outer_method_scope['main'].internal_name = 'main'
        # outer_method_scope['printf'] = [printf_int, printf_char, printf_float]
        # outer_method_scope['main'] = [main]

        self.method_stack = []
        self.method_list = []
        self.printf = None

    def warn_unused(self):
        for table in self.table_list:
            for key in table:
                if not table[key].used:
                    warn = "Warning: {} is unused".format(key)
                    print(warn)

    def no_main(self):

        if not SymbolTable.main_defined:
            raise Exception("function main is not defined")

    def include_stdio(self):
        self.method_stack[0]["printf"] = MethodType('int', ['char*', ...], False, 'printf', 0)
        self.method_stack[0]["printf"] = MethodType('int', ['char*'], False, 'printf', 0)
        self.printf = MethodType('int', ['char*'], False, 'printf', 0)

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

    def add_symbol(self, symbol, symbol_type, error, assinged=True, const=False, array_size_node=None):
        if symbol in self.table_stack[0]:
            raise DuplicateDeclaration("[Error] Line {}, Position {}: Duplicate declaration of variable {} "
                                       .format(error.line, error.column, symbol))
        _global = len(self.table_stack) == 1
        assinged = assinged or _global
        self.table_stack[0][symbol] = SymbolType(symbol, symbol_type, assinged, const, self.var_counter, _global)
        self.var_counter += 1

    def get_assigned_symbol(self, symbol_name, error) -> SymbolType:
        symbol_name = re.sub(r'\*', '', symbol_name)
        symbol_name = re.sub(r'\[]', '', symbol_name)
        symbol = self.get_written_symbol(symbol_name, error)
        if not (symbol.assigned and symbol.written):
            raise UninitializedVariable("[Error] Line {}, Position {}: variable {} is not initialised"
                                        .format(error.line, error.column, symbol_name))

        return symbol

    def get_written_symbol(self, symbol_name, error) -> SymbolType:
        symbol_name = re.sub(r'\*', '', symbol_name)
        symbol_name = re.sub(r'\[]', '', symbol_name)
        for scope in self.table_stack:
            if symbol_name in scope and scope[symbol_name].written:
                scope[symbol_name].used = True
                return scope[symbol_name]

        raise UndeclaredVariable("[Error] Line {}, Position {}: variable {} is undeclared"
                                 .format(error.line, error.column, symbol_name))

    def get_symbol(self, symbol, error) -> SymbolType:
        symbol = re.sub(r'\*', '', symbol)
        symbol = re.sub(r'\[]', '', symbol)
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
        if len(self.method_stack) != 1:
            if defined:
                raise Exception('[Error] Line {}, Position {}: function definition is not allowed here'.format(
                    error.line, error.column
                ))
            else:
                raise Exception('[Error] Line {}, Position {}: function declaration is not allowed here'.format(
                    error.line, error.column
                ))

        if method in self.method_stack[0]:
            if self.method_stack[0][method].defined and defined:
                raise DuplicateDeclaration("[Error] Line {}, Position {}: Duplicate definition of method {} "
                                           .format(error.line, error.column, method))
            else:
                if args != self.method_stack[0][method].arguments or method_type != self.method_stack[0][method].symbol_type:
                    raise Exception("[Error] Line {}: Conflicting types for {} "
                                    .format(error.line, method))
                self.method_stack[0][method].defined = self.method_stack[0][method].defined or defined

        else:
            self.method_stack[0][method] = MethodType(method_type, args, False, method, self.method_register, defined)
            if method == "main" and len(self.method_stack) == 1:
                self.method_stack[0]["main"].internal_name = "main"
                SymbolTable.main_defined = True
            self.method_register += 1

    def get_method(self, method, arg_types, error) -> MethodType:
        # key = self.generate_key(method, arg_types)
        if method == 'printf':
            try:
                if (arg_types[0] == 'char*'):
                    return self.printf
                return self.method_stack[-1]["printf_{}".format(arg_types[0])]
            except:
                raise UndeclaredVariable("[Error] Line {}, Position {}: method {}({}) is undeclared"
                                         .format(error.line, error.column, method, ','.join(arg_types)))

        for scope in self.method_stack:
            if method in scope:
                return scope[method]

        raise UndeclaredVariable("[Error] Line {}, Position {}: method {}({}) is undeclared"
                                 .format(error.line, error.column, method, ','.join(arg_types)))

    def get_written_method(self, method, arg_types, error) -> MethodType:
        # key = self.generate_key(method, arg_types)
        if method == 'printf':
            try:
                if (arg_types[0] == 'char*'):
                    return self.printf

                return self.method_stack[-1]["printf_{}".format(arg_types[0])]
            except:
                raise UndeclaredVariable("[Error] Line {}, Position {}: method {}({}) is undeclared"
                                         .format(error.line, error.column, method, ','.join(arg_types)))

        for scope in self.method_stack:
            if method in scope:
                if scope[method].written:
                    return scope[method]
                else:
                    raise UndeclaredVariable("[Error] Line {}, Position {}: method {}({}) is undeclared"
                                             .format(error.line, error.column, method, ','.join(arg_types)))

        raise UndeclaredVariable("[Error] Line {}, Position {}: function {}({}) is undeclared"
                                 .format(error.line, error.column, method, ','.join(arg_types)))

    def add_string(self, string):
        if string not in self.strings:
            val = '@.str.{}'.format(str(self.strings_nr))
            self.strings[string] = val
            self.restrings[val] = string

    def add_mips_string(self, string):
        if string not in self.mips_strings:
            # TODO delete this
            mips_val = "str.{}".format(str(self.strings_nr))
            self.mips_strings[string] = mips_val
            self.strings_nr += 1

            # %d, %c, %s, %f should be split for MIPS

        strings = re.split("%.", string)
        for my_string in strings:
            if my_string not in self.mips_strings:
                mips_val = "str.{}".format(str(self.strings_nr))
                self.mips_strings[my_string] = mips_val
                self.strings_nr += 1

    def get_strings(self):
        return self.strings

    # MIPS
    def get_mips_strings(self):
        return self.mips_strings

    def increase_offset(self, amount):
        for scope in self.table_stack:
            for key, val in scope.items():
                if val.written:
                    val.offset += amount

    def decrease_offset(self, amount):
        for scope in self.table_stack:
            for key, val in scope.items():
                if val.written:
                    val.offset -= amount

    def get_current_scope(self):
        s = SymbolTable()
        s.table_stack = list(self.table_stack)
        s.method_stack = list(self.method_stack)
        s.table_list = self.table_list
        s.method_list = self.method_list
        s.printf = self.printf
        s.strings = self.strings
        s.restrings = self.restrings
        s.mips_strings = self.mips_strings
        return s
