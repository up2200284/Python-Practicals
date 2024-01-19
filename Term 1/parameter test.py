from graphics import *

# def eyeDetail():
#     win = GraphWin("browneye",500,500)
#     centre = Point(250,250)
#     radius = 60
#     drawBrownEye(win,centre, radius)



def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


def drawBrownEye(win, centre, radius):
    drawCircle(win,centre,radius,"white")
    drawCircle(win,centre,radius-30,"brown")
    drawCircle(win,centre,radius-45,"black")

def drawPairofTwoEyes():
    win = GraphWin("browneye",500,500)
    x = 180
    y = 250
    centre = Point(x,y)
    radius = 60
    drawBrownEye(win,centre,radius)
    x= x + 120
    centre = Point(x,y)
    drawBrownEye(win,centre,radius)

    win.getMouse()

# eyeDetail()

drawPairofTwoEyes()
