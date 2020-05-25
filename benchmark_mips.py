from src.compile_mips import to_mips

import os

expected_output_correct = {
    'binaryOperations1.c': '10; 10.0; 10; 10.0; 10; 10.0; 10; 10.0; \n',
    'binaryOperations2.c': '10; 10; 10; 10; \n',
    'breakAndContinue.c': '0\n1\n2\n3\n4\n5\n\n',
    'comparisons1.c': '1; 0; 1; 0; 1; 0; \n',
    'comparisons2.c': '1; 0; 1; 0; 1; \n',
    'dereferenceAssignment.c': '10; 10\n11; 11\n\n',
    'fibonacciRecursive.c': 'Enter a number:fib(2)\t= 1;\nfib(3)\t= 2;\nfib(4)\t= 3;\nfib(5)\t= 5;\nfib(6)\t= 8;\n\n',
    'floatToIntConversion.c': '\n',
    'for.c': '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n\n',
    'forwardDeclaration.c': 'Hello World\nHello World\n\n',
    'if.c': 'Hello world!\nHello world!\n\n',
    'ifElse.c': 'Hello world!\nHello world!\n\n',
    'intToFloatConversion.c': '\n',
    'modulo.c': '1\n\n',
    'pointerArgument.c': '42; 42\n43; 43\n44; 44\n45; 45\n\n',
    'prime.c': 'Enter the number of prime numbers required\nFirst 5 prime numbers are :\n2\n3\n5\n7\n11\n\n',
    'printf1.c': 'Hello World!\n\n',
    'printf2.c': 'Hello World!\n\n',
    'printf3.c': '100.5%\n',
    'scanf1.c': 'Enter two numbers:5; 6\n',
    'scanf2.c': 'Enter a 5-character string:1234\n',
    'scoping.c': '10;20;30;40;\n',
    'unaryOperations.c': '9; 10; 11; 12; 13; 14; \n',
    'variables1.c': '5; 0.5; c\n',
    'variables2.c': '5; 0.5; c\n',
    'variables3.c': '10; 20; 30\n',
    'variables4.c': '10\n',
    'variables5.c': '10; 10; 10\n',
    'variables6.c': '10; 10; 10\n',
    'variables7.c': '1; 2; 3;\n',
    'variables8.c': '10; 20; 30; \n',
    'while.c': '1;2;3;4;5;\n',
}

