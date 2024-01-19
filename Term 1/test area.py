def fastFoodOrderPrice():
    orderCost = float(input("Enter cost: "))
    if orderCost>=20:
        orderCost += 2.50
    print(f"The total price of your order is £{orderCost:.2f}")
#fastFoodOrderPrice()

def whatToDoToday():
    userTemp = float(input("Enter temperature of today: "))
    if userTemp > 25:
        print("a swim in the sea is recommended")
    elif 10 <= userTemp <= 25:
        print("shopping in Gunwharf Quays is a good idea")
    else:
        print ("it's best to watch a film at home")
whatToDoToday()