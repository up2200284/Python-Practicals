import math
def areaOfRectangle():
    w = float(input("Enter a length (metres): "))
    l = float(input("Enter a value (metres): "))
    a = (w * l)
    print("the area is",a,"m^2")
areaOfRectangle()



def areaOfRectangle2():
    x1 = float(input("x1:"))
    y1 = float(input("y1:"))
    
    x2 = float(input("x2:"))
    y2 = float(input("y2:"))
    
    length = x2-x1
    width = y2-y1
    area = length * width
    print("the ara is ",area, " (metres squared)")
areaOfRectangle2()


def distanceBetweenPoints():
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    
    dx = x2-x1
    dy = y2-y1
    
    dxSq = dx*dx
    dySq = dy*dy
    
    added = dxSq + dySq
    
    d = math.sqrt(added)
    print("the distance is", d)
distanceBetweenPoints()


def slope():
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    
    dx = x2-x1
    dy = y2-y1
    
    slope = dy/dx
    print("slope: ",slope)
slope()

