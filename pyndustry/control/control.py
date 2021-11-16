from __future__ import annotations
from pyndustry import (Command, InsideCommand, Variable)
from pyndustry.graphics import (SetColor, colorByTuple)



class Sensor(Command):
    def __init__(self, value : Union(Variable, str), from_: Union(Variable, str), result : Union(Variable, str)):
        Command.__init__(self)
        self.value = value
        self.from_ = from_
        self.result = result

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'sensor {self.result} {self.from_} {self.value}'
        return value


    def to_variable(self) -> str:
        return self.result



class BaseControl(Command):
    def __init__(self, control_object : Union(Variable, str)):
        Command.__init__(self)
        self.name = 'Some control'
        self.control_object = control_object


    def convert(self) -> str:
        value = f'control {self.name} {self.control_object}'
        return value



class Enable(BaseControl):
    def __init__(self, control_object : Union(Variable, str), value : Union(Variable, str, bool)):
        BaseControl.__init__(self, control_object)
        self.name = 'enabled'

        self.value = value

        if isinstance(value, bool):
            self.value = str(value).lower()

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'control {self.name} {self.control_object} {self.value}'
        return value



class Shoot(BaseControl):
    def __init__(
            self,
            control_object : Union(Variable, str),
            x : Union(Variable, str, int, float),
            y : Union(Variable, str, int, float),
            value : Union(Variable, str, bool)
        ):
        BaseControl.__init__(self, control_object)
        self.name = 'shoot'

        self.x = x
        self.y = y
        self.value = value

        if isinstance(value, bool):
            self.value = str(value).lower()

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'control {self.name} {self.control_object} {self.x} {self.y} {self.value}'
        return value



class ShootTo(BaseControl):
    def __init__(
            self,
            control_object : Union(Variable, str),
            target : Union(Variable, str),
            value : Union(Variable, str, bool)
        ):
        BaseControl.__init__(self, control_object)
        self.name = 'shootp'

        self.target = target
        self.value = value

        if isinstance(value, bool):
            self.value = str(value).lower()

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'control {self.name} {self.control_object} {self.target} {self.value}'
        return value



class Configure(BaseControl):
    def __init__(
            self,
            control_object : Union(Variable, str),
            value : Union(Variable, str, bool)
        ):
        BaseControl.__init__(self, control_object)
        self.name = 'configure'

        self.value = value

        if isinstance(value, bool):
            self.value = str(value).lower()

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'control {self.name} {self.control_object} {self.value}'
        return value



class IlluminatorColor(BaseControl):
    def __init__(
            self,
            control_object : Union(Variable, str),
            color : Union(Color, tuple)
        ):
        BaseControl.__init__(self, control_object)
        self.name = 'color'

        self.color = color

        if isinstance(value, bool):
            self.value = str(value).lower()

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'control {self.name} {self.control_object} {self.color.r} {self.color.g} {self.color.b}'
        return value



class Radar(Command):
    def __init__(
            self,
            from_ : Union(Variable, str),
            unit_type : Union(str),
            order : Union(Variable, str, int)=1,
            order_by : Union(Variable, str)='distance',
            unit_type2 : Union(Variable, str)='any',
            unit_type3 : Union(Variable, str)='any',
            result : Union(Variable, str)='radar_result'
        ):
        Command.__init__(self)

        self.from_ = from_
        self.unit_type = unit_type
        self.order = order
        self.order_by = order_by
        self.unit_type2 = unit_type2
        self.unit_type3 = unit_type3
        self.result = result

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = (
            f'radar {self.unit_type} {self.unit_type2} {self.unit_type3} '
            f'{self.order_by} {self.from_} {self.order} {self.result}'
        )
        return value


    def to_variable(self) -> str:
        return self.result



class UnitBind(Command):
    def __init__(
            self,
            unit_name : Union(str)
        ):
        Command.__init__(self)

        self.unit_type = unit_type

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'ubind {self.unit_type}'
        return value



class BaseUnitControl(Command):
    def __init__(
            self
        ):
        Command.__init__(self)
        self.name = 'unitcontrol'

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'BaseUnitControl'
        return value



class UnitIdle(BaseUnitControl):
    def __init__(
            self
        ):
        BaseUnitControl.__init__(self)
        self.name = 'idle'

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'ucontrol {self.name}'
        return value


class UnitStop(BaseUnitControl):
    def __init__(
            self
        ):
        BaseUnitControl.__init__(self)
        self.name = 'stop'

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'ucontrol {self.name}'
        return value


class UnitMove(BaseUnitControl):
    def __init__(
            self,
            x : Union(Variable, int, float),
            y : Union(Variable, int, float),
            radius : Union(Variable, int, float)=None
        ):
        BaseUnitControl.__init__(self)
        self.name = 'move'

        self.x = x
        self.y = y
        self.radius = radius

        if radius is not None:
            self.name = 'approach'

        self._Command__add_to_storage()



    def convert(self) -> str:
        value = f'ucontrol {self.name} {self.x} {self.y} {self.radius}'
        return value



