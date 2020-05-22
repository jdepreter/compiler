from src.symbolTables import SymbolType
from copy import deepcopy


class MIPSOffset:
    def __init__(self, symbols = {}):
        self.symbols = {}
        for key in symbols.keys():
            self.symbols[deepcopy(key)] = deepcopy(symbols[key])

    def add_symbol(self, symbol: SymbolType):
        self.symbols[symbol.name] = 0

    def get_offset(self, symbol: SymbolType):
        return self.symbols[symbol.name]

    def increase_offset(self, amount: int):
        for key in self.symbols.keys():
            self.symbols[key] = self.symbols[key] + amount

    def decrease_offset(self, amount: int):
        for key in self.symbols.keys():
            self.symbols[key] = self.symbols[key] - amount
