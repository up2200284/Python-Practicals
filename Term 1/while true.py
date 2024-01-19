import random

def addNumbers():
    sum = 0
    userInput = input("Enter a number: ")
    while userInput != "q":
        sum+=int(userInput)
        userInput = input("Enter a number: ")

    print(sum)
#addNumbers()


def addNumbersVersion2():
    sum = 0
    while True:
        userInput = input("Enter a number: ")
        if userInput == "q":
            break
        sum += int(userInput)

    print(sum)

#addNumbersVersion2()

def randomGame():
    numb = random.randint(1,10)
    userNumb = int(input("Enter number: "))
