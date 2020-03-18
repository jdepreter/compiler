import unittest
from test import to_llvm
from CustomExceptions import CSyntaxError


class TestCase(unittest.TestCase):
    def test_basic_files(self):
        to_llvm("basic_declaration.txt", "basic_declaration")
        to_llvm("basic_definition.txt", "basic_definition")

    def test_scope(self):
        to_llvm("scope_1.txt", "scope_1.txt")
        to_llvm("scope_empty.txt", "scope_empty")
        to_llvm("scope_nested.txt", "scope_nested")

    def test_int_folding(self):
        to_llvm("folding.txt", "folding.txt")

    def test_bool_folding(self):
        to_llvm("bool_testing.txt", "bool_testing")

    def test_pointers(self):
        to_llvm("pointers.txt", "bool_testing")

    def test_errors(self):
        with self.assertRaises(CSyntaxError):
            to_llvm("syntax_error.txt", "syntax_error")

        with self.assertRaises(CSyntaxError):
            to_llvm("syntax_error_1.txt", "syntax_error_1")


if __name__ == '__main__':
    unittest.main()
