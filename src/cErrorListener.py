from antlr4.error.ErrorListener import ErrorListener
from src.CustomExceptions import CSyntaxError


class CErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise CSyntaxError("[Syntax Error] Line {} Position {}: {}".format(line, column, msg))
