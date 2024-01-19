from graphics import *

def q1():
    sentence = input("please enter sentence ")

    words = sentence.split(" ")
    
    for word in words:
        print(word)
#q1()

def q2 ():

    sentence = input("please enter sentence: ")
    
    win = GraphWin("words on a screen", 500, 500)
    x = 10
    y = 10
    

    for i in range(len(sentence)):
         win.getMouse()
         x = x + 10
         p = Point(x,y)
         text = Text(p,sentence[i])

         text.draw(win)

#q2()

def q3():

    win = GraphWin("question3", 500, 500)

    colours = ["blue", "red"]
    i = 0
    for x in range(0,500,100):
        for y in range (0,500,100):
            if i>1:
                i =0
            win.getMouse()
            top_left = Point(x,y)
            bottom_right = Point (x+100, y +100)
            rec = Rectangle (top_left,bottom_right)
            rec.setFill(colours[i])
            rec.draw(win)
            i += 1
#q3()

def q4():
    win = GraphWin("question3", 500, 500)
    colours = ["blue"]
    for y in range (50,140,10):
        for x in range(50,500,10):
            win.getMouse()
            top_left = Point(x,y)
            bottom_right = Point (x+10, y +10)
            rec = Rectangle (top_left,bottom_right)
            rec.setFill(colours)
            rec.draw(win)
#q4()