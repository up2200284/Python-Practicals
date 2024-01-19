from graphics import *

def drawCircle(win,x,y,radius,colour):
    centre = Point(x,y)
    circle = Circle(centre,radius)
    circle.setFill(colour)
    circle.setOutline("black")
    circle.draw(win)
    return circle

def colourSelector(x,width):
    
    coloursFill = ["","green","blue"]

    areaWidth = width/4

    if x < areaWidth*2:
        return coloursFill[0]
    elif areaWidth*2 <= x <= areaWidth*3:
        return coloursFill[1]
    else:
        return coloursFill[2]
    
def main():
    
    width = 400
    height = 100
    radius = 10
    
    win = GraphWin("",width,height)

    for i in range(20):
            point = win.getMouse()
            x = point.getX()
            y = point.getY()
            colour = colourSelector(x,width)
            drawCircle(win,x,y,radius,colour)

    width = 400
    height = 100
    radius = 10
    
    win = GraphWin("",width,height)

    for rows in range(radius,10*radius,radius*2):
        for columns in range(radius,10*radius,radius*2):
            point = win.getMouse()
            x = point.getX()
            y = point.getY()
            colour = colourSelector(x,width)
            drawCircle(win,columns,rows,radius,colour)
main()

#4/10 was not functional at time of test!













