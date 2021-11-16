from __future__ import annotations
from pyndustry import (Command, InsideCommand, Variable)



class BindDrawer(Command):
    """Binds some drawer to output draws command.

    Args:
        drawer (Union): Drawer name
    """
    def __init__(self, drawer : Union(Variable, str)):
        Command.__init__(self)
        self.drawer = drawer
        if isinstance(drawer, Variable):
            self.drawer = drawer.name

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'drawflush {self.drawer}'
        return value



class Color(InsideCommand):
    """Contain color rgba data.

    Args:
        r (float, optional): Red chanel. Defaults to 0.
        g (float, optional): Grean chanel. Defaults to 0.
        b (float, optional): Blue chanel. Defaults to 0.
        a (float, optional): Alpha chanel. Defaults to 255.
    """
    def __init__(
            self,
            r : float=0,
            g : float=0,
            b : float=0,
            a : float=255
        ):
        InsideCommand.__init__(self)

        self.r = r
        self.g = g
        self.b = b
        self.a = a


    def convert(self) -> str:
        value = f'{self.r} {self.g} {self.b} {self.a}'
        return value



def colorByTuple(value : tuple) -> Color:
    """Makes Color from tuple.

    Args:
        value (tuple): Tuple with color data.

    Returns:
        Color: Output color
    """
    color = None
    if len(value) < 4:
        color = Color(value[0], value[1], value[2])
    elif len(value) == 4:
        color = Color(value[0], value[1], value[2], value[3])
    else:
        color = Color()
    return color



class ClearColor(Command):
    """Clear display command. Default black.

    Args:
        color (Union, optional): Clear color. Defaults to Color().
    """
    def __init__(
            self,
            color : Union(Color, tuple)=Color()
        ):
        Command.__init__(self)
        self.name = 'clear'
        self.color = color
        if not isinstance(color, Color):
            self.color = colorByTuple(color)

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'draw {self.name} {self.color.r} {self.color.g} {self.color.b} {self.color.a} 0 0'
        return value



class SetColor(Command):
    """Sets current color for draw commands.

    Args:
        color (Union): New color for commands of draw.
    """
    def __init__(
            self,
            color : Union(Color, tuple)
        ):
        Command.__init__(self)
        self.name = 'color'
        self.color = color
        if not isinstance(color, Color):
            self.color = colorByTuple(color)

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'draw {self.name} {self.color.r} {self.color.g} {self.color.b} {self.color.a} 0 0'
        return value



class SetStrokeWidth(Command):
    """Sets current line width for draw commands.

    Args:
        width (Union): New width for commands of draw.
    """
    def __init__(
            self,
            width : Union(Variable, int, float)
        ):
        Command.__init__(self)
        self.name = 'stroke'
        self.width = width
        if not isinstance(width, Variable):
            self.width = width.name

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'draw {self.name} {self.width} 0 0 255 0 0'
        return value



class DrawLine(Command):
    def __init__(
            self,
            x1 : Union(Variable, int, float),
            y1 : Union(Variable, int, float),
            x2 : Union(Variable, int, float),
            y2 : Union(Variable, int, float),
            color : Union(Color, tuple)=None
        ):
        Command.__init__(self)
        self.name = 'line'
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.color = color
        if self.color is not None:
            self.color = colorByTuple(color)

        if self.color is not None:
            SetColor(self.color)
        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'draw {self.name} {self.x1} {self.y1} {self.x2} {self.y2} 0 0'
        return value



class DrawRect(Command):
    def __init__(
            self,
            x : Union(Variable, int, float),
            y : Union(Variable, int, float),
            width : Union(Variable, int, float),
            height : Union(Variable, int, float),
            isWireframe: Union(Variable, bool)=False,
            color : Union(Color, tuple)=None
        ):
        Command.__init__(self)
        self.name = 'rect'
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.isWireframe = isWireframe
        
        if isinstance(isWireframe, Variable):
            self.isWireframe = isWireframe.value
        
        if self.isWireframe:
            self.name = 'lineRect'

        self.color = color
        if not isinstance(color, Color):
            if self.color is not None:
                self.color = colorByTuple(color)

        if self.color is not None:
            SetColor(self.color)
        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'draw {self.name} {self.x} {self.y} {self.width} {self.height} 0'
        return value



