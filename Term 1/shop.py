# def shoppingList():
#     numb = int(input("number of shopping items "))
#     totalItem = []
#     displayShoppingList(numb,totalItem)
#     deleteList(totalItem)
#     addList(totalItem)

# def displayShoppingList(numb,totalItem):
#      for i in range(0,numb):
#           item = input("Enter shopping item: ")
#           totalItem.append(item)
#      print(totalItem)

# def deleteList(totalItem):
#     totalItem.clear()
#     print (totalItem)

# def addList(totalItem):
#     totalItem.append("jim")
#     print(totalItem)

# shoppingList()

def userDetail():
    n = input("name: ")
    age = int(input("age: "))
    height = float(input("height: "))
    joemama = input("Enter your mama: ")
    printUserDetail(n,age,height,joemama)

def printUserDetail(n,age,height,joemama):
    print(f"your name: {n}, your age: {age}, your height: {height}, joemama: {joemama}")

    
userDetail()