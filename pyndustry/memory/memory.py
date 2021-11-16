from __future__ import annotations
from pyndustry import (Command, InsideCommand, Variable)



class ReadMemory(Command):
    """Reads data from memory storage.

    Args:
        memory (Union): Memory storage name.
        index (Union): Index of data.
        result (Union): Variable for result value.
    """
    def __init__(
            self,
            memory : Union(Variable, str),
            index: Union(Variable, int),
            result: Union(Variable, str)
        ):
        Command.__init__(self)
        self.name = 'read'
        self.memory = memory
        self.index = index
        self.result = result

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'{self.name} {self.result} {self.memory} {self.index}'
        return value



class WriteMemory(Command):
    """Writes data to memory storage.

    Args:
        memory (Union): Memory storage name.
        index (Union): Index of data.
        result (Union): Variable for result value.
    """
    def __init__(
            self,
            memory : Union(Variable, str),
            index: Union(Variable, int),
            value: Union(Variable, str)
        ):
        Command.__init__(self)
        self.name = 'write'
        self.memory = memory
        self.index = index
        self.value = value

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'{self.name} {self.value} {self.memory} {self.index}'
        return value


class MemoryStorage(Variable):
    """Class for easy interaction with memory storages.

    Args:
        name (Union): Storage name.
    """
    def __init__(self, name : Union(Variable, str)):
        self.name = name

        if isinstance(name, Variable):
            self.name = name.name
        self.value_name = f'memoryStorageResult__{self.name}'
        
        
    # a = var[n]
    def __getitem__(self, key) -> Variable:
        ReadMemory(self.name, key, self.value_name)
        return Variable(self.value_name)
    

    # var[n] = a
    def __setitem__(self, key, value) -> None:
        WriteMemory(self.name, key, value)

