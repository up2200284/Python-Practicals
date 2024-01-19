from graphics import *

def letterWriter():
    win = GraphWin("Stick figure", 300, 200)
    
    #head
    head = Circle(Point(200, 60), 20)
    head.draw(win)
    
    #body
    body = Line(Point(200, 80), Point(200, 120))
    body.draw(win)
    
    #left arm
    arm1 = Line(Point(200, 90), Point(160, 80))
    arm1.draw(win)
    
    #right arm
    arm2 = Line(Point(200, 90), Point(240, 80))
    arm2.draw(win)
    
    #left leg
    leg1 = Line(Point(200, 120), Point(170, 170))
    leg1.draw(win)
    
    #right leg
    leg2 = Line(Point(200, 120), Point(230, 170))
    leg2.draw(win)
    
    #pen
    pen = Line(Point(165,75), Point(175,92))
    pen.draw(win)
    
    #large pad of paper
    paper = Rectangle(Point(20,30), Point(150,170))
    paper.draw(win)
    
    #hole1
    hole1 = Circle(Point(30,85),4)
    hole1.draw(win)
    
    #hole2
    hole2 = Circle(Point(30,120),4)
    hole2.draw(win)
    # test 6/10
#letterWriter()

def letterWriter2():
       win = GraphWin("Stick figure", 300, 200)

       #head
       head = Circle(Point(200, 60), 20)
       head.draw(win)
       
       #body
       body = Line(Point(200, 80), Point(200, 120))
       body.draw(win)
       
       #left arm
       arm1 = Line(Point(200, 90), Point(160, 80))
       arm1.draw(win)
       
       #right arm
       arm2 = Line(Point(200, 90), Point(240, 80))
       arm2.draw(win)
       
       #left leg
       leg1 = Line(Point(200, 120), Point(170, 170))
       leg1.draw(win)
       
       #right leg
       leg2 = Line(Point(200, 120), Point(230, 170))
       leg2.draw(win)
       
       #pen
       pen = Line(Point(165,75), Point(175,92))
       pen.draw(win)
       
       #large pad of paper
       paper = Rectangle(Point(20,30), Point(150,170))
       paper.draw(win)
       
       #hole1
       hole1 = Circle(Point(30,85),4)
       hole1.draw(win)
       
       #hole2
       hole2 = Circle(Point(30,120),4)
       hole2.draw(win)

       textX = 60
       textY = 45
       characters = "Hello!"
       for char in characters:
        win.getMouse()
        hello_text = Text(Point(textX, textY), char)
        hello_text.setSize(14)
        hello_text.draw(win)
        textX += 10
       win.getMouse()
       pen.move(-110,60)
       win.getMouse()
letterWriter2()

       
    