class UnitSetBoost(BaseUnitControl):
    def __init__(
            self,
            value : Union(Variable, bool)
        ):
        BaseUnitControl.__init__(self)
        self.name = 'boost'

        self.value = value

        self._Command__add_to_storage()



    def convert(self) -> str:
        value = f'ucontrol {self.name} {self.value}'
        return value



class UnitMoveToEnemySpawn(BaseUnitControl):
    def __init__(
            self,
        ):
        BaseUnitControl.__init__(self)
        self.name = 'pathfind'


        self._Command__add_to_storage()



    def convert(self) -> str:
        value = f'ucontrol {self.name}'
        return value



class UnitShoot(BaseUnitControl):
    def __init__(
            self,
            x : Union(Variable, str, int, float),
            y : Union(Variable, str, int, float),
            value : Union(Variable, str, bool)
        ):
        BaseUnitControl.__init__(self)
        self.name = 'target'

        self.x = x
        self.y = y
        self.value = value

        if isinstance(value, bool):
            self.value = str(value).lower()

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'ucontrol {self.name} {self.x} {self.y} {self.value}'
        return value



class UnitShootTo(BaseUnitControl):
    def __init__(
            self,
            target : Union(Variable, str),
            value : Union(Variable, str, bool)
        ):
        BaseUnitControl.__init__(self)
        self.name = 'targetp'

        self.target = target
        self.value = value

        if isinstance(value, bool):
            self.value = str(value).lower()

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'ucontrol {self.name} {self.target} {self.value}'
        return value



class UnitDropItem(BaseUnitControl):
    def __init__(
            self,
            target : Union(Variable, str),
            ammount : Union(Variable, str, int)
        ):
        BaseUnitControl.__init__(self)
        self.name = 'itemDrop'

        self.target = target
        self.ammount = ammount

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'ucontrol {self.name} {self.target} {self.ammount}'
        return value


class UnitDropPay(BaseUnitControl):
    def __init__(
            self
        ):
        BaseUnitControl.__init__(self)
        self.name = 'payDrop'

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'ucontrol {self.name}'
        return value



class UnitTakeItem(BaseUnitControl):
    def __init__(
            self,
            target : Union(Variable, str),
            item : Union(str),
            ammount : Union(Variable, str, int)
        ):
        BaseUnitControl.__init__(self)
        self.name = 'itemTake'


        self.target = target
        self.item = item
        self.ammount = ammount

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'ucontrol {self.name} {self.target} {self.item} {self.ammount}'
        return value



class UnitTakePay(BaseUnitControl):
    def __init__(
            self,
            take_units : (Variable, str, bool)
        ):
        BaseUnitControl.__init__(self)
        self.name = 'payTake'

        self.take_units = take_units

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'ucontrol {self.name} {self.take_units}'
        return value



class UnitMine(BaseUnitControl):
    def __init__(
            self,
            x : Union(Variable, str, int, float),
            y : Union(Variable, str, int, float),
        ):
        BaseUnitControl.__init__(self)
        self.name = 'mine'

        self.x = x
        self.y = y

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'ucontrol {self.name} {self.x} {self.y}'
        return value



class UnitSetFlag(BaseUnitControl):
    def __init__(
            self,
            value : Union(Variable, str, int),
        ):
        BaseUnitControl.__init__(self)
        self.name = 'flag'

        self.value = value

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'ucontrol {self.name} {self.value}'
        return value



class UnitBuild(BaseUnitControl):
    def __init__(
            self,
            x : Union(Variable, str, int, float),
            y : Union(Variable, str, int, float),
            block : Union(Variable, str),
            rotation : Union(Variable, str, int),
            config : Union(Variable, str)
        ):
        BaseUnitControl.__init__(self)
        self.name = 'build'

        self.x = x
        self.y = y
        self.block = block
        self.rotation = rotation
        self.config = config

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'ucontrol {self.name} {self.x} {self.y} {self.block} {self.rotation} {self.config}'
        return value



class UnitBuild(BaseUnitControl):
    def __init__(
            self,
            x : Union(Variable, str, int, float),
            y : Union(Variable, str, int, float),
            block : Union(Variable, str),
            rotation : Union(Variable, str, int),
            config : Union(Variable, str)
        ):
        BaseUnitControl.__init__(self)
        self.name = 'build'

        self.x = x
        self.y = y
        self.block = block
        self.rotation = rotation
        self.config = config

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'ucontrol {self.name} {self.x} {self.y} {self.block} {self.rotation} {self.config}'
        return value



class UnitGetBlock(BaseUnitControl):
    def __init__(
            self,
            x : Union(Variable, str, int, float),
            y : Union(Variable, str, int, float),
            block : Union(Variable, str),
            building : Union(Variable, str, bool)
        ):
        BaseUnitControl.__init__(self)
        self.name = 'getBlock'

        self.x = x
        self.y = y
        self.block = block
        self.building = building

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'ucontrol {self.name} {self.x} {self.y} {self.block} {self.building}'
        return value



