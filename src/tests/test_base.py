import unittest
from src.compile import to_llvm
from src.compile_mips import to_mips
import src
import re

mars = "../../MARS/Mars4_5_mod.jar"


def clear_newlines(string: str) -> str:
    return re.sub("\n", "", string)


class Assignment1(unittest.TestCase):
    def test_basic_files(self):
        self.assertEqual(to_llvm("basic_declaration.c", "basic_declaration"), "")
        self.assertEqual(clear_newlines(to_mips("basic_declaration.c", "basic_declaration", mars=mars)), "")

        self.assertEqual(to_llvm("basic_definition.c", "basic_definition"), "")
        self.assertEqual(clear_newlines(to_mips("basic_definition.c", "basic_definition", mars=mars)), "")

    def test_scope(self):
        self.assertEqual(to_llvm("scope_1.c", "scope_1"), "")
        self.assertEqual(clear_newlines(to_mips("scope_1.c", "scope_1", mars=mars)), "")

        self.assertEqual(to_llvm("scope_empty.c", "scope_empty"), "")
        self.assertEqual(clear_newlines(to_mips("scope_empty.c", "scope_empty", mars=mars)), "")

        self.assertEqual(to_llvm("scope_nested.c", "scope_nested"), "23")
        self.assertEqual(clear_newlines(to_mips("scope_nested.c", "scope_nested", mars=mars)), "23")

    def test_folding(self):
        self.assertEqual(to_llvm("folding.c", "folding"), "2440.00000013.00000013")
        self.assertEqual(clear_newlines(to_mips("folding.c", "folding", mars=mars)), "2440.013.013")

    def test_bool_folding(self):
        self.assertEqual(to_llvm("bool_testing.c", "bool_testing"), "6")
        self.assertEqual(clear_newlines(to_mips("bool_testing.c", "bool_testing", mars=mars)), "6")

    def test_modulo(self):
        self.assertEqual(to_llvm("modulo.c", "modulo"), "1")
        self.assertEqual(clear_newlines(to_mips("modulo.c", "modulo", mars=mars)), "1")

    def test_char(self):
        self.assertEqual(to_llvm("char_casting.c", "char_casting"), "bcd97")
        self.assertEqual(clear_newlines(to_mips("char_casting.c", "char_casting", mars=mars)), "bcd97")

        self.assertEqual(to_llvm("char_folding.c", "char_folding"), "d")
        self.assertEqual(clear_newlines(to_mips("char_folding.c", "char_folding", mars=mars)), "d")

    def test_pointers(self):
        self.assertEqual(to_llvm("pointers.c", "pointers"), "")
        self.assertEqual(clear_newlines(to_mips("pointers.c", "pointers", mars=mars)), "")

        self.assertEqual(to_llvm("pointer_dereference.c", "pointer_dereference"), "3")
        self.assertEqual(clear_newlines(to_mips("pointer_dereference.c", "pointer_dereference", mars=mars)), "3")

    def test_not(self):
        self.assertEqual(to_llvm("not_testing.c", "not_testing"), "1")
        self.assertEqual(clear_newlines(to_mips("not_testing.c", "not_testing", mars=mars)), "1")

    def test_unary(self):
        self.assertEqual(to_llvm("unary_magic.c", "unary_magic"), "3")
        self.assertEqual(clear_newlines(to_mips("unary_magic.c", "unary_magic", mars=mars)), "3")

        self.assertEqual(to_llvm("unary_++.c", "unary_++"), "799")
        self.assertEqual(clear_newlines(to_mips("unary_++.c", "unary_++", mars=mars)), "799")

        self.assertEqual(to_llvm("unary_--.c", "unary_--"), "533")
        self.assertEqual(clear_newlines(to_mips("unary_--.c", "unary_--", mars=mars)), "533")

    def test_errors(self):
        with self.assertRaises(src.CustomExceptions.CSyntaxError):
            to_llvm("syntax_error.c", "syntax_error")

        with self.assertRaises(src.CustomExceptions.CSyntaxError):
            to_llvm("syntax_error_1.c", "syntax_error_1")

        with self.assertRaises(src.CustomExceptions.CSyntaxError):
            to_llvm("assignment_to_r_value.c", "assignment_to_r_value")

        with self.assertRaises(src.CustomExceptions.UninitializedVariable):
            to_llvm("uninitialised_var_error.c", "uninit_var_error")

        with self.assertRaises(src.CustomExceptions.UndeclaredVariable):
            to_llvm("undeclared_var_error.c", "undeclared_var_error")

        with self.assertRaises(src.CustomExceptions.ConstAssignment):
            to_llvm("const_assignment_error.c", "const_assignment")

        with self.assertRaises(src.CustomExceptions.DuplicateDeclaration):
            to_llvm("duplicate_declaration_error.c", "duplicate_declaration")

        with self.assertRaises(src.CustomExceptions.IncompatibleType):
            to_llvm("incompatible_type_error.c", "incompatible_type")

    def test_errors_mips(self):
        with self.assertRaises(src.CustomExceptions.CSyntaxError):
            clear_newlines(to_mips("syntax_error.c", "syntax_error", mars=mars))

        with self.assertRaises(src.CustomExceptions.CSyntaxError):
            clear_newlines(to_mips("syntax_error_1.c", "syntax_error_1", mars=mars))

        with self.assertRaises(src.CustomExceptions.CSyntaxError):
            clear_newlines(to_mips("assignment_to_r_value.c", "assignment_to_r_value", mars=mars))

        with self.assertRaises(src.CustomExceptions.UninitializedVariable):
            clear_newlines(to_mips("uninitialised_var_error.c", "uninit_var_error", mars=mars))

        with self.assertRaises(src.CustomExceptions.UndeclaredVariable):
            clear_newlines(to_mips("undeclared_var_error.c", "undeclared_var_error", mars=mars))

        with self.assertRaises(src.CustomExceptions.ConstAssignment):
            clear_newlines(to_mips("const_assignment_error.c", "const_assignment", mars=mars))

        with self.assertRaises(src.CustomExceptions.DuplicateDeclaration):
            clear_newlines(to_mips("duplicate_declaration_error.c", "duplicate_declaration", mars=mars))

        with self.assertRaises(src.CustomExceptions.IncompatibleType):
            clear_newlines(to_mips("incompatible_type_error.c", "incompatible_type", mars=mars))


