from graphics import *
#win = GraphWin("Graphics Window", 400, 300)
#p = Point(200, 150)
#p.setOutline("red")
#input()

def diningTable():
    win = GraphWin("My window", 400, 400)
    
    table = Rectangle(Point(50,100), Point(350,300))
    table.draw(win)
    
    plate1 = Circle(Point(130,130), 20)
    plate1.draw(win)
    plate2 = Circle(Point(270,130), 20)
    plate2.draw(win)
    input()
diningTable()