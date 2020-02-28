# Generated from ./ANTLR/LLVM/grammer1.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3+\n\3\3\4\3\4\3\4\3\4\5\4\61\n\4\3\5\3\5\3\5")
        buf.write("\5\5\66\n\5\3\5\3\5\7\5:\n\5\f\5\16\5=\13\5\5\5?\n\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\7\6F\n\6\f\6\16\6I\13\6\5\6K\n\6\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3")
        buf.write("\r\3\16\3\16\3\17\6\17^\n\17\r\17\16\17_\3\17\3\17\2\2")
        buf.write("\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\3\2\6\4\2>>@@\3\2\63;\3\2\62;\5\2\13")
        buf.write("\f\17\17\"\"\2m\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5*\3\2\2")
        buf.write("\2\7\60\3\2\2\2\t\62\3\2\2\2\13J\3\2\2\2\rL\3\2\2\2\17")
        buf.write("N\3\2\2\2\21P\3\2\2\2\23R\3\2\2\2\25T\3\2\2\2\27V\3\2")
        buf.write("\2\2\31X\3\2\2\2\33Z\3\2\2\2\35]\3\2\2\2\37 \7#\2\2 \4")
        buf.write("\3\2\2\2!\"\7?\2\2\"+\7?\2\2#+\t\2\2\2$%\7@\2\2%+\7?\2")
        buf.write("\2&\'\7>\2\2\'+\7?\2\2()\7#\2\2)+\7?\2\2*!\3\2\2\2*#\3")
        buf.write("\2\2\2*$\3\2\2\2*&\3\2\2\2*(\3\2\2\2+\6\3\2\2\2,-\7(\2")
        buf.write("\2-\61\7(\2\2./\7~\2\2/\61\7~\2\2\60,\3\2\2\2\60.\3\2")
        buf.write("\2\2\61\b\3\2\2\2\62>\5\31\r\2\63?\7\62\2\2\64\66\7/\2")
        buf.write("\2\65\64\3\2\2\2\65\66\3\2\2\2\66\67\3\2\2\2\67;\t\3\2")
        buf.write("\28:\t\4\2\298\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<")
        buf.write("?\3\2\2\2=;\3\2\2\2>\63\3\2\2\2>\65\3\2\2\2?@\3\2\2\2")
        buf.write("@A\5\33\16\2A\n\3\2\2\2BK\7\62\2\2CG\t\3\2\2DF\t\4\2\2")
        buf.write("ED\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2HK\3\2\2\2IG\3")
        buf.write("\2\2\2JB\3\2\2\2JC\3\2\2\2K\f\3\2\2\2LM\7-\2\2M\16\3\2")
        buf.write("\2\2NO\7/\2\2O\20\3\2\2\2PQ\7,\2\2Q\22\3\2\2\2RS\7\61")
        buf.write("\2\2S\24\3\2\2\2TU\7\'\2\2U\26\3\2\2\2VW\7=\2\2W\30\3")
        buf.write("\2\2\2XY\7*\2\2Y\32\3\2\2\2Z[\7+\2\2[\34\3\2\2\2\\^\t")
        buf.write("\5\2\2]\\\3\2\2\2^_\3\2\2\2_]\3\2\2\2_`\3\2\2\2`a\3\2")
        buf.write("\2\2ab\b\17\2\2b\36\3\2\2\2\13\2*\60\65;>GJ_\3\b\2\2")
        return buf.getvalue()


class grammer1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    BINOP2 = 2
    BINOP = 3
    NEG_INT = 4
    INT = 5
    PLUS = 6
    MIN = 7
    MAAL = 8
    DEEL = 9
    MOD = 10
    SEMICOLON = 11
    LBRACKET = 12
    RBRACKET = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'!'", "'+'", "'-'", "'*'", "'/'", "'%'", "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "BINOP2", "BINOP", "NEG_INT", "INT", "PLUS", "MIN", "MAAL", 
            "DEEL", "MOD", "SEMICOLON", "LBRACKET", "RBRACKET", "WS" ]

    ruleNames = [ "T__0", "BINOP2", "BINOP", "NEG_INT", "INT", "PLUS", "MIN", 
                  "MAAL", "DEEL", "MOD", "SEMICOLON", "LBRACKET", "RBRACKET", 
                  "WS" ]

    grammarFileName = "grammer1.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


