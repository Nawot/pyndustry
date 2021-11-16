from __future__ import annotations
import pyperclip


class CommandsStorage(object):
    '''Contain of all commands for next output to mindustry logic.'''
    __commands = []
    __current_line = 1
    __runtime_current_line = 1 - 2


    def __init__(self):
        pass


    @staticmethod
    def add_command(command : Command) -> None:
        """Adds command to storage. Why I write it, It's sholde be obvious?

        Args:
            command (Command): One more command.
        """
        CommandsStorage.__commands.append(command)
        CommandsStorage.__runtime_current_line += 1


    @staticmethod
    def get_line_count() -> int:
        """
        Returns:
            int: Total commands count
        """
        return len(CommandsStorage.__commands)


    @staticmethod
    def get_current_line_num() -> int:
        """Line num of last added command when it final converting to str.

        Note:
            Useful inside a function of converting command to str.
        
        Example::
            storage = CommandsStorage()

            a = SomeCommand(args)
            b = SomeCommand(args)
            storage.get_runtime_current_line_num() # return 1
            c = SomeCommand(args)

        Returns:
            int: Line num
        """
        return CommandsStorage.__current_line


    @staticmethod
    def get_runtime_current_line_num() -> int:
        """Line num of last added command when commands added.

        Example::
            storage = CommandsStorage()

            a = SomeCommand(args)
            b = SomeCommand(args)
            storage.get_runtime_current_line_num() # return 2
            c = SomeCommand(args)

        Returns:
            int: Line num
        """
        return CommandsStorage.__runtime_current_line
    

    @staticmethod
    def copy() -> None:
        """Copy final converting of commands to clipboard.
        """
        pyperclip.copy(CommandsStorage.convert())


    @staticmethod
    def convert() -> str:
        """Converting all commands to final string.

        Returns:
            str: Final string.
        """
        result = ''
        for command in CommandsStorage.__commands:
            result += command.convert() + '\n'
            CommandsStorage.__current_line += 1
        result = result[:-1] # Remove last line break.
        return result


    def __str__(self) -> str:
        return self.convert()



class Command(object):
    """Base command class.
    """
    def __init__(self):
        Function._Function__func_lines += 1


    def convert(self) -> str:
        """Convert command to mindustry logic command.

        Returns:
            str: String of mindustry logic command.
        """
        return 'Command'


    def to_variable(self) -> str:
        """
        Returns:
            str: Variable name
        """
        return 'result'


    def __add_to_storage(self) -> None:
        CommandsStorage.add_command(self)


    def jump_to(self, jump: Jump) -> self:
        """Jump command now jump to this command.

        Args:
            jump (Jump): Some prev defined jamp command.

        Returns:
            self: Itself command for next actions.
        """
        jump.to = CommandsStorage.get_runtime_current_line_num()
        return self


    def __str__(self) -> str:
        return self.to_variable()



class InsideCommand(object):
    def __init__(self):
        pass


    def convert(self) -> str:
        """Convert inside command to inside command of mindustry logic.

        Returns:
            str: String of mindustry logic inside command.
        """
        return 'InsideCommand'


    def __str__(self) -> str:
        return self.convert()


