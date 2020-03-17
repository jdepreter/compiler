import unittest
import test
from CustomExceptions import CSyntaxError
from antlr4.error.Errors import NoViableAltException


class TestCase(unittest.TestCase):
    def test_basic_files(self):
        test.to_llvm("./tests/basic_declaration.txt", "basic_declaration.txt")
        test.to_llvm("./tests/basic_definition.txt", "basic_definition.txt")

    def test_scope(self):
        test.to_llvm("./tests/scope_1.txt", "scope_1.txt")
        test.to_llvm("./tests/scope_empty.txt", "scope_empty.txt")
        test.to_llvm("./tests/scope_nested.txt", "scope_nested.txt")

    def test_folding(self):
        test.to_llvm("./tests/folding.txt", "folding.txt")

    def test_errors(self):
        with self.assertRaises(CSyntaxError):
            test.to_llvm("./tests/syntax_error.txt", "syntax_error.txt")

        with self.assertRaises(CSyntaxError):
            test.to_llvm("./tests/syntax_error_1.txt", "syntax_error_1.txt")


if __name__ == '__main__':
    unittest.main()
