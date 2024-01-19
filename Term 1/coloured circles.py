from graphics import *

def drawCircle(win,x,y,size,colour,colourTwo):
    centre = Point(x,y)
    circle = Circle(centre,size)
    circle.setFill(colour)
    circle.setOutline(colourTwo)
    circle.draw(win)
    return circle

def colourSelector(x, y,width,height):
    
    coloursFill = ["blue","orange","red","green"]

    hWidth = width/2
    hHeight = height/2

    if x < hWidth and y < hHeight:
        return coloursFill[0]
    elif x >= hWidth and y < hHeight:
        return coloursFill[1]
    elif x < hWidth and y >= hHeight:
        return coloursFill[2]
    else:
        return coloursFill[3]
    
def colourOutline(x,y,width,height):
    coloursOutline = ["red","grey","brown","black"]

    hWidth = width/2
    hHeight = height/2

    if x < hWidth and y < hHeight:
        return coloursOutline[0]
    elif x >= hWidth and y < hHeight:
        return coloursOutline[1]
    elif x < hWidth and y >= hHeight:
        return coloursOutline[2]
    else:
        return coloursOutline[3]
def partOne():
    
    width = 600
    height = 300
    size = 20
    
    win = GraphWin("",width,height)
    for i in range(5):
        point = win.getMouse()
        x = point.getX()
        y = point.getY()
        colour = colourSelector(x,y,width,height)
        colourTwo = colourOutline (x,y,width,height)
        drawCircle(win,x,y,size,colour,colourTwo)
partOne()

def partTwo():

    width = 600
    height = 300
    size = 20
    
    win = GraphWin("",width,height)
    for rows in range(size,6*size,size*2):
        for columns in range(size,10*size,size*2):
            point = win.getMouse()
            x = point.getX()
            y = point.getY()
            colour = colourSelector(x,y,width,height)
            colourTwo = colourOutline (x,y,width,height)
            drawCircle(win,columns,rows,size,colour,colourTwo)
partTwo()