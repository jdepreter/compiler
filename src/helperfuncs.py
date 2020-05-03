import struct
from src.CustomExceptions import *


def raise_error(message: str, line: int, position: int):
    raise Exception("[Error] Line {}, Postition {}: {}".format(line, position, message))


def print_warning(message: str, line: int, position: int):
    print("[Warning] Line {}, Position {}: {}", line, position, message)


def get_return_type(type1, type2):
    if '*' in type1 or '*' in type2 or '&' in type1 or '&' in type2:
        raise Exception('pointer type cannot be operated on')
    if type1 == "float" or type2 == "float":
        return 'float'
    elif type1 == "int" or type2 == "int":
        return 'int'
    elif type1 == "char" or type2 == "char":
        return 'char'
    else:
        raise Exception('nonexistent  types')


def double_to_hex(f):
    hex_string = hex(struct.unpack('<Q', struct.pack('<d', f))[0])
    hex_string = hex_string[:11]
    hex_string += "0000000"
    return hex_string


def get_type_and_stars(input_type):

    stars = input_type.count('*')
    if stars == 0:
        symbol_type = input_type
    else:
        symbol_type = input_type[:-stars]

    if '&' == symbol_type[0]:
        symbol_type = symbol_type[1:]
        return symbol_type, input_type[len(input_type) - stars:]+'*'
    else:
        return symbol_type, input_type[len(input_type) - stars:]


def allowed_operation(symbol_type1, symbol_type2, operation, ctx):
    if ('*' in symbol_type1 or '&' in symbol_type1) and ('*' in symbol_type2 or '&' in symbol_type2):
        raise IncompatibleType("[Error] Line {} Position {}: Incompatible Operation {} {} {}".format(
            ctx.line, ctx.column,
            symbol_type1, operation, symbol_type2
        ))

    if ('*' in symbol_type1 or '&' in symbol_type1) or ('*' in symbol_type2 or '&' in symbol_type2):
        if operation not in ['+', '-']:
            raise IncompatibleType("[Error] Line {} Position {}: Incompatible Operation {} {} {}".format(
                ctx.line, ctx.column,
                symbol_type1, operation, symbol_type2
            ))

    if (symbol_type1=="float" or symbol_type2 == "float") and operation == "%":
        raise IncompatibleType("[Error] Line {} Position {}: Incompatible Operation {} {} {}".format(
            ctx.line, ctx.column,
            symbol_type1, operation, symbol_type2
        ))
