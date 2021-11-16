from __future__ import annotations
from pyndustry import (Command, InsideCommand, Variable)



class Contections():
    """Class for easy getting block in connection.
    """
    def __init__(self):
        self.value_name = 'connection'


    # a = var[n]
    def __getitem__(self, key) -> Variable:
        GetLink(key, self.value_name)
        return Variable(self.value_name)

    
    def __len__(self) -> int:
        return '@links'



class GetLink(Command):
    def __init__(
            self,
            index : Union(Variable, str, int),
            result : Union(Variable, str)='get_link_result'):
        self.index = index
        self.result = result
        self._Command__add_to_storage()


    # a = var[n]
    def __getitem__(self, key) -> Variable:
        ReadMemory(self.name, key, self.value_name)
        return Variable(self.value_name)


    def convert(self):
        value = f'getlink {self.result} {self.index}'
        return value



class Processor(InsideCommand):
    """Class make special for getting in processor vars.
    """
    __contections = Contections()

    def __init__(self):
        pass


    @property
    def x(self) -> str:
        """Processor x position.
        """
        return '@thisx'


    @property
    def y(self) -> str:
        """Processor y position.
        """
        return '@thisy'


    @property
    def current_bind_unit(self) -> str:
        """Processor bind unit.
        """
        return '@unit'


    @property
    def ipt(self) -> str:
        """Processor ipt.
        """
        return '@ipt'


    @property
    def connections(self) -> Contections:
        return Processor._Processor__contections


    @property
    def connections_count(self) -> str:
        """Processor links count.
        """
        return '@links'


    @property
    def time(self) -> str:
        """Time from start processor.
        """
        return '@time'


    @property
    def tick(self) -> str:
        """Amount of ticks from begin processor start.
        Returns:
            str: Count of ticks from begin processor start.
        """
        return '@tick'


    @property
    def map_width(self) -> str:
        """Map width.
        """
        return '@mapw'


    @property
    def map_height(self) -> str:
        """Map height.
        """
        return '@maph'


    def convert(self) -> str:
        return '@this'


    def __str__(self) -> str:
        return self.convert()