class IfElse(unittest.TestCase):
    def test_if_else(self):
        self.assertEqual(to_llvm("ifelse/true_true.c", "true_true"), "89")
        self.assertEqual(clear_newlines(to_mips("ifelse/true_true.c", "true_true", mars=mars)), "89")

        self.assertEqual(to_llvm("ifelse/true_false.c", "true_false"), "89")
        self.assertEqual(clear_newlines(to_mips("ifelse/true_false.c", "true_false", mars=mars)), "89")

        self.assertEqual(to_llvm("ifelse/false.c", "false"), "ff2")
        self.assertEqual(clear_newlines(to_mips("ifelse/false.c", "false", mars=mars)), "ff2")

        self.assertEqual(to_llvm("ifelse/false_true.c", "false"), "tf2")
        self.assertEqual(clear_newlines(to_mips("ifelse/false_true.c", "false", mars=mars)), "tf2")

    def test_if_else_assignment(self):
        self.assertEqual(to_llvm("ifelse/fancy_if_false.c", "fancy_if_false"), "")
        self.assertEqual(clear_newlines(to_mips("ifelse/fancy_if_false.c", "fancy_if_false", mars=mars)), "")

        self.assertEqual(to_llvm("ifelse/fancy_if_true.c", "fancy_if_true"), "2")
        self.assertEqual(clear_newlines(to_mips("ifelse/fancy_if_true.c", "fancy_if_true", mars=mars)), "2")

    def test_switch(self):
        self.assertEqual(to_llvm("ifelse/switch1.c", "switch1"), "3")
        self.assertEqual(clear_newlines(to_mips("ifelse/switch1.c", "switch1", mars=mars)), "3")

        self.assertEqual(to_llvm("ifelse/switch2.c", "switch2"), "Default")
        self.assertEqual(clear_newlines(to_mips("ifelse/switch2.c", "switch2", mars=mars)), "Default")


