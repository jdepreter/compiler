from src.compile import to_llvm

import os

base_path = os.getcwd() + '/src/tests/benchmark1/CorrectCode'
# with os.scandir(base_path) as entries:
#     for entry in entries:
#         if entry.is_file():
#             try:
#                 print(to_llvm('./src/tests/benchmark1/CorrectCode/' + entry.name, entry.name.split('.')[0]))
#                 print(entry.name, 'success')
#             except Exception as e:
#                 print(e)
#                 print(entry.name, 'failed')

base_path = os.getcwd() + '/src/tests/benchmark1/SemanticErrors/'
with os.scandir(base_path) as entries:
    for entry in entries:
        if entry.is_file():
            try:
                print(to_llvm('./src/tests/benchmark1/SemanticErrors/' + entry.name, entry.name.split('.')[0]))
                print(entry.name, 'success')
            except Exception as e:
                print(e)
                print(entry.name, 'might have failed')
