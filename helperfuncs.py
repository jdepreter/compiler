
def get_return_type(type1, type2):
    if type1 == "float" or type2 == "float":
        return 'float'
    elif type1 == "int" or type2 == "int":
        return 'int'
    elif type1 == "char" or type2 == "char":
        return 'char'
    else:
        raise Exception('false types')