# TODO: Make more override methods
class Variable(Command):
    """Mindustry variable and functions related with variable.

    Args:
        str name: Variable name.
        Variable, str int, float, bool value: Variable value.
    """
    def __init__(self, name : str, value : Union(Variable, int, float, str, bool)=None):
        Command.__init__(self)
        self.name = name
        self.value = value
        # For previously identified variable. To not make excess command.
        if self.value is not None:
            if isinstance(value, Variable):
                self.value = value.name
            self._Command__add_to_storage()


    def convert(self) -> str:
        """Convert command to mindustry logic command.

        Returns:
            str: String of mindustry logic command.
        """
        value = f'set {self.name} {self.value}'
        return value


    def to_variable(self) -> str:
        """
        Returns:
            str: Variable name
        """
        return self.name


    # +=
    def __iadd__(self, value) -> self:
        Operation(Plus(self, value))
        return self


    # +
    def __add__(self, value) -> self:
        result = f'{self.name}_add'
        Operation(Plus(self, value, result=result))
        return Variable(result)


    # -=
    def __isub__(self, value) -> self:
        Operation(Minus(self, value))
        return self


    # -
    def __sub__(self, value) -> self:
        result = f'{self.name}_add'
        Operation(Minus(self, value, result=result))
        return Variable(result)


    # *=
    def __imul__(self, value) -> self:
        Operation(Multiply(self, value))
        return self


    # *
    def __mul__(self, value) -> Variable:
        result = f'{self.name}_mul'
        Operation(Multiply(self, value, result=result))
        return Variable(result)


    # /=
    def __itruediv__(self, value) -> self:
        Operation(Divide(self, value))
        return self


    # /
    def __truediv__(self, value) -> Variable:
        result = f'{self.name}_div'
        Operation(Divide(self, value, result=result))
        return Variable(result)


    # //=
    def __ifloordiv__(self, value) -> self:
        Operation(FloorDivide(self, value))
        return self
    

    # //
    def __floordiv__(self, value) -> Variable:
        result = f'{self.name}_fdiv'
        Operation(FloorDivide(self, value, result=result))
        return Variable(result)
    

    # %=
    def __imod__(self, value) -> self:
        Operation(Mod(self, value))
        return self
    

    # %
    def __mod__(self, value) -> Variable:
        result = f'{self.name}_mod'
        Operation(Mod(self, value, result=result))
        return Variable(result)
    

    # **=
    def __ipow__(self, value) -> self:
        Operation(Pow(self, value))
        return self


    # **
    def __ipow__(self, value) -> Variable:
        result = f'{self.name}_pow'
        Operation(Pow(self, value, result=result))
        return Variable(result)


    def sin(self, value) -> self:
        Operation(Sin(self, value))
        return self


    def cos(self, value) -> self:
        Operation(Cos(self, value))
        return self


    # <
    def __lt__(self, value) -> str:
        return Less(self, value)


    # <=
    def __le__(self, value) -> str:
        return LessOrEqual(self, value)


    # >
    def __gt__(self, value) -> str:
        return More(self, value)


    # >=
    def __ge__(self, value) -> str:
        return MoreOrEqual(self, value)


    # ==
    def __eq__(self, value) -> str:
        return Equal(self, value)


    # !=
    def __ne__(self, value) -> str:
        return NotEqual(self, value)



class Operation(Command):
    """Operation with variable such as: + - * / and etc.
    If the operation is special class that values takes from it.

    Args:
        operation (Union): Operation type such as: + - * / and etc.
        value1 (Union, optional): left value. Defaults to None.
        value2 (Union, optional): right value. Defaults to None.
        result (Union, optional): result variable. Defaults to None.
        
    """
    def __init__(
            self,
            operation: Union(AssignmentOperator, MathFunc, str),
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None,
            result: Union(Variable, str)=None
        ):
        Command.__init__(self)

        self.operation = operation
        self.result = result

        if value1 is not None:
            self.value1 = value1
        if value2 is not None:
            self.value2 = value2
        
        self._Command__add_to_storage()
    

    def convert(self) -> str:
        """Convert command to mindustry logic command.

        Returns:
            str: String of mindustry logic command.
        """
        value = ''
        if not isinstance(self.operation, InsideCommand):
            value = (
                f'op {self.operation} {self.result} '
                f'{self.value1} {self.value2}')
        else:
            value = f'op {self.operation}'
        return value


    def to_variable(self) -> str:
        """
        Returns:
            str: Result variable name
        """
        return self.result



class MathFunc(InsideCommand):
    """Base class for math operation.
    """
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None
        ):
        InsideCommand.__init__(self)
        self.name = 'MathFunc'
        self.value1 = value1
        self.value2 = value2


    def convert(self) -> str:
        """Convert command to mindustry logic command.

        Returns:
            str: String of mindustry logic command.
        """
        a = 'op sin result a b'
        value = f'{self.name} {self.value1} {self.value2}'
        return value
        