class Loops(unittest.TestCase):
    def test_for_loop(self):
        self.assertEqual(clear_newlines(to_llvm("loops/loop.c", "loop")), "123412")
        self.assertEqual(clear_newlines(to_mips("loops/loop.c", "loop", mars=mars)), "123412")

        self.assertEqual(clear_newlines(to_llvm("loops/nested_break.c", "nested_break")), "112123123123123123123")
        self.assertEqual(clear_newlines(to_mips("loops/nested_break.c", "nested_break", mars=mars)), "112123123123123123123")

    def test_for_continue(self):
        self.assertEqual(clear_newlines(to_llvm("loops/for_continue.c", "for_continue")), "23456789")
        self.assertEqual(clear_newlines(to_mips("loops/for_continue.c", "for_continue", mars=mars)), "23456789")

    def test_for_return(self):
        self.assertEqual(clear_newlines(to_llvm("loops/loop_return.c", "loop_return")), "12341")
        self.assertEqual(clear_newlines(to_mips("loops/loop_return.c", "loop_return", mars=mars)), "12341")

    def test_do_while(self):
        self.assertEqual(to_llvm("loops/do_while.c", "do_while"), "0")
        self.assertEqual(clear_newlines(to_mips("loops/do_while.c", "do_while", mars=mars)), "0")

        self.assertEqual(to_llvm("loops/do_while_2.c", "do_while_2"), "012")
        self.assertEqual(clear_newlines(to_mips("loops/do_while_2.c", "do_while_2", mars=mars)), "012")

    def test_break_error(self):
        with self.assertRaises(src.CustomExceptions.BreakError):
            to_llvm("loops/break_error.c", "break_error")

    def test_continue_error(self):
        with self.assertRaises(src.CustomExceptions.BreakError):
            to_llvm("loops/continue_error.c", "continue_error")

    def test_break_error_mips(self):
        with self.assertRaises(src.CustomExceptions.BreakError):
            to_mips("loops/break_error.c", "break_error")

    def test_continue_error_mips(self):
        with self.assertRaises(src.CustomExceptions.BreakError):
            to_mips("loops/continue_error.c", "continue_error")


class Function(unittest.TestCase):
    def test_faculty(self):
        self.assertEqual(clear_newlines(to_llvm("functions/faculty.c", "faculty")), "6")
        self.assertEqual(clear_newlines(to_mips("functions/faculty.c", "faculty")), "6")

    def test_declaration(self):
        self.assertEqual(to_llvm("functions/declaration_1.c", "declaration_1"), "2")
        self.assertEqual(clear_newlines(to_mips("functions/declaration_1.c", "declaration_1", mars=mars)), "2")

        self.assertEqual(to_llvm("functions/declaration_2.c", "declaration_2"), "2")
        self.assertEqual(clear_newlines(to_mips("functions/declaration_2.c", "declaration_2", mars=mars)), "2")

        self.assertEqual(to_llvm("functions/declaration_multi.c", "declaration_multi"), "2")
        self.assertEqual(clear_newlines(to_mips("functions/declaration_multi.c", "declaration_multi", mars=mars)), "2")

    def test_definition_only(self):
        self.assertEqual(to_llvm("functions/definition_only.c", "definition_only"), "2")
        self.assertEqual(clear_newlines(to_mips("functions/definition_only.c", "definition_only", mars=mars)), "2")

    def test_forward_declaration(self):
        self.assertEqual(to_llvm("functions/definition_after.c", "definition_after"), "2")
        self.assertEqual(clear_newlines(to_mips("functions/definition_after.c", "definition_after", mars=mars)), "2")

    def test_var_and_function(self):
        self.assertEqual(to_llvm("functions/var_and_function.c", "var_and_function"), "10")
        self.assertEqual(clear_newlines(to_mips("functions/var_and_function.c", "var_and_function", mars=mars)), "10")

    def test_duplicate_definition(self):
        with self.assertRaises(Exception):
            to_llvm("functions/multi_definition.c", "multi_definition")

    def test_duplicate_definition_mips(self):
        with self.assertRaises(Exception):
            to_mips("functions/multi_definition.c", "multi_definition", mars=mars)


if __name__ == '__main__':
    unittest.main()
