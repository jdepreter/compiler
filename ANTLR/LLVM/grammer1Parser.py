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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("{\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\6\2\35\n\2\r\2\16\2\36\3\2\3\2\6\2#\n\2\r\2\16\2$\7\2")
        buf.write("\'\n\2\f\2\16\2*\13\2\3\3\3\3\3\4\3\4\3\4\7\4\61\n\4\f")
        buf.write("\4\16\4\64\13\4\3\5\5\5\67\n\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\5\5B\n\5\3\6\3\6\5\6F\n\6\3\7\3\7\5\7J\n")
        buf.write("\7\3\7\3\7\3\7\5\7O\n\7\7\7Q\n\7\f\7\16\7T\13\7\3\b\3")
        buf.write("\b\3\b\3\b\5\bZ\n\b\7\b\\\n\b\f\b\16\b_\13\b\3\t\3\t\3")
        buf.write("\t\3\t\5\te\n\t\5\tg\n\t\3\n\3\n\3\n\3\n\3\n\5\nn\n\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\5\13u\n\13\3\f\3\f\3\r\3\r\3")
        buf.write("\r\2\2\16\2\4\6\b\n\f\16\20\22\24\26\30\2\2\2\177\2\32")
        buf.write("\3\2\2\2\4+\3\2\2\2\6-\3\2\2\2\bA\3\2\2\2\nE\3\2\2\2\f")
        buf.write("I\3\2\2\2\16U\3\2\2\2\20`\3\2\2\2\22m\3\2\2\2\24t\3\2")
        buf.write("\2\2\26v\3\2\2\2\30x\3\2\2\2\32\34\5\4\3\2\33\35\7\3\2")
        buf.write("\2\34\33\3\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36\37\3\2")
        buf.write("\2\2\37(\3\2\2\2 \"\5\4\3\2!#\7\3\2\2\"!\3\2\2\2#$\3\2")
        buf.write("\2\2$\"\3\2\2\2$%\3\2\2\2%\'\3\2\2\2& \3\2\2\2\'*\3\2")
        buf.write("\2\2(&\3\2\2\2()\3\2\2\2)\3\3\2\2\2*(\3\2\2\2+,\5\6\4")
        buf.write("\2,\5\3\2\2\2-\62\5\b\5\2./\7\13\2\2/\61\5\b\5\2\60.\3")
        buf.write("\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\7")
        buf.write("\3\2\2\2\64\62\3\2\2\2\65\67\7\4\2\2\66\65\3\2\2\2\66")
        buf.write("\67\3\2\2\2\678\3\2\2\289\7\5\2\29:\5\6\4\2:;\7\6\2\2")
        buf.write(";B\3\2\2\2<=\5\n\6\2=>\7\n\2\2>?\5\n\6\2?B\3\2\2\2@B\5")
        buf.write("\n\6\2A\66\3\2\2\2A<\3\2\2\2A@\3\2\2\2B\t\3\2\2\2CF\3")
        buf.write("\2\2\2DF\5\f\7\2EC\3\2\2\2ED\3\2\2\2F\13\3\2\2\2GJ\5\16")
        buf.write("\b\2HJ\3\2\2\2IG\3\2\2\2IH\3\2\2\2JR\3\2\2\2KN\7\17\2")
        buf.write("\2LO\5\16\b\2MO\5\22\n\2NL\3\2\2\2NM\3\2\2\2OQ\3\2\2\2")
        buf.write("PK\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2S\r\3\2\2\2TR")
        buf.write("\3\2\2\2U]\5\20\t\2VY\7\16\2\2WZ\5\20\t\2XZ\5\22\n\2Y")
        buf.write("W\3\2\2\2YX\3\2\2\2Z\\\3\2\2\2[V\3\2\2\2\\_\3\2\2\2][")
        buf.write("\3\2\2\2]^\3\2\2\2^\17\3\2\2\2_]\3\2\2\2`f\5\24\13\2a")
        buf.write("d\7\7\2\2be\5\24\13\2ce\5\22\n\2db\3\2\2\2dc\3\2\2\2e")
        buf.write("g\3\2\2\2fa\3\2\2\2fg\3\2\2\2g\21\3\2\2\2hn\5\26\f\2i")
        buf.write("j\7\b\2\2jk\5\f\7\2kl\7\t\2\2ln\3\2\2\2mh\3\2\2\2mi\3")
        buf.write("\2\2\2n\23\3\2\2\2ou\5\30\r\2pq\7\5\2\2qr\5\f\7\2rs\7")
        buf.write("\6\2\2su\3\2\2\2to\3\2\2\2tp\3\2\2\2u\25\3\2\2\2vw\7\f")
        buf.write("\2\2w\27\3\2\2\2xy\7\r\2\2y\31\3\2\2\2\22\36$(\62\66A")
        buf.write("EINRY]dfmt")
        return buf.getvalue()


