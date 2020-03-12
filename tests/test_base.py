import unittest
import test


class TestCase(unittest.TestCase):
    def test_basic_files(self):
        test.to_llvm("basic_declaration.txt")
        test.to_llvm("basic_definition.txt")

    def test_scope(self):
        test.to_llvm("scope_1.txt")
        test.to_llvm("scope_empty.txt")
