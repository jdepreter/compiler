

class CSyntaxError(Exception):
    pass


class UndeclaredVariable(Exception):
    pass


class UninitializedVariable(Exception):
    pass


class DuplicateDeclaration(Exception):
    pass


class IncompatibleType(Exception):
    pass


class ConstAssignment(Exception):
    pass


class BreakError(Exception):
    pass
