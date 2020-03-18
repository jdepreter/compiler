import unittest
from test import to_llvm
from CustomExceptions import *


class TestCase(unittest.TestCase):
    def test_basic_files(self):
        to_llvm("basic_declaration.txt", "basic_declaration")
        to_llvm("basic_definition.txt", "basic_definition")

    def test_scope(self):
        to_llvm("scope_1.txt", "scope_1")
        to_llvm("scope_empty.txt", "scope_empty")
        to_llvm("scope_nested.txt", "scope_nested")

    def test_folding(self):
        to_llvm("folding.txt", "folding")

    def test_bool_folding(self):
        to_llvm("bool_testing.txt", "bool_testing")

    def test_modulo(self):
        to_llvm("modulo.txt", "modulo")

    def test_char(self):
        to_llvm("char_casting.txt", "char_casting")
        to_llvm("char_folding.txt", "char_folding")

    def test_pointers(self):
        to_llvm("pointers.txt", "pointers")

    def test_unary(self):
        to_llvm("unary_magic.txt", "unary_magic")
        to_llvm("unary_++.txt", "unary_++")
        to_llvm("unary_--.txt", "unary_--")

    def test_errors(self):
        with self.assertRaises(CSyntaxError):
            to_llvm("syntax_error.txt", "syntax_error")

        with self.assertRaises(CSyntaxError):
            to_llvm("syntax_error_1.txt", "syntax_error_1")

        with self.assertRaises(UninitializedVariable):
            to_llvm("uninitialised_var_error.txt", "uninit_var_error")

        with self.assertRaises(UndeclaredVariable):
            to_llvm("undeclared_var_error.txt", "undeclared_var_error")

        with self.assertRaises(ConstAssignment):
            to_llvm("const_assignment_error.txt", "const_assignment")

        with self.assertRaises(DuplicateDeclaration):
            to_llvm("duplicate_declaration_error.txt", "duplicate_declaration")

        with self.assertRaises(IncompatibleType):
            to_llvm("incompatible_type_error.txt", "incompatible_type")


if __name__ == '__main__':
    unittest.main()
