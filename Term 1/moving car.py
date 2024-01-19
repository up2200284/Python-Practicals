from graphics import *
from time import *

def car():
    win = GraphWin("Moving Car",800,500)
    
    #road
    road = Line(Point(10, 400), Point(800, 400))
    road.draw(win)
    
    #carTop
    carTop = Rectangle(Point(120,260), Point(280,320))
    carTop.setFill("blue")
    carTop.draw(win)

    #carBody
    carBody = Rectangle(Point(70,320), Point(330,360))
    carBody.setFill("blue")
    carBody.draw(win)

    #carWheel
    carWheel = Circle(Point(130,370),30)
    carWheel.setFill("black")
    carWheel.draw(win)

    #carWheel2
    carWheel2 = Circle(Point(270,370),30)
    carWheel2.setFill("black")
    carWheel2.draw(win)
    
    #carWheely
    carWheely = Circle(Point(130,370),20)
    carWheely.setFill("white")
    carWheely.draw(win)

    #carWheely2
    carWheely2 = Circle(Point(270,370),20)
    carWheely2.setFill("white")
    carWheely2.draw(win)

    fullCar = [carTop,carBody,carWheel,carWheely,carWheel2,carWheely2]
    win.getMouse()

    for i in range(750):
        sleep(.01)
        for carPart in fullCar:
            carPart.move(1,0)
car()