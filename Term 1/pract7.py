from graphics import *
import time

def getName():
    while True:
        name = input("Enter name: ")
        if name.isalpha():
            return name
#getName()

def trafficLights():
    win = GraphWin("traffic lights",300,300)
    box = Rectangle(Point(100,50),Point(200,250))
    box.setFill("black")
    box.draw(win)
    boxTwo = Rectangle(Point(110,60),Point(190,240))
    boxTwo.setFill("grey")
    boxTwo.draw(win)
    red = Circle(Point(150, 100), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(150, 150), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(150, 200), 20)
    green.setFill("black")
    green.draw(win)
    while True:
        red.setFill("red")
        amber.setFill("black")
        green.setFill("black")
        time.sleep(1)
        red.setFill("red")
        amber.setFill("yellow")
        time.sleep(1)
        red.setFill("black")
        amber.setFill("black")
        green.setFill("green")
        time.sleep(1)
        amber.setFill("yellow")
        green.setFill("black")
        time.sleep(1)
#trafficLights()
              
def gradeCoursework():
    while True:
        mark = input("Enter valid mark(0-20): ")
        if mark.isdigit():
            break
    grade = ("ABCFX")
    mark = int(mark)
    if 16<=mark<= 20:
        print (grade[0])
    elif 12 <= mark <= 15:
        print(grade[1])
    elif 8 <= mark <= 11:
        print(grade[2])
    elif 8 > mark:
        print(grade[3])
    else:
        print (grade[4])
#gradeCoursework()

def orderPrice():
    total = 0
    while True:
        unitPrice = input("Enter valid Price in pounds: £")
        if unitPrice.isdigit():
            break
    while True:
        quantityProduct = input("Enter valid Quantity of products: ")
        if quantityProduct.isdigit():
            break
    if unitPrice.isdigit() and quantityProduct.isdigit():
            cost = int(unitPrice) * int(quantityProduct)
            newCost = cost + total
    while True:
        moreProduct = input("Enter whether there are more products (y/n): ")
        if moreProduct == "n":
            break
        elif moreProduct == "y":
            orderPrice() 
    print(f"total cost is £{newCost}")    
orderPrice()
            
#while truing 3 questions
# if all above is yeppers, then output total and end
# if 2/3 yeppers then repeat the first two and increment
# if not appropiate yepper then repeat question