class grammer1Parser ( Parser ):

    grammarFileName = "grammer1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'!'", "'('", "')'", "'%'", "'(-('", 
                     "'))'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BINOP2", "BINOP", "NEG_INT", "INT", "OPERATOR", "OPERATOR2", 
                      "WS" ]

    RULE_gram = 0
    RULE_line = 1
    RULE_bool1 = 2
    RULE_bool2 = 3
    RULE_expr = 4
    RULE_plus = 5
    RULE_vm = 6
    RULE_mod = 7
    RULE_neg_sol = 8
    RULE_vm_sol = 9
    RULE_neg_value = 10
    RULE_value = 11

    ruleNames =  [ "gram", "line", "bool1", "bool2", "expr", "plus", "vm", 
                   "mod", "neg_sol", "vm_sol", "neg_value", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    BINOP2=8
    BINOP=9
    NEG_INT=10
    INT=11
    OPERATOR=12
    OPERATOR2=13
    WS=14

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
            self.state = 24
            self.line()
            self.state = 26 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 25
                    self.match(grammer1Parser.T__0)

                else:
                    raise NoViableAltException(self)
                self.state = 28 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << grammer1Parser.T__0) | (1 << grammer1Parser.T__1) | (1 << grammer1Parser.T__2) | (1 << grammer1Parser.BINOP2) | (1 << grammer1Parser.BINOP) | (1 << grammer1Parser.INT) | (1 << grammer1Parser.OPERATOR2))) != 0):
                self.state = 30
                self.line()
                self.state = 32 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 31
                        self.match(grammer1Parser.T__0)

                    else:
                        raise NoViableAltException(self)
                    self.state = 34 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 40
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
            self.state = 41
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


        def BINOP(self, i:int=None):
            if i is None:
                return self.getTokens(grammer1Parser.BINOP)
            else:
                return self.getToken(grammer1Parser.BINOP, i)

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
            self.state = 43
            self.bool2()
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==grammer1Parser.BINOP:
                self.state = 44
                self.match(grammer1Parser.BINOP)
                self.state = 45
                self.bool2()
                self.state = 50
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

        def bool1(self):
            return self.getTypedRuleContext(grammer1Parser.Bool1Context,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammer1Parser.ExprContext)
            else:
                return self.getTypedRuleContext(grammer1Parser.ExprContext,i)


        def BINOP2(self):
            return self.getToken(grammer1Parser.BINOP2, 0)

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
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==grammer1Parser.T__1:
                    self.state = 51
                    self.match(grammer1Parser.T__1)


                self.state = 54
                self.match(grammer1Parser.T__2)
                self.state = 55
                self.bool1()
                self.state = 56
                self.match(grammer1Parser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.expr()
                self.state = 59
                self.match(grammer1Parser.BINOP2)
                self.state = 60
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def plus(self):
            return self.getTypedRuleContext(grammer1Parser.PlusContext,0)


        def getRuleIndex(self):
            return grammer1Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = grammer1Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
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


        def OPERATOR2(self, i:int=None):
            if i is None:
                return self.getTokens(grammer1Parser.OPERATOR2)
            else:
                return self.getToken(grammer1Parser.OPERATOR2, i)

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
        self.enterRule(localctx, 10, self.RULE_plus)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammer1Parser.T__2, grammer1Parser.INT]:
                self.state = 69
                self.vm()
                pass
            elif token in [grammer1Parser.T__0, grammer1Parser.T__3, grammer1Parser.T__6, grammer1Parser.BINOP2, grammer1Parser.BINOP, grammer1Parser.OPERATOR2]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==grammer1Parser.OPERATOR2:
                self.state = 73
                self.match(grammer1Parser.OPERATOR2)
                self.state = 76
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [grammer1Parser.T__2, grammer1Parser.INT]:
                    self.state = 74
                    self.vm()
                    pass
                elif token in [grammer1Parser.T__5, grammer1Parser.NEG_INT]:
                    self.state = 75
                    self.neg_sol()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 82
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


        def OPERATOR(self, i:int=None):
            if i is None:
                return self.getTokens(grammer1Parser.OPERATOR)
            else:
                return self.getToken(grammer1Parser.OPERATOR, i)

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
        self.enterRule(localctx, 12, self.RULE_vm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.mod()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==grammer1Parser.OPERATOR:
                self.state = 84
                self.match(grammer1Parser.OPERATOR)
                self.state = 87
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [grammer1Parser.T__2, grammer1Parser.INT]:
                    self.state = 85
                    self.mod()
                    pass
                elif token in [grammer1Parser.T__5, grammer1Parser.NEG_INT]:
                    self.state = 86
                    self.neg_sol()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 93
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
        self.enterRule(localctx, 14, self.RULE_mod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.vm_sol()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==grammer1Parser.T__4:
                self.state = 95
                self.match(grammer1Parser.T__4)
                self.state = 98
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [grammer1Parser.T__2, grammer1Parser.INT]:
                    self.state = 96
                    self.vm_sol()
                    pass
                elif token in [grammer1Parser.T__5, grammer1Parser.NEG_INT]:
                    self.state = 97
                    self.neg_sol()
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


    class Neg_solContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def neg_value(self):
            return self.getTypedRuleContext(grammer1Parser.Neg_valueContext,0)


        def plus(self):
            return self.getTypedRuleContext(grammer1Parser.PlusContext,0)


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
        self.enterRule(localctx, 16, self.RULE_neg_sol)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammer1Parser.NEG_INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.neg_value()
                pass
            elif token in [grammer1Parser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.match(grammer1Parser.T__5)
                self.state = 104
                self.plus()
                self.state = 105
                self.match(grammer1Parser.T__6)
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


        def plus(self):
            return self.getTypedRuleContext(grammer1Parser.PlusContext,0)


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
        self.enterRule(localctx, 18, self.RULE_vm_sol)
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [grammer1Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.value()
                pass
            elif token in [grammer1Parser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.match(grammer1Parser.T__2)
                self.state = 111
                self.plus()
                self.state = 112
                self.match(grammer1Parser.T__3)
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
        self.enterRule(localctx, 20, self.RULE_neg_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
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
        self.enterRule(localctx, 22, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(grammer1Parser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





