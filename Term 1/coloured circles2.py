from graphics import *

def drawCircle(win,x,y,size,colour):
    centre = Point(x,y)
    circle = Circle(centre,size)
    circle.setFill(colour)
    circle.draw(win)
    return circle

def colourSelector(x, y,width,height):
    
    colours = ["blue","orange","red","green","pink","purple"]

    hWidth = width/3
    hHeight = height/2

    if x < hWidth and y < hHeight:
        return colours[0]
    elif x >= hWidth and x < 400 and y < hHeight:
        return colours[1]
    elif x >= 400 and y < hHeight:
        return colours[2]
    elif x < hWidth and y >= hHeight:
        return colours[3]
    elif x >= 200 and x < 400 and y >= hHeight:
        return colours[4]
    elif x >= 400 and y >= hHeight:
        return colours[5]
    
def main():
    
    width = 600
    height = 300
    size = 20
    
    win = GraphWin("",width,height)

    for rows in range(20,6*size,size):
        for columns in range(20,10*size,size):
            point = win.getMouse()
            x = point.getX()
            y = point.getY()
            colour = colourSelector(x,y,width,height)
            drawCircle(win,columns,rows,size,colour)

main()