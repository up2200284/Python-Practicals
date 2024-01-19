from graphics import *

chosenColor = []

#user input
def userInput():
    while True:
        patchSize = input("Enter patch work size(valid sizes are 5,7,9): ")
        if patchSize in ['5','7','9']:
            colorPattern()
            break
        elif patchSize.isdigit():
            print("Invalid integer value ")
        elif patchSize.isalpha():
            print("Input is not an integer ")
        else:
            print("Invalid input, enter 5 or 7 or 9 ")

#valid colour input
def colorPattern():
     count = 0
     colorSet = ['red','green','blue','magenta','orange','yellow','cyan']
     while True:
        if count == 3:
            break
        colorChoice = input(f"Enter a valid colour (valid color are {colorSet}: ")
        if colorChoice in colorSet:
            count+=1
            colorSet.remove(colorChoice)
            chosenColor.append(colorChoice)
        elif colorChoice.isdigit():
            print("Input is not a colour ")
        elif colorChoice.isalpha():
            print("Invalid colour ")
        else:
            print("Invalid input, enter red,green,blue,magenta,orange,yellow,cyan")

# Running the user Input
def main():
    userInput()
main()

# Running the Graphics window
win = GraphWin("patch",500,500)
bgColors = ["white","orange","red"]

# H Shape of the penultimate design
def shapeMakeH(win,x,y,colorOne,colorTwo):
    rectangle = Rectangle(Point(x,y-100),Point(x+25,y-75))
    rectangle.setFill(colorOne)
    rectangle.setOutline(colorOne) 
    rectangle.draw(win)
    rectangleTwo = Rectangle(Point(x+5,y-100),Point(x+20,y-90))
    rectangleThree = Rectangle(Point(x+5,y-85),Point(x+20,y-75))
    rectangleTwo.setFill(colorTwo)
    rectangleThree.setFill(colorTwo)
    rectangleTwo.setOutline(colorTwo)
    rectangleThree.setOutline(colorTwo)
    rectangleTwo.draw(win)
    rectangleThree.draw(win)


# I Shape of the penultimate design
def shapeMakeI(win,x,y,colorOne,colorTwo):
    rectangle = Rectangle(Point(x,y-100),Point(x+25,y-75))
    rectangle.setFill(colorOne)
    rectangle.setOutline(colorOne) 
    rectangle.draw(win)
    rectangleTwo = Rectangle(Point(x,y-95),Point(x+10,y-80))
    rectangleThree = Rectangle(Point(x+15,y-95),Point(x+25,y-80))
    rectangleTwo.setFill(colorTwo)
    rectangleThree.setFill(colorTwo)
    rectangleTwo.setOutline(colorTwo)
    rectangleThree.setOutline(colorTwo)
    rectangleTwo.draw(win)
    rectangleThree.draw(win)

#patch background color
def backgroundColor(win,x,y,chosenColor):
     bg = Rectangle(Point(x,y),Point(x+100,y+100))
     bg.setFill(chosenColor)
     bg.draw(win)

#final design
def drawPatchFinal(x,y,radius,win,chosenColor):
    for i in range(10):
        circle = Circle(Point(x-50,y+50),radius)
        circle.setOutline(chosenColor)
        circle.draw(win)
        y += 5
        radius -=5

#Applying First user colour Input
def designColourOne():
    x=0
    y=0
    count = 0
    for columns in range(x,x+500,x+100): #makes the whole page go first colour
            for rows in range(y,y+500,y+100):
                 while count < 5:
                     backgroundColor(win,x,y,chosenColor[2])
                     x+=100
                     count +=1   
            x=0
            y+=100
            count = 0
designColourOne()

#Second user Input Color
def designColourTwo():
    x = 0
    y=0
    count = 0
    for columns in range(x,x+500,x+100): #diagonal second colour and final design on top of the first colour
            for rows in range(y,y+500,y+100):
                while count < 5:
                 backgroundColor(win,x,y,"white")
                 drawPatchFinal(x+100,y,50,win,chosenColor[0])
                 x+=100
                 count +=5
            y+=100
            count=0
designColourTwo()

#Third user Input Color
def designColourThree():
    x=0
    y=0
    for columns in range(x,x+500,x+100): #places third colour on top of all previous colours and any final designs as well
            for rows in range(y,y+500,y+100):
                 if x == 200 and y == 100:
                      backgroundColor(win,x,y,chosenColor[1])
                 x+=100
                 if 200 <= x <= 500 and y == 0:
                      backgroundColor(win,x,y,"white")
                      drawPatchFinal(x,y,50,win,chosenColor[1])
                 if 200 <= x <= 500 and y == 100:
                      backgroundColor(win,x,y,chosenColor[1])
                 if 300 <= x <= 500 and y == 200:
                      backgroundColor(win,x,y,chosenColor[1])
                 if 400 <= x <= 500 and y == 300:
                      backgroundColor(win,x,y,chosenColor[1])
                 if x == 100 and y == 0:
                     backgroundColor(win,x,y,"white")
                 if x == 400 and y < 400:
                     backgroundColor(win,x,y,"white")
                     drawPatchFinal(x+100,y,50,win,chosenColor[1])
            y+=100
            x=200 
designColourThree()

#combining the penultimate design
def penUltimateDesign(win,x,y):
    count = 0
    colorBoolean = True
    for columns in range(x,x+100,25):
            for rows in range(y,y+25,25):
                 while count < 4:
                    if count % 2 == 0 and colorBoolean:
                        shapeMakeH(win,x,y,chosenColor[2],"white")
                        x += 25
                        count +=1
                    elif count % 2 == 0 and not colorBoolean:
                        shapeMakeH(win,x,y,"white",chosenColor[2])
                        x += 25
                        count +=1
                    elif count %2 == 1 and colorBoolean:
                        shapeMakeI(win,x,y,chosenColor[2],"white")
                        x+=25
                        count +=1
                    elif count % 2 == 1 and not colorBoolean:
                        shapeMakeI(win,x,y,"white",chosenColor[2])
                        x += 25
                        count +=1
                 count =0
                 x-=100
                 y+=25
            colorBoolean = not colorBoolean





#100x100 grid covers penultimate design
def grid(win,x,y):
    count = 0
    while count < 5 :
        line = Line(Point(x,y-100),Point(x,y))
        line.setFill("black")
        line.draw(win)
        x += 25
        count += 1
    while count != 10:
        line = Line(Point(x-125,y-100),Point(x-25,y-100))
        line.setFill("black")
        line.draw(win)
        y += 25
        count +=1

#500x500grid covers whole map
def gridTwo(win):
    x = 100
    y = 100
    count = 1
    while count != 5 :
        line = Line(Point(x,y-100),Point(x,y+400))
        line.setFill("black")
        line.draw(win)
        x += 100
        count += 1
    while count != 10:
        line = Line(Point(x-600,y),Point(x,y))
        line.setFill("black")
        line.draw(win)
        y += 100
        count +=1
gridTwo(win)

#applies penultimate design to the locations
def penUltimatePattern():
    x = 100
    y = 300
    for columns in range(x,x+400,x):
        for rows in range(y,y+300,y-100):
            if x == 100 and y == 300:
                penUltimateDesign(win,x,y)
                grid(win,x,y)
            if x == 100 and y == 400:
                penUltimateDesign(win,x,y)
                grid(win,x,y)
            if x == 200 and y == 400:
                penUltimateDesign(win,x,y)
                grid(win,x,y)
            y+= 100
        x+=100
        y-=100
penUltimatePattern()

#keeps the graphics window open until you click on it.
win.getMouse()

