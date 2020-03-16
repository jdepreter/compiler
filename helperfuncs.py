import struct


def get_return_type(type1, type2):
    if type1 == "float" or type2 == "float":
        return 'float'
    elif type1 == "int" or type2 == "int":
        return 'int'
    elif type1 == "char" or type2 == "char":
        return 'char'
    else:
        raise Exception('false types')


def double_to_hex(f):
    hex_string = hex(struct.unpack('<Q', struct.pack('<d', f))[0])
    hex_string = hex_string[:11]
    hex_string += "0000000"
    return hex_string


def get_type_and_stars(type):
    stars = type.count('*')
    if stars == 0:
        symbol_type = type
    else:
        symbol_type = type[:-stars]
    return symbol_type, type[len(type)-stars:]