class Sin(MathFunc):
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None
        ):
        MathFunc.__init__(self, value1, value2)
        self.name = 'sin'



class Cos(MathFunc):
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None
        ):
        MathFunc.__init__(self, value1, value2)
        self.name = 'cos'



class AssignmentOperator(InsideCommand):
    """Base class for assignment operators such as: + - * / and etc.
    """
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None,
            result : Union(Variable, str)=None
        ):
        InsideCommand.__init__(self)
        self.name = 'AssignmentOperator'
        self.value1 = value1
        self.value2 = value2
        if result is not None:
            self.result = result
        else:
            self.result = self.value1


    def convert(self) -> str:
        """Convert command to mindustry logic command.

        Returns:
            str: String of mindustry logic command.
        """
        value = f'{self.name} {self.result} {self.value1} {self.value2}'
        return value


    def to_variable(self) -> str:
        """
        Returns:
            str: Result variable name
        """
        return self.result



class Plus(AssignmentOperator):
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None,
            result : Union(Variable, str)=None
        ):
        AssignmentOperator.__init__(self, value1, value2, result=result)
        self.name = 'add'



class Minus(AssignmentOperator):
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None,
            result : Union(Variable, str)=None
        ):
        AssignmentOperator.__init__(self, value1, value2, result=result)
        self.name = 'sub'



class Multiply(AssignmentOperator):
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None,
            result : Union(Variable, str)=None
        ):
        AssignmentOperator.__init__(self, value1, value2, result=result)
        self.name = 'mul'



class Divide(AssignmentOperator):
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None,
            result : Union(Variable, str)=None
        ):
        AssignmentOperator.__init__(self, value1, value2, result=result)
        self.name = 'div'



class FloorDivide(AssignmentOperator):
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None,
            result : Union(Variable, str)=None
        ):
        AssignmentOperator.__init__(self, value1, value2, result=result)
        self.name = 'idiv'



class Mod(AssignmentOperator):
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None,
            result : Union(Variable, str)=None
        ):
        AssignmentOperator.__init__(self, value1, value2, result=result)
        self.name = 'mod'



class Pow(AssignmentOperator):
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None,
            result : Union(Variable, str)=None
        ):
        AssignmentOperator.__init__(self, value1, value2, result=result)
        self.name = 'pow'



class ComparisonOperator(InsideCommand):
    """Base class for comparison operators such as: < > == != and etc.
    """
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None
        ):
        InsideCommand.__init__(self)
        self.name = 'ComparisonOperator'
        self.value1 = value1
        self.value2 = value2


    def inverse(self) -> ComparisonOperator:
        return ComparisonOperator(self.value1, self.value2)


    def convert(self) -> str:
        value = f'{self.name} {self.value1} {self.value2}'
        return value



class Less(ComparisonOperator):
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None
        ):
        ComparisonOperator.__init__(self, value1, value2)
        self.name = 'lessThan'


    def inverse(self) -> ComparisonOperator:
        return More(self.value1, self.value2)



class LessOrEqual(ComparisonOperator):
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None
        ):
        ComparisonOperator.__init__(self, value1, value2)
        self.name = 'lessThanEq'


    def inverse(self) -> ComparisonOperator:
        return MoreOrEqual(self.value1, self.value2)



class More(ComparisonOperator):
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None
        ):
        ComparisonOperator.__init__(self, value1, value2)
        self.name = 'greaterThan'


    def inverse(self) -> ComparisonOperator:
        return Less(self.value1, self.value2)



class MoreOrEqual(ComparisonOperator):
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None
        ):
        ComparisonOperator.__init__(self, value1, value2)
        self.name = 'greaterThanEq'


    def inverse(self) -> ComparisonOperator:
        return LessOrEqual(self.value1, self.value2)



