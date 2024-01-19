from graphics import *

def drawRectangle(win,x,y,size,colour):
    tl = Point(x,y)
    br = Point (x + size, y + size)
    rectangle = Rectangle(tl,br)
    rectangle.setFill(colour)
    rectangle.draw(win)
    return rectangle

def colourSelector(x, y,width,height):
    
    colours = ["blue","orange","red","green","pink","purple"]

    hWidth = width/2
    hHeight = height/2

    if x < hWidth and y < hHeight:
        return colours[0]
    elif x >= hWidth and y < hHeight:
        return colours[1]
    elif x < hWidth and y >= hHeight:
        return colours[2]
    else:
        return colours[3]
    
def main():
    
    width = 600
    height = 300
    size = 20
    
    win = GraphWin("",width,height)

    for rows in range(0,6*size,size):
        for columns in range(0,10*size,size):
            point = win.getMouse()
            x = point.getX()
            y = point.getY()
            colour = colourSelector(x,y,width,height)
            drawRectangle(win,columns,rows,size,colour)

main()