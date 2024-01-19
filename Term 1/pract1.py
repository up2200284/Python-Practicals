def sayHello():
    print("Hello World")
sayHello()

def sayBye():
    print("Goodbye Mars")
sayBye()


# A simple kilograms to ounces conversion program
# It asks for a weight in kilograms (for example 10)
# and converts it to ounces (352.74)
def kilos2Ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = 35.274 * kilos
    print("The weight in ounces is", ounces)
#kilos2Ounces()

#count numbers from 0-9
def count():
    for number in range(10):
        print ("Number is now: ", number)
#count()

def sayHello2():
    print ("Hello")
    print ("World")
#sayHello2()

def dollars2Pounds():
    dollars = float(input("Enter money value in dollars "))
    pounds = 0.8 * dollars
    print("The dollars in pounds is £",pounds)
#dollars2Pounds()

def tenHellos():
    for i in range (10):
        print("Hello World")
#tenHellos()

def railFareIncrease():
    ticket = 16.5
    for i in range(11):
        ticket = ticket * 1.02
        print ("The Price of the ticket is £",ticket)
#railFareIncrease()

def countTo():
    numb = int(input("Enter a number: "))
    for numb in range(numb):
        print(numb + 1)
#countTo()

def countTo2():
    numb1 = int(input("Enter a number: "))
    numb2 = int(input("Enter a number: "))
    for i in range(numb1,numb2 + 1):
        print(i)
#countTo2()

def changeCounter():
    penny = int(input("Enter number of single pennies "))
    twoPence = int(input("Enter number of 2 pennies "))
    fivePence = int(input("Enter number of 5 pence "))
    total = penny + twoPence *2 + fivePence*5
    print ("you have",total,"pennies")
#changeCounter()

def weightsTable():
    print ("""Kgs | Ounces
 ==================
 ==================""")
    for i in range(10,60,10):
        print(i,"|",i * 35.274)
weightsTable()

def futureRailFare():
    numbInitialFare = float(input("Enter Initial Fare £"))
    numbMonths = int(input("Enter number of months "))
    for x in range(numbMonths):
        numbInitialFare = numbInitialFare * 1.02
        print (numbInitialFare)
#futureRailFare()
        