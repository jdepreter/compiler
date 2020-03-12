from antlr4.error.ErrorListener import ErrorListener


class CErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("[Syntax Error] Line {} Position {}: {}".format(line, column, msg))
