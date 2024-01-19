number = 8

def isEven(number):
    return number % 2 == 0


def reverse(word, length):
    if len(word) <= length:
        return
    result = ""
    for ch in word:
        result = ch + result
    return result

temp = float(input("enter a temperature: "))

if temp < 20:
    print("heat")
elif temp < 23:
    print("nothing")
elif temp < 25:
    print("fan")
else:
    print("cooling")