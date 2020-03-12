import unittest
import test
from CustomExceptions import *
from antlr4.error.Errors import NoViableAltException


class TestCase(unittest.TestCase):
    def test_basic_files(self):
        test.to_llvm("basic_declaration.txt", "basic_declaration.txt")
        test.to_llvm("basic_definition.txt", "basic_definition.txt")

    def test_scope(self):
        test.to_llvm("scope_1.txt", "scope_1.txt")
        test.to_llvm("scope_empty.txt", "scope_empty.txt")
        test.to_llvm("scope_nested.txt", "scope_nested.txt")

    def test_folding(self):
        test.to_llvm("folding.txt", "folding.txt")

    def test_errors(self):
        with self.assertRaises(CSyntaxError):
            test.to_llvm("syntax_error.txt", "syntax_error.txt")

        with self.assertRaises(CSyntaxError):
            test.to_llvm("syntax_error_1.txt", "syntax_error_1.txt")
