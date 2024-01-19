def reversed(word):
    reversed = ""
    for ch in word:
        reversed = ch + reversed
    return reversed