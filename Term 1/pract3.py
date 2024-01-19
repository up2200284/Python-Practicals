from graphics import *
from math import *

def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    armOne = Line(Point(100,100), Point(130,100))
    armOne.draw(win)
    armTwo = Line(Point(100,100), Point(70,100))
    armTwo.draw(win)
    feetOne = Line(Point(100,120), Point(120, 160))
    feetOne.draw(win)
    feetTwo = Line(Point(100,120), Point(80, 160))
    feetTwo.draw(win)


def drawCircle():
    rad = float(input("Enter Radius Value: "))
    winTwo = GraphWin("Circle")
    circle = Circle(Point(100, 60), rad)
    circle.draw(winTwo)

def drawArcheryTarget():
    winThree = GraphWin("Circle",500, 500)
    
    circle = Circle(Point(250, 250),30)
    circle.draw(winThree)
    circle.setFill("blue")
    
    circleTwo = Circle(Point(250, 250),20)
    circleTwo.setFill("red")
    circleTwo.draw(winThree)
    
    circleThree = Circle(Point(250, 250),10)
    circleThree.setFill("yellow")
    circleThree.draw(winThree)

def drawRectangle():
    h1 = float(input("Enter Height value : "))
    w1 = float(input("Enter Width value : "))
    winFour = GraphWin("Rectangle")
    rectangle = Rectangle(Point(100-float(h1)/2,100-float(w1)/2), Point(100+float(h1)/2,100+float(w1)/2))
    rectangle.draw(winFour)
    winFour.getMouse()

def blueCircle():
    winFive = GraphWin("blueCircles")
    radius = 50
    circle = Circle(winFive.getMouse(), radius)
    
    circle.setFill("Blue")
    circle.draw(winFive)
    
def tenLines():
    win = GraphWin("Line drawer")
    for i in range(10):
        message = Text(Point(100, 100), "Click on first point")
        message.draw(win)
        p1 = win.getMouse()
        message.setText("Click on second point")
        p2 = win.getMouse()
        line = Line(p1, p2)
        line.draw(win)
        message.setText("")
        
def tenStrings():
    win = GraphWin("Ten Strings", 500, 500)
    text = Entry(Point(100,20),5)
    text.draw(win)
    
    for i in range(10):
        point = win.getMouse()
        message = Text(point, text.getText())
        message.draw(win)
        text.setText("")

def tenColouredRectangles():
    win = GraphWin("Ten Coloured Rectangles")
    text = Entry(Point(100, 20), 5)
    text.setText("blue")
    text.draw(win)
    for _ in range(10):
        point1 = win.getMouse()
        point2 = win.getMouse()
        rectangle = Rectangle(point1, point2)
        rectangle.setFill(text.getText())
        rectangle.draw(win)
        
def fiveClickStickFigure():
    win = GraphWin("stick boi",500,500)
    
    userInstructions = Text(Point(250,20),"Click five times to draw the stickman")
    userInstructions.draw(win)
    p1 = win.getMouse()
    p2 = win.getMouse()
    circleX = (p2.getX()-p1.getX())**2
    circleY = (p2.getY()-p1.getY())**2
    circleRad = sqrt(circleX+circleY)
    #formula for radius from two co-ordinates squareroot((x2-x1)**2 +(y2-y1)**2)  = radius
    head = Circle((p1), circleRad)
    head.draw(win)
    
    p3 = win.getMouse()
    body = Line(Point(p1.getX(), p1.getY() + circleRad),p3)
    body.draw(win)
    userInstructions.setText("Click to Close.")

    p4 = win.getMouse()
    arm = Line(Point(p3.getX(), p3.getY() - (p3.getY() - (p1.getY() + circleRad))/2),p4)
    arm.draw(win)


    armOpposite = Line(Point((p4.getX() - (p4.getX() - (p3.getX()))/2), p3.getY() - (p3.getY() - (p1.getY() + circleRad))/2),p4)
    armOpposite.draw(win)


   # print(p3.getY())
    #print(p1.getY() + circleRad)
    #print(p3.getY() - (p1.getY() + circleRad))
    #print((p3.getY() - (p1.getY() + circleRad))/2)
    #print(p3.getY() - (p3.getY() - (p1.getY() + circleRad))/2)
    print(p3.getX())
    print(p4.getX())
    print(p4.getX() - p3.getX())
    print((p4.getX() - (p3.getX()))/2)
    print((p4.getX() - (p4.getX() - (p3.getX()))/2))

fiveClickStickFigure()