class Equal(ComparisonOperator):
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None
        ):
        ComparisonOperator.__init__(self, value1, value2)
        self.name = 'equal'


    def inverse(self) -> ComparisonOperator:
        return NotEqual(self.value1, self.value2)



class NotEqual(ComparisonOperator):
    def __init__(
            self,
            value1 : Union(Variable, int, float, str, bool)=None,
            value2 : Union(Variable, int, float, str, bool)=None
        ):
        ComparisonOperator.__init__(self, value1, value2)
        self.name = 'notEqual'


    def inverse(self) -> ComparisonOperator:
        return Equal(self.value1, self.value2)



class Always(ComparisonOperator):
    def __init__(self):
        pass


    def inverse(self) -> ComparisonOperator:
        return Never() 


    def convert(self) -> str:
        value = 'always x false'
        return value



class Never(ComparisonOperator):
    def __init__(self):
        pass

    
    def inverse(self) -> ComparisonOperator:
        return Always() 


    def convert(self) -> str:
        value = 'strictEqual False False'
        return value



class BindPrinter(Command):
    """Binds some printer to output print command.

    Args:
        printer (Union): Printer name
    """
    def __init__(self, printer : Union(Variable, str)):
        Command.__init__(self)
        self.printer = printer

        self._Command__add_to_storage()


    def convert(self) -> str:
        """Convert command to mindustry logic command.

        Returns:
            str: String of mindustry logic command.
        """
        value = f'printflush {self.printer}'
        return value
    

    def to_variable(self) -> str:
        """
        Returns:
            str: Printer variable name
        """
        return self.printer



class Mprint(Command):
    """Print command. Prints message to current bind brinter.

    Args:
        value (Union): Message.
        printer (Union): Printer. Defaults to None.
    """
    def __init__(
            self,
            value : Union(Variable, int, float, str, bool),
            printer : Union(Variable, str)=None):
        Command.__init__(self)

        self.printer = printer
        self.value = value
        if isinstance(value, str):
            self.value = f'"{value}"'
        if self.printer is not None:
            BindPrinter(self.printer)

        self._Command__add_to_storage()


    def convert(self) -> str:
        """Convert command to mindustry logic command.

        Returns:
            str: String of mindustry logic command.
        """
        value = f'print {self.value}'
        return value
    
    def to_variable(self) -> str:
        """
        Returns:
            str: Result variable name
        """
        return self.value



class Jump(Command):
    """Jump command. Makes jump if condition return True.

    Args:
        condition (Union): Condition command such as < > == != and etc.
    """
    def __init__(self, condition : Union(str, bool)):
        Command.__init__(self)
        self.__condition = condition
        if isinstance(self.__condition, bool):
            if self.__condition:
                self.__condition = Always()
            else:
                self.__condition = Never()
        self.to = -1

        self._Command__add_to_storage()


    def jump_to(self) -> self:
        """Jump to self line.
        """
        self.to = CommandsStorage.get_runtime_current_line_num() + 1
        return self


    def convert(self) -> str:
        """Convert command to mindustry logic command.

        Returns:
            str: String of mindustry logic command.
        """
        value = f'jump {self.to} {self.__condition}'
        return value



