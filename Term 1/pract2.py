from math import *

def speedCalculator():
    distance = float(input("Enter distance in km: "))
    duration = float(input("Enter Journey in Hours: "))
    speed = distance/duration
    print ("Your speed was",speed,"km/h")

def circumferenceOfCircle():
    radius = float(input("Enter a radius value: "))
    circumference = pi*radius*2
    print("The circumference is",circumference)
    
def areaOfCircle():
    radius = float(input("Enter a radius value: "))
    area = pi*radius**2
    print("The area of a circle is",area)

def costOfPizza():
    diameter = float(input("Enter Diameter of Pizza in cm: "))
    area = (diameter/2)**2*pi
    cost = 0.035*area
    print("It costs: £",round(cost,2))

def slopeOfLine():
    x1 = float(input("Enter a value fo coordinate x1: "))
    y1 = float(input("Enter a value fo coordinate y1: "))
    x2 = float(input("Enter a value fo coordinate x2: "))
    y2 = float(input("Enter a value fo coordinate y2: "))
    slope = (y2-y1)/(x2-x1)
    print(slope)
    
def distanceBetweenPoints():
    x1 = float(input("Enter a value fo coordinate x1: "))
    y1 = float(input("Enter a value fo coordinate y1: "))
    x2 = float(input("Enter a value fo coordinate x2: "))
    y2 = float(input("Enter a value fo coordinate y2: "))
    distance = sqrt((x2-x1)**2+(y2-y1)**2)
    print(distance)
    
def travelStatistics():
    speed = float(input("Enter a speed value in km/h: "))
    duration = float(input("Enter duration of journey in hours: "))
    distance = speed*duration
    fuelUsed = distance/5
    print ("Distance travelled is",distance,"km")
    print ("Fuel used is",fuelUsed,"litres")

def sumOfSquares():
    x = 0
    numb = int(input("Enter an integer: "))
    for i in range(1,numb+1):
        x += i**2  
    print(x)

def averageOfNumbers():
    numbcount = int(input("how many numbers would you like to input"))
    sum = 0
    for i in range(1,numbcount + 1):
        sum += i
    average = sum/numbcount
    print (average)
averageOfNumbers()


def fibonacci():
    numb = int(input("Enter an integer: "))
    a = 0
    b = 1
    for _ in range(numb):
        print(a)
        c = a +b
        a = b 
        b=c
fibonacci()
    
def selectCoins():
    pence = int(input("Enter money in pence: "))
    pounds = pence /  100
    print(pounds)

