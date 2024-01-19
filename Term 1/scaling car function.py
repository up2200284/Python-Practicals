from graphics import *
from time import *


def main():
    win = GraphWin('',800,500)
    car = []

    #carTop
    xTL = 100
    yTL = 130
    wCarTop = 100
    hCarTop = 50
    colourCar = 'blue'
    diff = 30

    topLeft = Point(xTL, yTL)
    bottomRight = Point(xTL + wCarTop, yTL + hCarTop)
    carTop = Rectangle(topLeft, bottomRight )
    carTop.setFill(colourCar)
    carTop.draw(win)
    car.append(carTop)

    #carBody
    topLeft = Point(xTL-diff, yTL+hCarTop)
    bottomRight = Point(xTL + wCarTop + diff, yTL + hCarTop + hCarTop)
    carTop = Rectangle(topLeft, bottomRight )
    carTop.setFill(colourCar)
    carTop.draw(win)
    car.append(carTop)

    #left wheel
    center = Point(xTL, yTL + hCarTop + hCarTop )
    radius = hCarTop/2
    blackCircle = Circle(center,radius)
    blackCircle.setFill('black')
    blackCircle.draw(win)
    car.append(blackCircle)


    radius = radius - 10
    whiteCircle = Circle(center,radius)
    whiteCircle.setFill("white")
    whiteCircle.draw(win)
    car.append(whiteCircle)

    #right wheel
    center = Point(xTL + wCarTop, yTL + hCarTop + hCarTop )
    radius = hCarTop/2
    blackCircle = Circle(center,radius)
    blackCircle.setFill("black")
    blackCircle.draw(win)
    car.append(blackCircle)


    radius = radius - 10
    whiteCircle = Circle(center,radius)
    whiteCircle.setFill("white")
    whiteCircle.draw(win)
    car.append(whiteCircle)


    win.getMouse()

    for _ in range(1000):
        sleep(.01)
        for carPart in car:
            carPart.move(1,0)



    win.getMouse()


main()