from pyndustry.pyndustry import *
from pyndustry.graphics import *


def main():
    storage = CommandsStorage()


    jump = Jump(More('@tick', 1))
    angle = Variable('angle', 0)

    radius = Variable('radius', 0.4).jump_to(jump)

    angle += 1000
    pi = Variable('pi', 3.14159265359)

    x = Variable('x', .5)
    y = Variable('y', .5)

    a = Variable('a', (pi * 2 * angle / 360))

    x = x.sin(a) * radius
    y = y.cos(a) * radius

    x = x + 0.5 # offset to center
    y = y + 0.5 # offset to center

    display = LargeDisplay('display1')
    display.bind()
    display.clear()
    display.draw_color = Color(0, 255, 0)
    display.drawLine(x, y, .5, .5, byCoefficient=True)

    display.drawPoly(0.5, 0.5, 32, radius, isWireframe=True, byCoefficient=True)
    display.drawPoly(0.5, 0.5, 32, radius * 0.75, isWireframe=True, byCoefficient=True)
    display.drawPoly(0.5, 0.5, 32, radius * 0.5, isWireframe=True, byCoefficient=True)
    display.drawPoly(0.5, 0.5, 32, radius * 0.25, isWireframe=True, byCoefficient=True)


    print(storage.convert())
    storage.copy()


if __name__ == '__main__':
    main()