class UnitGetBlock(BaseUnitControl):
    def __init__(
            self,
            x : Union(Variable, str, int, float),
            y : Union(Variable, str, int, float),
            radius : Union(Variable, str, int, float),
            result : Union(Variable, str)='unit_get_block_result'
        ):
        BaseUnitControl.__init__(self)
        self.name = 'within'

        self.x = x
        self.y = y
        self.radius = radius
        self.result = result

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'ucontrol {self.name} {self.x} {self.y} {self.radius} {self.result}'
        return value


    def to_variable(self) -> str:
        return self.result



class UnitRadar(Command):
    def __init__(
            self,
            unit_type : Union(str),
            order : Union(Variable, str, int)=1,
            order_by : Union(Variable, str)='distance',
            unit_type2 : Union(Variable, str)='any',
            unit_type3 : Union(Variable, str)='any',
            result : Union(Variable, str)='radar_result'
        ):
        Command.__init__(self)

        self.unit_type = unit_type
        self.order = order
        self.order_by = order_by
        self.unit_type2 = unit_type2
        self.unit_type3 = unit_type3
        self.result = result

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = (
            f'uradar {self.unit_type} {self.unit_type2} {self.unit_type3} '
            f'{self.order_by} 0 {self.order} {self.result}'
        )
        return value


    def to_variable(self) -> str:
        return self.result



class BaseUnitFind(Command):
    def __init__(
            self,
            out_x : Union(Variable, str)='unit_find_x',
            out_y : Union(Variable, str)='unit_find_y',
            group : Union(Variable, str)='core',
            is_enemy : Union(Variable, str, bool)=True,
            is_found : Union(Variable, str)='unit_find_is_found',
            result : Union(Variable, str)='unit_find_result'
        ):
        Command.__init__(self)

        self.name = 'find'

        self.out_x = out_x
        self.out_y = out_y
        self.group = group
        self.is_enemy = is_enemy
        self.is_found = is_found
        self.result = result

        if isinstance(is_enemy, bool):
            self.is_enemy = str(is_enemy).lower()


    def convert(self) -> str:
        value = (
            f'ulocate {self.name} {self.group} {self.is_enemy} 0 '
            f'{self.out_x} {self.out_y} {self.is_found} {self.result}'
            )
        return value


    def to_variable(self) -> str:
        return self.result



class UnitFindOre(BaseUnitFind):
    def __init__(
            self,
            value : Union(Variable, str),
            out_x : Union(Variable, str)='unit_find_x',
            out_y : Union(Variable, str)='unit_find_y',
            group : Union(Variable, str)='core',
            is_enemy : Union(Variable, str, bool)=True,
            is_found : Union(Variable, str)='unit_find_is_found',
            result : Union(Variable, str)='unit_find_result'
        ):
        BaseUnitFind.__init__(self, out_x, out_y, group, is_enemy, is_found, result)

        self.name = 'ore'
        self.value = value

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = (
            f'ulocate {self.name} {self.group} {self.is_enemy} {self.value} '
            f'{self.out_x} {self.out_y} {self.is_found} {self.result}'
            )
        return value



class UnitFindBuilding(BaseUnitFind):
    def __init__(
            self,
            out_x : Union(Variable, str)='unit_find_x',
            out_y : Union(Variable, str)='unit_find_y',
            group : Union(Variable, str)='core',
            is_enemy : Union(Variable, str, bool)=True,
            is_found : Union(Variable, str)='unit_find_is_found',
            result : Union(Variable, str)='unit_find_result'
        ):
        BaseUnitFind.__init__(self, out_x, out_y, group, is_enemy, is_found, result)

        self.name = 'building'

        self._Command__add_to_storage()



class UnitFindSpawn(BaseUnitFind):
    def __init__(
            self,
            out_x : Union(Variable, str)='unit_find_x',
            out_y : Union(Variable, str)='unit_find_y',
            group : Union(Variable, str)='core',
            is_enemy : Union(Variable, str, bool)=True,
            is_found : Union(Variable, str)='unit_find_is_found',
            result : Union(Variable, str)='unit_find_result'
        ):
        BaseUnitFind.__init__(self, out_x, out_y, group, is_enemy, is_found, result)

        self.name = 'spawn'

        self._Command__add_to_storage()



class UnitFindDamaged(BaseUnitFind):
    def __init__(
            self,
            out_x : Union(Variable, str)='unit_find_x',
            out_y : Union(Variable, str)='unit_find_y',
            group : Union(Variable, str)='core',
            is_enemy : Union(Variable, str, bool)=True,
            is_found : Union(Variable, str)='unit_find_is_found',
            result : Union(Variable, str)='unit_find_result'
        ):
        BaseUnitFind.__init__(self, out_x, out_y, group, is_enemy, is_found, result)

        self.name = 'damaged'

        self._Command__add_to_storage()
