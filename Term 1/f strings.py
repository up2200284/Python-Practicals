def weightsTable2():
    print ("f{'Kgs':<5} | {'Ounces': <5}")
    for kilos in range (10, 60, 10):
        ounces = kilos * 35.274
        print (f"{kilos:<5} | {'Ounces': <5}")