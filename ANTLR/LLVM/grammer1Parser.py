# Generated from ./ANTLR/LLVM/grammer1.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("x\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\6\2\33")
        buf.write("\n\2\r\2\16\2\34\3\2\3\2\6\2!\n\2\r\2\16\2\"\7\2%\n\2")
        buf.write("\f\2\16\2(\13\2\3\3\3\3\3\4\3\4\3\4\7\4/\n\4\f\4\16\4")
        buf.write("\62\13\4\3\5\5\5\65\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\5\5@\n\5\3\6\3\6\5\6D\n\6\3\6\3\6\3\6\5\6I\n\6")
        buf.write("\7\6K\n\6\f\6\16\6N\13\6\3\7\3\7\3\7\3\7\5\7T\n\7\7\7")
        buf.write("V\n\7\f\7\16\7Y\13\7\3\b\3\b\3\b\3\b\5\b_\n\b\5\ba\n\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tk\n\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\5\nr\n\n\3\13\3\13\3\f\3\f\3\f\2\2\r\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\2\6\3\2\16\17\3\2\20\25\3\2\5\6\3")
        buf.write("\2\7\b\2|\2\30\3\2\2\2\4)\3\2\2\2\6+\3\2\2\2\b?\3\2\2")
        buf.write("\2\nC\3\2\2\2\fO\3\2\2\2\16Z\3\2\2\2\20j\3\2\2\2\22q\3")
        buf.write("\2\2\2\24s\3\2\2\2\26u\3\2\2\2\30\32\5\4\3\2\31\33\7\n")
        buf.write("\2\2\32\31\3\2\2\2\33\34\3\2\2\2\34\32\3\2\2\2\34\35\3")
        buf.write("\2\2\2\35&\3\2\2\2\36 \5\4\3\2\37!\7\n\2\2 \37\3\2\2\2")
        buf.write("!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#%\3\2\2\2$\36\3\2\2")
        buf.write("\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\3\3\2\2\2(&\3\2\2")
        buf.write("\2)*\5\6\4\2*\5\3\2\2\2+\60\5\b\5\2,-\t\2\2\2-/\5\b\5")
        buf.write("\2.,\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61")
        buf.write("\7\3\2\2\2\62\60\3\2\2\2\63\65\7\r\2\2\64\63\3\2\2\2\64")
        buf.write("\65\3\2\2\2\65\66\3\2\2\2\66\67\7\13\2\2\678\5\6\4\28")
        buf.write("9\7\f\2\29@\3\2\2\2:;\5\n\6\2;<\t\3\2\2<=\5\n\6\2=@\3")
        buf.write("\2\2\2>@\5\n\6\2?\64\3\2\2\2?:\3\2\2\2?>\3\2\2\2@\t\3")
        buf.write("\2\2\2AD\5\f\7\2BD\3\2\2\2CA\3\2\2\2CB\3\2\2\2DL\3\2\2")
        buf.write("\2EH\t\4\2\2FI\5\f\7\2GI\5\20\t\2HF\3\2\2\2HG\3\2\2\2")
        buf.write("IK\3\2\2\2JE\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\13")
        buf.write("\3\2\2\2NL\3\2\2\2OW\5\16\b\2PS\t\5\2\2QT\5\16\b\2RT\5")
        buf.write("\20\t\2SQ\3\2\2\2SR\3\2\2\2TV\3\2\2\2UP\3\2\2\2VY\3\2")
        buf.write("\2\2WU\3\2\2\2WX\3\2\2\2X\r\3\2\2\2YW\3\2\2\2Z`\5\22\n")
        buf.write("\2[^\7\t\2\2\\_\5\22\n\2]_\5\20\t\2^\\\3\2\2\2^]\3\2\2")
        buf.write("\2_a\3\2\2\2`[\3\2\2\2`a\3\2\2\2a\17\3\2\2\2bk\5\24\13")
        buf.write("\2cd\7\13\2\2de\7\6\2\2ef\7\13\2\2fg\5\n\6\2gh\7\f\2\2")
        buf.write("hi\7\f\2\2ik\3\2\2\2jb\3\2\2\2jc\3\2\2\2k\21\3\2\2\2l")
        buf.write("r\5\26\f\2mn\7\13\2\2no\5\n\6\2op\7\f\2\2pr\3\2\2\2ql")
        buf.write("\3\2\2\2qm\3\2\2\2r\23\3\2\2\2st\7\3\2\2t\25\3\2\2\2u")
        buf.write("v\7\4\2\2v\27\3\2\2\2\21\34\"&\60\64?CHLSW^`jq")
        return buf.getvalue()