class DrawPoly(Command):
    def __init__(
            self,
            x : Union(Variable, int, float),
            y : Union(Variable, int, float),
            sides : Union(Variable, int, float),
            radius : Union(Variable, int, float),
            rotation : Union(Variable, int, float)=0,
            isWireframe: Union(Variable, bool)=False,
            color : Union(Color, tuple)=None
        ):
        Command.__init__(self)
        self.name = 'poly'
        self.x = x
        self.y = y
        self.sides = sides
        self.radius = radius
        self.rotation = rotation

        self.isWireframe = isWireframe
        
        if isinstance(isWireframe, Variable):
            self.isWireframe = isWireframe.value
        
        if self.isWireframe:
            self.name = 'linePoly'

        self.color = color
        if not isinstance(color, Color):
            if self.color is not None:
                self.color = colorByTuple(color)

        if self.color is not None:
            SetColor(self.color)
        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'draw {self.name} {self.x} {self.y} {self.sides} {self.radius} {self.rotation}'
        return value



class DrawTriangle(Command):
    def __init__(
            self,
            x1 : Union(Variable, int, float),
            y1 : Union(Variable, int, float),
            x2 : Union(Variable, int, float),
            y2 : Union(Variable, int, float),
            x3 : Union(Variable, int, float),
            y3 : Union(Variable, int, float),
            isWireframe: Union(Variable, bool)=False,
            color : Union(Color, tuple)=None
        ):
        Command.__init__(self)
        self.name = 'triangle'
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

        self.isWireframe = isWireframe
        
        if isinstance(isWireframe, Variable):
            self.isWireframe = isWireframe.value
        
        if self.isWireframe:
            self.name = 'triangle'

        self.color = color
        if not isinstance(color, Color):
            if self.color is not None:
                self.color = colorByTuple(color)

        if self.color is not None:
            SetColor(self.color)
        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'draw {self.name} {self.x1} {self.y1} {self.x2} {self.y2} {self.x3} {self.y3}'
        return value



class DrawGameSprite(Command):
    def __init__(
            self,
            x : Union(Variable, int, float),
            y : Union(Variable, int, float),
            image : Union(Variable, str),
            size : Union(Variable, int, float),
            rotation : Union(Variable, int, float),
        ):
        Command.__init__(self)
        self.name = 'image'
        self.x = x
        self.y = y
        self.image = image
        self.size = size
        self.rotation = rotation

        self._Command__add_to_storage()


    def convert(self) -> str:
        value = f'draw {self.name} {self.x} {self.y} {self.image} {self.size} {self.rotation} 0'
        return value



