from graphics import *
import os

def personalGreeting():
    greetUser = input("Enter your name: ")
    print(f"Hello {greetUser}, nice to meet you!")
#personalGreeting()

def formalName():
    givenName = input("Enter your given name: ")
    familyName = input("Enter your family name: ")
    formalName = f"{givenName[0]}. {familyName}"
    print(formalName)
#formalName()

def kilos2Ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = kilos * 35.274
    print(f"{kilos} kilos is equal to {ounces:.2f} ounces")
kilos2Ounces()

def generateEmail():
    firstName = input("enter firstname ")
    lastName = input("enter surname ")
    yearEntry = input("enter the year you joined university ")
    Email = f"{lastName[0:4]}.{firstName[0]}.{yearEntry[-2:]}@myport.ac.uk"
    print (Email)
#generateEmail()

def gradeTest():
    mark = int(input("Enter mark between 0 and 10 "))
    grades="FFFFCCBBAAA"
    print(grades[mark])
#gradeTest()
    
def graphicLetters():
    wordEnter = input("Enter a word: ")
    win = GraphWin("graphicLetters",500,500)
    for letter in range(len(wordEnter)):
        p = win.getMouse()
        text = Text(p,wordEnter[letter])
        text.setSize(24)
        text.draw(win)
#graphicLetters()


def singASong():
    songWord = input("Enter song word ")
    songRow = int(input("How many times should the word be repeated in a line "))
    songColumn = int(input("How many lines does it have "))
    songWord = songWord + " "
    songLine = songWord*songRow
    for i in range(0,songColumn):
        print(songLine)
#singASong()

def exchangeTable():
    pound = 0
    euro = 0
    for i in range(21):
        print(f"€{euro:2} | £{pound:5.2f}")
        euro = euro + 1
        pound = round((euro/1.17),2)
exchangeTable()

def makeInitialism():
    sentence = input("Enter a sentence: ")
    newSentence = " "
    
    for word in sentence.split():
        capitalizedLetter = f"{word[0].upper()}"
        newSentence = newSentence + capitalizedLetter
    print(newSentence)
#makeInitialism()

def nameToNumber():
    name = input("Enter name: ")
    value = 0
    for letter in name:
        value = value + ord(letter) - 96
    print(value)
#nameToNumber()

def fileInCaps():
    os.chdir("textFiles")
    name = input("Enter file name: ")
    textFile = name + ".txt"
    inFile = open(textFile, "r")
    contents = inFile.read()
    upperContents = contents.upper()
    print (upperContents)
    inFile.close()
#fileInCaps()

def totalSpending():
    os.chdir("textFiles")
    inFile = open("spending.txt", "r")
    line = inFile.readline()
    sum = 0
    for line in inFile:
        sum += float(line)
    print(f"£{sum}")
    inFile.close()
#totalSpending()

def rainfallChart():
    os.chdir("textFiles")
    inFile = open("rainfall.txt", "r")
    for line in inFile:
        word = line.split()
        name = word[0]
        num = int(word[1])
        print(f"{name} {'*'*num}")
    inFile.close()
#rainfallChart()

def graphicalRainFallChart():
    os.chdir("textFiles")
    inFile = open("rainfall.txt", "r")
    y = 50
    win = GraphWin("Graphical Rainfall Chart", 700,500)
    for line in inFile:
        word = line.split()
        name = word[0]
        blocks = int(word[1])
        for i in range(blocks):
            top_left = Point((i*10) +110,y)
            bottom_right = Point ((i*10) +120,y +10)
            rec = Rectangle (top_left,bottom_right)
            rec.setFill("blue")
            rec.draw(win)
            message = Text(Point(50,y+3),name)
            message.draw(win)
        y +=20
    win.getMouse()   
    inFile.close()
#graphicalRainFallChart()

def rainfallInInches():
    os.chdir("textFiles")
    inFile = open("rainfall.txt", "r")
    for line in inFile:
        word = line.split()
        name = word[0]
        num = ((float(word[1]))/25.4)
        outFile = open("rainfallInches.txt", "a")
        outFile.writelines(f"{name} {num:.2f}\n")
    inFile.close()
    outFile.close()
#rainfallInInches()

def wc():
    os.chdir("textFiles")
    file = input("Enter a text file: ")
    file = file+".txt"
    inFile = open(file, "r")
    content = inFile.read()
    lines = content.split('\n')
    words = content.split()
    lineCount = len(lines)
    wordCount = len(words)
    charCount = len(content)

    print(f"Characters: {charCount}")
    print(f"Words: {wordCount}")
    print(f"Lines: {lineCount}")
wc()