class Mif():
    """The if work on jumps.

    Args:
        str, bool condition: This is a condition from variable comparison operators.
        Function function: Function with commands
    """
    def __init__(
            self,
            condition : Union(str, bool),
            function : Function):
        self.__condition = condition
        self.__function = function

        self.__previousNode = None
        self.__nextNode = None

        self.__jumpIf = None
        self.__jumpElse = None


    def melse(self, function) -> Melse:
        """Makes Melse Command. It doing some of staff if result of if contition not True.

        Args:
            Function function: Function with commands

        Returns:
            Melse: This is melse class
        """
        self.__nextNode = Melse(self, function)
        return self.__nextNode


    def melif(self, condition, function) -> Melif:
        """Makes Melif Command. It doing some of staff if result of if contition not True ans self if return True.

        Args:
            str, bool condition: This is a condition from variable comparison operators.
            Function function: Function with commands

        Returns:
            Melif: This is melif class
        """
        self.__nextNode = Melif(self, condition, function)
        return self.__nextNode


    def _back_apply(self) -> None:
        if self.__previousNode is not None:
            self.__previousNode._back_apply()

        self.__jumpIf = Jump(self.__condition)


    def _front_apply(self) -> None:
        self.__jumpElse = Jump(True)
        self.__function.jump_to_end(self.__jumpIf)
        self.__function.execute()
        if self.__previousNode is not None:
            self.__previousNode._front_apply()

        self.__function.jump_to_end(self.__jumpElse)


    def apply(self) -> None:
        """Creates jumps from nodes if elif else.
        """
        self.__jumpIf = Jump(self.__condition)

        if(self.__previousNode is not None):
            self._back_apply()

        self._front_apply()



class Melse(Mif):
    def __init__(
            self,
            previousNode : Union(Mif, Melif),
            function : Function):
        self.__previousNode = previousNode
        self.__function = function


    def _back_apply(self) -> None:
        if self.__previousNode is not None:
            self.__previousNode._back_apply()


    def _front_apply(self) -> None:
        self.__function.execute()
        if self.__previousNode is not None:
            self.__previousNode._front_apply()


    def apply(self) -> None:
        """Creates jumps from nodes if elif else.
        """
        if(self.__previousNode is not None):
            self._back_apply()

        self._front_apply()



class Melif(Mif):
    def __init__(
            self,
            previousNode : Union(Mif, Melif),
            condition : Union(str, bool),
            function : Function):
        self.__previousNode = previousNode
        self.__nextNode = None

        self.__condition = condition
        self.__function = function

        self.__jumpIf = None
        self.__jumpElse = None


    def melse(self, function) -> Melse:
        """Makes Melse Command. It doing some of staff if result of if contition not True.

        Args:
            Function function: Function with commands

        Returns:
            Melse: This is melse class
        """
        self.__nextNode = Melse(self, function)
        return self.__nextNode


    def melif(self, condition, function) -> Melif:
        """Makes Melif Command. It doing some of staff if result of if contition not True ans self if return True.

        Args:
            str, bool condition: This is a condition from variable comparison operators.
            Function function: Function with commands

        Returns:
            Melif: This is melif class
        """
        self.__nextNode = Melif(self, condition, function)
        return self.__nextNode


    def _back_apply(self) -> None:
        if self.__previousNode is not None:
            self.__previousNode._back_apply()

        self.__jumpIf = Jump(self.__condition)


    def _front_apply(self) -> None:
        self.__jumpElse = Jump(True)
        self.__function.jump_to_end(self.__jumpIf)
        self.__function.execute()
        if self.__previousNode is not None:
            self.__previousNode._front_apply()

        self.__function.jump_to_end(self.__jumpElse)


    def apply(self) -> None:
        """Creates jumps from nodes if elif else.
        """
        if(self.__previousNode is not None):
            self._back_apply()

        self._front_apply()



class Function():
    """Contain lambda with logic.
    """
    __func_lines = 0

    
    def __init__(self, function):
        self.__function = function


    def jump_to_end(self, jump: Jump) -> self:
        """Creates Jump command to last line of function.

        Args:
            jump (Jump): Some prev defined jamp command.

        Returns:
            self: Itself command for next actions.
        """
        jump.to = CommandsStorage.get_runtime_current_line_num() + 1
        return self


    def execute(self) -> None:
        """Executes all commands contain with itself.
        """
        Function.__func_lines = 0
        self.__function()


    def getFuncLines(self) -> int:
        return Function.__func_lines



class End(Command):
    """Just end command.
    """
    def __init__(self):
        Command.__init__(self)
        self._Command__add_to_storage()


    def convert(self) -> str:
        """Convert command to mindustry logic command.

        Returns:
            str: String of mindustry logic command.
        """
        value = f'end'
        return value
