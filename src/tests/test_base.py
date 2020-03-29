import unittest
from src.compile import to_llvm
import src
import re


def clear_newlines(string: str) -> str:
    return re.sub("\n", "", string)


class Assignment1(unittest.TestCase):
    def test_basic_files(self):
        self.assertEqual(to_llvm("basic_declaration.txt", "basic_declaration"), "")
        self.assertEqual(to_llvm("basic_definition.txt", "basic_definition"), "")

    def test_scope(self):
        self.assertEqual(to_llvm("scope_1.txt", "scope_1"), "")
        self.assertEqual(to_llvm("scope_empty.txt", "scope_empty"), "")
        self.assertEqual(to_llvm("scope_nested.txt", "scope_nested"), "2\n3\n")

    def test_folding(self):
        self.assertEqual(to_llvm("folding.txt", "folding"), "40.000000\n13.000000\n")

    def test_bool_folding(self):
        self.assertEqual(to_llvm("bool_testing.txt", "bool_testing"), "6\n")

    def test_modulo(self):
        self.assertEqual(to_llvm("modulo.txt", "modulo"), "1\n")

    def test_char(self):
        self.assertEqual(to_llvm("char_casting.txt", "char_casting"), "b\nc\nd\n97\n")
        self.assertEqual(to_llvm("char_folding.txt", "char_folding"), "d\n")

    def test_pointers(self):
        self.assertEqual(to_llvm("pointers.txt", "pointers"), "")
        self.assertEqual(to_llvm("pointer_dereference.txt", "pointer_dereference"), "3\n")

    def test_not(self):
        self.assertEqual(to_llvm("not_testing.txt", "not_testing"), "1\n")

    def test_unary(self):
        self.assertEqual(to_llvm("unary_magic.txt", "unary_magic"), "3\n")
        self.assertEqual(to_llvm("unary_++.txt", "unary_++"), "7\n9\n9\n")
        self.assertEqual(to_llvm("unary_--.txt", "unary_--"), "5\n3\n3\n")

    def test_errors(self):
        with self.assertRaises(src.CustomExceptions.CSyntaxError):
            to_llvm("syntax_error.txt", "syntax_error")

        with self.assertRaises(src.CustomExceptions.CSyntaxError):
            to_llvm("syntax_error_1.txt", "syntax_error_1")

        with self.assertRaises(src.CustomExceptions.CSyntaxError):
            to_llvm("assignment_to_r_value.txt", "assignment_to_r_value")

        with self.assertRaises(src.CustomExceptions.UninitializedVariable):
            to_llvm("uninitialised_var_error.txt", "uninit_var_error")

        with self.assertRaises(src.CustomExceptions.UndeclaredVariable):
            to_llvm("undeclared_var_error.txt", "undeclared_var_error")

        with self.assertRaises(src.CustomExceptions.ConstAssignment):
            to_llvm("const_assignment_error.txt", "const_assignment")

        with self.assertRaises(src.CustomExceptions.DuplicateDeclaration):
            to_llvm("duplicate_declaration_error.txt", "duplicate_declaration")

        with self.assertRaises(src.CustomExceptions.IncompatibleType):
            to_llvm("incompatible_type_error.txt", "incompatible_type")


    def test_if_else(self):
        self.assertEqual(to_llvm("ifelse/true_true.txt", "true_true"), "8\n9\n")
        self.assertEqual(to_llvm("ifelse/true_false.txt", "true_false"), "8\n9\n")
        self.assertEqual(to_llvm("ifelse/false.txt", "false"), "f\nf\n2\n")
        self.assertEqual(to_llvm("ifelse/false_true.txt", "false"), "t\nf\n2\n")


class IfElse(unittest.TestCase):
    def test_if_else(self):
        self.assertEqual(to_llvm("ifelse/true_true.txt", "true_true"), "8\n9\n")
        self.assertEqual(to_llvm("ifelse/true_false.txt", "true_false"), "8\n9\n")
        self.assertEqual(to_llvm("ifelse/false.txt", "false"), "f\nf\n2\n")
        self.assertEqual(to_llvm("ifelse/false_true.txt", "false"), "t\nf\n2\n")


class Loops(unittest.TestCase):
    def test_for_loop(self):
        self.assertEqual(clear_newlines(to_llvm("loops/loop.txt", "loop")), "123412")
        self.assertEqual(clear_newlines(to_llvm("loops/nested_break.txt", "nested_break")), "112123123123123123123")

    def test_for_continue(self):
        self.assertEqual(clear_newlines(to_llvm("loops/for_continue.txt", "for_continue")), "23456789")

    def test_forreturn(self):
        self.assertEqual(clear_newlines(to_llvm("loops/loop_return.txt", "loop_return")), "12341")

    def test_break_error(self):
        with self.assertRaises(src.CustomExceptions.BreakError):
            to_llvm("loops/break_error.txt", "break_error")


class Function(unittest.TestCase):
    def test_faculty(self):
        self.assertEqual(clear_newlines(to_llvm("functions/faculty.txt", "faculty")), "6")


if __name__ == '__main__':
    unittest.main()
