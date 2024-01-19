import math
from graphics import *

def fastFoodOrderPrice():
    orderCost = float(input("Enter cost: "))
    if orderCost>=20:
        orderCost += 2.50
    print(f"The total price of your order is £{orderCost:.2f}")
#fastFoodOrderPrice()

def whatToDoToday():
    userTemp = float(input("Enter temperature of today: "))
    if userTemp > 25:
        print("a swim in the sea is recommended")
    elif 10 <= userTemp <= 25:
        print("shopping in Gunwharf Quays is a good idea")
    else:
        print ("it's best to watch a film at home")
#whatToDoToday()

def displaysquareRoots(start,end):
    for i in range(start,end+1):
        print(f"The square root of {i} is,{math.sqrt(i):.3f}")
#displaysquareRoots(2,4)

def calculateGrade(mark):
    grade = ("ABCFX")
    if 16<=mark<= 20:
        return (grade[0])
    elif 12 <= mark <= 15:
        return(grade[1])
    elif 8 <= mark <= 11:
        return(grade[2])
    elif 8 > mark:
        return(grade[3])
    else:
        return (grade[4])
#calculateGrade(6)

def peasInAPod():
    x = 50
    peaNumb = int(input("Enter number of peas: "))
    windowSize = peaNumb * 100
    win = GraphWin("peas",windowSize,100)
    # peas = []
    for i in range(peaNumb):
        circle = Circle(Point(x,50),50)
        circle.setOutline("green")
        circle.setFill("green")
        # peas.append(circle)
        circle.draw(win)
        x += 100
    # option = int(input("select a circle to remove 1, 2, 3,..."))
    # peas[option-1].undraw()
    win.getMouse()
# peasInAPod()

def ticketPrice(distance,age):
    ticketPrice = float((distance * 0.15) + 10)
    if 15 >= age or age >= 60:
        ticketPrice = ticketPrice * 0.40
    ticketPrice = (f"£{ticketPrice:.2f}")
    return ticketPrice
#ticketPrice(100,60)

def numberedSquare(n):
    for i in range(n,0,-1):
        for x in range(n):
            print(i+x, end= ' ')
        print() # when print is an empty = print(end = "\n")
#numberedSquare(4)
# win = GraphWin("colouredEye",400,400)
# centre = Point(200,200)
# radius = 50
# colour = "blue"

def drawColouredEye(win, centre, radius, colour):
    circle = Circle(centre,radius)
    circle.setFill(colour)
    circle.draw(win)
#drawColouredEye(win,centre,radius,colour)

def eyePicker():
    x = float(input("Enter x co-ordinates: "))
    y = float(input("Enter y co-ordinates: "))
    radius = float(input("Enter radius of a circle: "))
    colour = input("Enter a colour: ")
    circle = Circle(Point(x,y),radius)
    validColour = ["blue","grey","green","brown"]
    if colour not in validColour:
        print("not valid colour")
        return
    if x > 400 or y > 400:
        print("eye centre is not in window")
        return
    win = GraphWin("eyePicker",400,400)
    circle.setFill(colour)
    circle.draw(win)
#eyePicker()

def drawPatchWindow():
    x = 35
    y = 35
    radius = 35
    win = GraphWin("patch4",100,100)
    for i in range(7):
        circle = Circle(Point(x+15,y+30),radius)
        circle.setOutline("red")
        circle.draw(win)
        y += 5
        radius -=5
    win.getMouse()
# drawPatchWindow()

#win = GraphWin("patch")

def drawPatch(win,x,y,colour):
    radius = 5
    for i in range(7):
        circle = Circle(Point(x,y),radius)
        circle.setOutline(colour)
        circle.draw(win)
        y -= 5
        radius +=5
# drawPatch(win,35,65,"blue")

def drawPatchWork():
    x = 35
    y = 65
    win = GraphWin("patchwork",300,200)
    for rows in range(x,6*x,x*2):
        for columns in range(y,10*y,y*2):
            drawPatch(win,x,y,"blue")
            x += 75
        y += 75
        win.getMouse()
drawPatchWork()