expected_output_semantic = {
    'arrayAccessTypeMismatch.c': 'Error Line 3, Position 6: array subscript is not an integer',  #
    'arrayAccessTypeMismatch2.c': 'Error Line 3, Position 4: x is not an array',  #
    'arrayCompareError.c': 'pointer type cannot be operated on',  #
    'arraySizeTypeMismatch.c': 'Error Line 2, Position 10: array subscript is not an integer',  #
    'declarationDeclarationMismatch1.c': '[Error] Line 5: Conflicting types for f ',
    'declarationDeclarationMismatch2.c': '[Error] Line 5: Conflicting types for f ',
    'declarationDeclarationMismatch3.c': '[Error] Line 5: Conflicting types for f ',
    'declarationDefinitionMismatch1.c': '[Error] Line 5: Conflicting types for f ',
    'declarationDefinitionMismatch2.c': '[Error] Line 5: Conflicting types for f ',
    'declarationDefinitionMismatch3.c': '[Error] Line 5: Conflicting types for f ',
    'definitionInLocalScope.c': '[Error] Line 5, Position 4: function definition is not allowed here',
    'dereferenceTypeMismatch1.c': "[Syntax Error] Line 2 Position 5: no viable alternative at input '*5'",
    'dereferenceTypeMismatch2.c': "[Syntax Error] Line 4 Position 6: no viable alternative at input '&5'",
    'functionCallargumentMismatch1.c': '[Error] Line 4, Position 6: Too few arguments for calling f missing arg(s) with type(s): int',
    'functionCallargumentMismatch2.c': '[Error] Line 4, Position 9: Too many arguments for calling f',
    'functionCallargumentMismatch3.c': '[Error] Line 4, Position 4: Too few arguments for calling printf missing arg(s) with type(s): float',
    'functionCallargumentMismatch4.c': '[Error] Line 4, Position 4: Too many arguments for calling printf',
    'functionRedefinition1.c': '[Error] Line 7, Position 0: Duplicate definition of method f ',
    'functionRedefinition2.c': '[Error] Line 7, Position 0: Duplicate definition of method f ',
    'functionRedefinition3.c': '[Error] Line 7, Position 0: Duplicate definition of method f ',
    'incompatibleTypes1.c': '\n',
    'incompatibleTypes2.c': '\n',  # '[Warning] line 4: implicit cast from char to int',  #
    'incompatibleTypes3.c': 'Can\'t cast void',
    'incompatibleTypes4.c': 'pointer type cannot be operated on',
    'incompatibleTypes5.c': '[Error] Line 3, Position 10: variable x is not initialised',
    'incompatibleTypes6.c': "Segmentation fault (core dumped)\nCommand 'clang ./llvm/incompatibleTypes6.ll -o ./llvm/incompatibleTypes6 && ./llvm/incompatibleTypes6' returned non-zero exit status 139.",
    'incompatibleTypes7.c': '',  #'[Warning] line 5: implicit cast from char to int',
    'invalidIncludeError.c': '[Syntax Error] Line 1 Position 25: token recognition error at: \'.\'',  #
    'invalidLoopControlStatement.c': '[Error] Line 2 Position 1 continue statement not within loop',
    'invalidUnaryOperation.c': "[Syntax Error] Line 4 Position 24: no viable alternative at input 'printf(\"%d; \",9++'",
    'mainNotFound.c': 'function main is not defined',
    'parameterRedefinition1.c': '[Error] Line 3, Position 13: Duplicate declaration of variable a ',
    'parameterRedefinition2.c': '[Error] Line 3, Position 13: Duplicate declaration of variable a ',
    'parameterRedefinition3.c': '[Error] Line 3, Position 30: Duplicate declaration of variable a ',
    'pointerOperationError.c': '[Error] Line 5, Position 8: variable a is not initialised',  # Andere error dan verwacht
    'returnOutsideFunction.c': 'Error at line: 1 column :0 return statement outside of function ',  #
    'returnTypeMismatch.c': 'Error at line: 2 column :4 void function should not return value ',
    'undeclaredFunction.c': '[Error] Line 2, Position 4: function f() is undeclared',
    'undeclaredVariable1.c': '[Error] Line 2, Position 4: variable x is undeclared',
    'undeclaredVariable2.c': '[Error] Line 2, Position 3: variable x is undeclared',
    'undeclaredVariable3.c': '[Error] Line 3, Position 4: variable z is undeclared',
    'variableRedefinition1.c': '[Error] Line 4, Position 4: Duplicate declaration of variable x ',
    'variableRedefinition2.c': '[Error] Line 4, Position 4: Duplicate declaration of variable x ',
    'variableRedefinition3.c': '[Error] Line 4, Position 4: Duplicate declaration of variable x ',
    'variableRedefinition4.c': '[Error] Line 3, Position 0: Duplicate declaration of variable x ',
    'variableRedefinition5.c': '[Error] Line 2, Position 0: Duplicate declaration of variable x ',  #
    'variableRedefinition6.c': '[Error] Line 3, Position 0: Duplicate declaration of variable x ',
}

# print("Correct Code: ")
# base_path = os.getcwd() + '/src/tests/benchmark1/CorrectCode'
# with os.scandir(base_path) as entries:
#     for entry in entries:
#         if entry.is_file():
#             try:
#                 if entry.name == '.DS_Store':
#                     continue
#                 print(entry.name)
#                 output = to_mips('./src/tests/benchmark1/CorrectCode/' + entry.name, entry.name.split('.')[0])
#                 if output != expected_output_correct[entry.name]:
#                     print("^", output)
#                     print("^", expected_output_correct[entry.name])
#                     # quit(1)
#                 else:
#                     print(output)
#                 print(entry.name, 'compiled and executed without errors')
#             except Exception as e:
#                 print(e)
#                 print(entry.name, 'failed')

print("Semantic Errors: ")
base_path = os.getcwd() + '/src/tests/benchmark1/SemanticErrors/'
with os.scandir(base_path) as entries:
    for entry in entries:
        if entry.is_file():
            try:
                print(entry.name)
                output = to_mips('./src/tests/benchmark1/SemanticErrors/' + entry.name, entry.name.split('.')[0])
                if output != expected_output_semantic[entry.name]:
                    print("^", output)
                    print("^", expected_output_semantic[entry.name])
                    # quit(1)
                else:
                    print(output)
                print(entry.name, 'compiled and executed without errors')
            except Exception as e:
                print(e)
                print(entry.name, 'Error as Expected')