class grammer1Parser ( Parser ):

    grammarFileName = "grammer1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "';'", "'('", "')'", "'!'", "'&&'", 
                     "'||'", "'=='", "'>'", "'<'", "'!='", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>", "NEG_INT", "INT", "PLUS", "MIN", "MAAL", 
                      "DEEL", "MOD", "SEMICOLON", "LBRACKET", "RBRACKET", 
                      "NOT", "AND", "OR", "EQ", "GT", "LT", "NE", "GE", 
                      "LE", "WS" ]

    RULE_gram = 0
    RULE_line = 1
    RULE_bool1 = 2
    RULE_bool2 = 3
    RULE_plus = 4
    RULE_vm = 5
    RULE_mod = 6
    RULE_neg_sol = 7
    RULE_vm_sol = 8
    RULE_neg_value = 9
    RULE_value = 10

    ruleNames =  [ "gram", "line", "bool1", "bool2", "plus", "vm", "mod", 
                   "neg_sol", "vm_sol", "neg_value", "value" ]

    EOF = Token.EOF
    NEG_INT=1
    INT=2
    PLUS=3
    MIN=4
    MAAL=5
    DEEL=6
    MOD=7
    SEMICOLON=8
    LBRACKET=9
    RBRACKET=10
    NOT=11
    AND=12
    OR=13
    EQ=14
    GT=15
    LT=16
    NE=17
    GE=18
    LE=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class GramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammer1Parser.LineContext)
            else:
                return self.getTypedRuleContext(grammer1Parser.LineContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(grammer1Parser.SEMICOLON)
            else:
                return self.getToken(grammer1Parser.SEMICOLON, i)

        def getRuleIndex(self):
            return grammer1Parser.RULE_gram

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGram" ):
                listener.enterGram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGram" ):
                listener.exitGram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGram" ):
                return visitor.visitGram(self)
            else:
                return visitor.visitChildren(self)




    def gram(self):

        localctx = grammer1Parser.GramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_gram)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.line()
            self.state = 24 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 23
                    self.match(grammer1Parser.SEMICOLON)

                else:
                    raise NoViableAltException(self)
                self.state = 26 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammer1Parser.INT) | (1 << grammer1Parser.PLUS) | (1 << grammer1Parser.MIN) | (1 << grammer1Parser.SEMICOLON) | (1 << grammer1Parser.LBRACKET) | (1 << grammer1Parser.NOT) | (1 << grammer1Parser.AND) | (1 << grammer1Parser.OR) | (1 << grammer1Parser.EQ) | (1 << grammer1Parser.GT) | (1 << grammer1Parser.LT) | (1 << grammer1Parser.NE) | (1 << grammer1Parser.GE) | (1 << grammer1Parser.LE))) != 0):
                self.state = 28
                self.line()
                self.state = 30 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 29
                        self.match(grammer1Parser.SEMICOLON)

                    else:
                        raise NoViableAltException(self)
                    self.state = 32 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bool1(self):
            return self.getTypedRuleContext(grammer1Parser.Bool1Context,0)


        def getRuleIndex(self):
            return grammer1Parser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = grammer1Parser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.bool1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bool2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammer1Parser.Bool2Context)
            else:
                return self.getTypedRuleContext(grammer1Parser.Bool2Context,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(grammer1Parser.AND)
            else:
                return self.getToken(grammer1Parser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(grammer1Parser.OR)
            else:
                return self.getToken(grammer1Parser.OR, i)

        def getRuleIndex(self):
            return grammer1Parser.RULE_bool1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool1" ):
                listener.enterBool1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool1" ):
                listener.exitBool1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool1" ):
                return visitor.visitBool1(self)
            else:
                return visitor.visitChildren(self)




    def bool1(self):

        localctx = grammer1Parser.Bool1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bool1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.bool2()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==grammer1Parser.AND or _la==grammer1Parser.OR:
                self.state = 42
                _la = self._input.LA(1)
                if not(_la==grammer1Parser.AND or _la==grammer1Parser.OR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 43
                self.bool2()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(grammer1Parser.LBRACKET, 0)

        def bool1(self):
            return self.getTypedRuleContext(grammer1Parser.Bool1Context,0)


        def RBRACKET(self):
            return self.getToken(grammer1Parser.RBRACKET, 0)

        def NOT(self):
            return self.getToken(grammer1Parser.NOT, 0)

        def plus(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammer1Parser.PlusContext)
            else:
                return self.getTypedRuleContext(grammer1Parser.PlusContext,i)


        def EQ(self):
            return self.getToken(grammer1Parser.EQ, 0)

        def LT(self):
            return self.getToken(grammer1Parser.LT, 0)

        def LE(self):
            return self.getToken(grammer1Parser.LE, 0)

        def GT(self):
            return self.getToken(grammer1Parser.GT, 0)

        def GE(self):
            return self.getToken(grammer1Parser.GE, 0)

        def NE(self):
            return self.getToken(grammer1Parser.NE, 0)

        def getRuleIndex(self):
            return grammer1Parser.RULE_bool2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool2" ):
                listener.enterBool2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool2" ):
                listener.exitBool2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool2" ):
                return visitor.visitBool2(self)
            else:
                return visitor.visitChildren(self)




    def bool2(self):

        localctx = grammer1Parser.Bool2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bool2)
        self._la = 0 # Token type
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==grammer1Parser.NOT:
                    self.state = 49
                    self.match(grammer1Parser.NOT)


                self.state = 52
                self.match(grammer1Parser.LBRACKET)
                self.state = 53
                self.bool1()
                self.state = 54
                self.match(grammer1Parser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.plus()
                self.state = 57
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammer1Parser.EQ) | (1 << grammer1Parser.GT) | (1 << grammer1Parser.LT) | (1 << grammer1Parser.NE) | (1 << grammer1Parser.GE) | (1 << grammer1Parser.LE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 58
                self.plus()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.plus()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlusContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammer1Parser.VmContext)
            else:
                return self.getTypedRuleContext(grammer1Parser.VmContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(grammer1Parser.PLUS)
            else:
                return self.getToken(grammer1Parser.PLUS, i)

        def MIN(self, i:int=None):
            if i is None:
                return self.getTokens(grammer1Parser.MIN)
            else:
                return self.getToken(grammer1Parser.MIN, i)

        def neg_sol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammer1Parser.Neg_solContext)
            else:
                return self.getTypedRuleContext(grammer1Parser.Neg_solContext,i)


        def getRuleIndex(self):
            return grammer1Parser.RULE_plus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlus" ):
                listener.enterPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlus" ):
                listener.exitPlus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlus" ):
                return visitor.visitPlus(self)
            else:
                return visitor.visitChildren(self)




    def plus(self):

        localctx = grammer1Parser.PlusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_plus)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammer1Parser.INT, grammer1Parser.LBRACKET]:
                self.state = 63
                self.vm()
                pass
            elif token in [grammer1Parser.PLUS, grammer1Parser.MIN, grammer1Parser.SEMICOLON, grammer1Parser.RBRACKET, grammer1Parser.AND, grammer1Parser.OR, grammer1Parser.EQ, grammer1Parser.GT, grammer1Parser.LT, grammer1Parser.NE, grammer1Parser.GE, grammer1Parser.LE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==grammer1Parser.PLUS or _la==grammer1Parser.MIN:
                self.state = 67
                _la = self._input.LA(1)
                if not(_la==grammer1Parser.PLUS or _la==grammer1Parser.MIN):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 70
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 68
                    self.vm()
                    pass

                elif la_ == 2:
                    self.state = 69
                    self.neg_sol()
                    pass


                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mod(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammer1Parser.ModContext)
            else:
                return self.getTypedRuleContext(grammer1Parser.ModContext,i)


        def MAAL(self, i:int=None):
            if i is None:
                return self.getTokens(grammer1Parser.MAAL)
            else:
                return self.getToken(grammer1Parser.MAAL, i)

        def DEEL(self, i:int=None):
            if i is None:
                return self.getTokens(grammer1Parser.DEEL)
            else:
                return self.getToken(grammer1Parser.DEEL, i)

        def neg_sol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammer1Parser.Neg_solContext)
            else:
                return self.getTypedRuleContext(grammer1Parser.Neg_solContext,i)


        def getRuleIndex(self):
            return grammer1Parser.RULE_vm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVm" ):
                listener.enterVm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVm" ):
                listener.exitVm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVm" ):
                return visitor.visitVm(self)
            else:
                return visitor.visitChildren(self)




    def vm(self):

        localctx = grammer1Parser.VmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.mod()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==grammer1Parser.MAAL or _la==grammer1Parser.DEEL:
                self.state = 78
                _la = self._input.LA(1)
                if not(_la==grammer1Parser.MAAL or _la==grammer1Parser.DEEL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 81
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 79
                    self.mod()
                    pass

                elif la_ == 2:
                    self.state = 80
                    self.neg_sol()
                    pass


                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vm_sol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammer1Parser.Vm_solContext)
            else:
                return self.getTypedRuleContext(grammer1Parser.Vm_solContext,i)


        def MOD(self):
            return self.getToken(grammer1Parser.MOD, 0)

        def neg_sol(self):
            return self.getTypedRuleContext(grammer1Parser.Neg_solContext,0)


        def getRuleIndex(self):
            return grammer1Parser.RULE_mod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMod" ):
                listener.enterMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMod" ):
                listener.exitMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMod" ):
                return visitor.visitMod(self)
            else:
                return visitor.visitChildren(self)




    def mod(self):

        localctx = grammer1Parser.ModContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.vm_sol()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==grammer1Parser.MOD:
                self.state = 89
                self.match(grammer1Parser.MOD)
                self.state = 92
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 90
                    self.vm_sol()
                    pass

                elif la_ == 2:
                    self.state = 91
                    self.neg_sol()
                    pass




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Neg_solContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def neg_value(self):
            return self.getTypedRuleContext(grammer1Parser.Neg_valueContext,0)


        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(grammer1Parser.LBRACKET)
            else:
                return self.getToken(grammer1Parser.LBRACKET, i)

        def MIN(self):
            return self.getToken(grammer1Parser.MIN, 0)

        def plus(self):
            return self.getTypedRuleContext(grammer1Parser.PlusContext,0)


        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(grammer1Parser.RBRACKET)
            else:
                return self.getToken(grammer1Parser.RBRACKET, i)

        def getRuleIndex(self):
            return grammer1Parser.RULE_neg_sol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeg_sol" ):
                listener.enterNeg_sol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeg_sol" ):
                listener.exitNeg_sol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeg_sol" ):
                return visitor.visitNeg_sol(self)
            else:
                return visitor.visitChildren(self)




    def neg_sol(self):

        localctx = grammer1Parser.Neg_solContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_neg_sol)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammer1Parser.NEG_INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.neg_value()
                pass
            elif token in [grammer1Parser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.match(grammer1Parser.LBRACKET)
                self.state = 98
                self.match(grammer1Parser.MIN)
                self.state = 99
                self.match(grammer1Parser.LBRACKET)
                self.state = 100
                self.plus()
                self.state = 101
                self.match(grammer1Parser.RBRACKET)
                self.state = 102
                self.match(grammer1Parser.RBRACKET)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vm_solContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(grammer1Parser.ValueContext,0)


        def LBRACKET(self):
            return self.getToken(grammer1Parser.LBRACKET, 0)

        def plus(self):
            return self.getTypedRuleContext(grammer1Parser.PlusContext,0)


        def RBRACKET(self):
            return self.getToken(grammer1Parser.RBRACKET, 0)

        def getRuleIndex(self):
            return grammer1Parser.RULE_vm_sol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVm_sol" ):
                listener.enterVm_sol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVm_sol" ):
                listener.exitVm_sol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVm_sol" ):
                return visitor.visitVm_sol(self)
            else:
                return visitor.visitChildren(self)




    def vm_sol(self):

        localctx = grammer1Parser.Vm_solContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_vm_sol)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammer1Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.value()
                pass
            elif token in [grammer1Parser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(grammer1Parser.LBRACKET)
                self.state = 108
                self.plus()
                self.state = 109
                self.match(grammer1Parser.RBRACKET)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Neg_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEG_INT(self):
            return self.getToken(grammer1Parser.NEG_INT, 0)

        def getRuleIndex(self):
            return grammer1Parser.RULE_neg_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeg_value" ):
                listener.enterNeg_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeg_value" ):
                listener.exitNeg_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeg_value" ):
                return visitor.visitNeg_value(self)
            else:
                return visitor.visitChildren(self)




    def neg_value(self):

        localctx = grammer1Parser.Neg_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_neg_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(grammer1Parser.NEG_INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(grammer1Parser.INT, 0)

        def getRuleIndex(self):
            return grammer1Parser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = grammer1Parser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(grammer1Parser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