class Display(Variable):
    """Class for easy interaction with draw commands.

    Args:
        name (Union): Display name. Example: "Display1"
    """
    def __init__(self, name : Union(Variable, str)):
        self.name = name

        self.__clear_color = Color()
        self.__width = 80
        self.__height = 80

        self.__draw_color = Color(255, 255, 255)
        self.__line_width = 1

        if isinstance(name, Variable):
            self.name = name.name
    

    @property
    def width(self) -> float:
        return self.__width
    

    @property
    def height(self) -> float:
        return self.__height
    

    @property
    def clear_color(self) -> Color:
        return self.__clear_color
    

    @clear_color.setter
    def draw_color(self, value : Union(Color, tuple)) -> None:
        self.__clear_color = value
    

    @property
    def draw_color(self) -> Color:
        return self.__draw_color
    

    @draw_color.setter
    def draw_color(self, value : Union(Color, tuple)) -> None:
        self.__draw_color = value
        SetColor(value)
    

    @property
    def line_width(self) -> float:
        return self.__line_width
    

    @line_width.setter
    def line_width(self, value : Union(Variable, int, float)) -> None:
        self.__line_width = value
        SetStrokeWidth(value)
    

    def bind(self) -> None:
        BindDrawer(self.name)
    

    def clear(self) -> None:
        ClearColor(self.__clear_color)
    
    
    def drawLine(
            self,
            x1 : Union(Variable, int, float),
            y1 : Union(Variable, int, float),
            x2 : Union(Variable, int, float),
            y2 : Union(Variable, int, float),
            byCoefficient : bool=False
        ) -> None:
            """
            Args:
                x1 (Union): Line first point x.
                y1 (Union): Line first point y.
                x2 (Union): Line second point x.
                y2 (Union): Line second point y.
                byCoefficient (bool, optional): Use positions relatively of display size. Defaults to False.
            """
            if byCoefficient:
                temp_x1 = x1 * self.width
                temp_y1 = y1 * self.height
                temp_x2 = x2 * self.width
                temp_y2 = y2 * self.height
            DrawLine(temp_x1, temp_y1, temp_x2, temp_y2)
    

    def drawRect(
        self,
        x : Union(Variable, int, float),
        y : Union(Variable, int, float),
        width : Union(Variable, int, float),
        height : Union(Variable, int, float),
        isWireframe: Union(Variable, bool)=False,
        byCoefficient : bool=False
    ) -> None:
        """
        Args:
            x (Union): Begin position x.
            y (Union): Begin position y.
            width (Union): Rectangle width.
            height (Union): Rectangle height.
            isWireframe (Union, optional): Draw only outline. Defaults to False.
            byCoefficient (bool, optional): Use positions relatively of display size. Defaults to False.
        """
        if byCoefficient:
            temp_x1 = x1 * self.width
            temp_y1 = y1 * self.height
            temp_width = width * self.width
            temp_height = height * self.height
        DrawRect(temp_x, temp_y, temp_width, temp_height, isWireframe)
    

    def drawPoly(
        self,
        x : Union(Variable, int, float),
        y : Union(Variable, int, float),
        sides : Union(Variable, int, float),
        radius : Union(Variable, int, float),
        rotation : Union(Variable, int, float)=0,
        isWireframe: Union(Variable, bool)=False,
        byCoefficient : bool=False
    ) -> None:
        """
        Args:
            x (Union): Center position x.
            y (Union): Center position y.
            sides (Union): Sides count.
            radius (Union): Radius.
            rotation (Union, optional): Poly rotation. Defaults to 0.
            isWireframe (Union, optional): Draw only outline. Defaults to False.
            byCoefficient (bool, optional): Use positions relatively of display size. Defaults to False.
        """
        if byCoefficient:
            temp_x = x * self.width
            temp_y = y * self.height
            temp_radius = radius * ((self.width + self.height) / 2)
        DrawPoly(temp_x, temp_y, sides, temp_radius, rotation, isWireframe)
    

    def drawTriangle(
        self,
        x1 : Union(Variable, int, float),
        y1 : Union(Variable, int, float),
        x2 : Union(Variable, int, float),
        y2 : Union(Variable, int, float),
        x3 : Union(Variable, int, float),
        y3 : Union(Variable, int, float),
        isWireframe: Union(Variable, bool)=False,
        byCoefficient : bool=False
    ) -> None:
        if byCoefficient:
            temp_x1 = x1 * self.width
            temp_y1 = y1 * self.height
            temp_x2 = x2 * self.width
            temp_y2 = y2 * self.height
            temp_x3 = x3 * self.width
            temp_y3 = y3 * self.height
        DrawTriangle(temp_x1, temp_y1, temp_x2, temp_y2, temp_x3, temp_y3, isWireframe)
    

    def drawGameSprite(
        self,
        x : Union(Variable, int, float),
        y : Union(Variable, int, float),
        image : Union(Variable, str),
        size : Union(Variable, int, float)=32,
        rotation : Union(Variable, int, float)=0,
        byCoefficient : bool=False
    ) -> None:
        """
        Args:
            x (Union): Center position x.
            y (Union): Center position y.
            image (Union): Sprite name. Example "@router".
            size (Union): Sprite size.
            rotation (Union, optional): Sprite rotation. Defaults to 0.
            isWireframe (Union, optional): Draw only outline. Defaults to False.
            byCoefficient (bool, optional): Use positions relatively of display size. Defaults to False.
        """
        if byCoefficient:
            temp_x = x * self.width
            temp_y = y * self.height
        DrawGameSprite(temp_x, temp_y, image, size, rotation)


    def to_variable(self) -> str:
        return self.name



class LargeDisplay(Display):
    """Display just only large.
    """
    def __init__(self, name : Union(Variable, str)):
        Display.__init__(self, name)

        self.__width = 176
        self.__height = 176


    @property
    def width(self) -> float:
        return self.__width
    

    @property
    def height(self) -> float:
        return self.__height
