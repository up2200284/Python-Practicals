import math
from graphics import *

win = GraphWin("browneye",500,500)
centre = Point(330,250)
radius = 60

def greet(name):
    return f"Hello, {name}!"


def product(a, b):
    return a * b


def divide(a, b):
    return a / b


def divdeAndProduct(a, b):
    productResult = product(a, b)
    divideResult = divide(a, b)
    return productResult, divideResult


def main():
    myName = input("What is your name? ")
    greeting = greet(myName)
    print(greeting)

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    productResult, divideResult = divdeAndProduct(num1, num2)
    print(f"{num1} * {num2} = {productResult}")
    print(f"{num1} / {num2} = {divideResult}")


def calcFutureValue(amount, years):
    interestRate = 0.065
    for year in range(years):
        amount = amount * (1 + interestRate)
    return amount


def futureValue():
    amount = float(input("Enter an amount to invest: "))
    years = int(input("Enter the number of years: "))
    final = calcFutureValue(amount, years)

    output = f"Investing £{amount:0.2f} for {years} years "
    output += f"results in £{final:0.2f}."
    print(output)


# For exercises 1 and 2
def areaOfCircle(radius):
    return math.pi * radius ** 2


# For exercise 3
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

def drawBrownEyeInCentre():
    win = GraphWin("browneye",500,500)
    drawCircle(win,Point(250,250),60,"white")
    drawCircle(win,Point(250,250),30,"brown")
    drawCircle(win,Point(250,250),15,"black")
    win.getMouse()

def drawBrownEye(win, centre, radius):
    drawCircle(win,centre,radius,"white")
    drawCircle(win,centre,radius-30,"brown")
    drawCircle(win,centre,radius-45,"black")
#drawBrownEye(win,centre,radius)

def drawPairOfBrownEyes():
    drawBrownEye(win,centre,radius)
    newCenter = Point(centre.getX() - 120, centre.getY())
    drawBrownEye(win,newCenter,radius)
    win.getMouse()
drawPairOfBrownEyes()

def circumferenceOfCircle(radius):
    return math.pi * radius * 2

def circleInfo():
    radius = float(input("Enter radius value "))
    areaOfCircle(radius)
    circumferenceOfCircle(radius)
    print(f"the area of the circle is {areaOfCircle(radius):.3f}, the circumference of the circle is {circumferenceOfCircle(radius):.3f}")
#circleInfo()
    
def drawBlockOfStars(width,height):
    line = "*"*width
    for i in range(0,height):
        print(line)
#drawBlockOfStars(5,3)

def drawLetterE():
    drawBlockOfStars(8,2)
    drawBlockOfStars(2,2)
    drawBlockOfStars(5,2)
    drawBlockOfStars(2,2)
    drawBlockOfStars(8,2)

def distanceBetweenPoints(p1,p2):
    p1 = Point()
    p2 = Point()
    
