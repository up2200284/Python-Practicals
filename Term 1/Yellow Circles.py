from graphics import *


def clickToClose(win):
    win.getMouse()
    win.close()

def drawRectangle(win):
    
    tlPoint = win.getMouse()#Point(100,100)
    brPoint = win.getMouse()#Point(300,200)

    rec = Rectangle(tlPoint,brPoint)
    rec.setFill("red")
    rec.draw(win)

def drawLine(win):

    p1 = win.getMouse()
    p2 = win.getMouse()

    l = Line(p1,p2)

    l.setFill("red")

    l.draw(win)

def drawCircle(win):

    centre = win.getMouse()
    radius = 50
    
    cir = Circle(centre,radius)

    cir.setFill("Blue")
    cir.draw (win)


def main():
    width = int(input("width: "))
    height = int(input("height: "))
    win = GraphWin("sad face", width, height)#Title, width, height

    for i in range(5):
       drawRectangle(win)
       drawCircle(win)
       drawLine(win)
    
    clickToClose(win)


###############################EXECUTE MAIN#############################################
main()
