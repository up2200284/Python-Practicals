#Exam
#write function biscuitCutting which inputs
#the diameter of each biscuit
#the number of each biscuits along the length of the mixture
#the number of biscuits along the width of the mixture
#output radius of each biscuit in cm
#output area of each biscuit in cm^2
#output total area of biscuit mixture (including spare) in cm^2
#output the highest number of complete biscuits that can be made from the spare mixture

from math import *

def biscuitCutting():
    diameter = float(input("Enter diameter of each biscuit in cm: "))
    numbBiscuitLength = int(input("Enter number of biscuit along the length of the mixture: "))
    numbBiscuitWidth = int(input("Enter number of biscuit along the width of the mixture: "))
    radius = diameter/2
    area = pi*radius**2
    biscuitMixture = diameter * numbBiscuitLength * numbBiscuitWidth
    print ("The radius of each biscuit is",radius,"cm")
    print ("The area of each biscuit is",area,"cm^2")
    print ("total area of the biscuit mixture",biscuitMixture,"cm^2")


#total 6/10

def biscuitCutting2():
    diameter = float(input("Enter diameter of each biscuit in cm: "))
    numbBiscuitLength = int(input("Enter number of biscuit along the length of the mixture: "))
    numbBiscuitWidth = int(input("Enter number of biscuit along the width of the mixture: "))
    
    radius = diameter/2
    print(radius)
    
    area = pi*radius**2
    print(area)
    
    length = numbBiscuitLength * diameter
    width = numbBiscuitWidth * diameter
    areaOfMixture = length * width
    print(areaOfMixture)
    
    totalBiscuitArea = area * numbBiscuitLength * numbBiscuitWidth
    spareBiscuitArea = areaOfMixture - totalBiscuitArea
    wholeBiscuit = spareBiscuitArea / area
    print (int(wholeBiscuit))
    