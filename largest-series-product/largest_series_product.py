import string

def largest_product(numString, div):
    
    def checkSanity():
        if div > len(numString): raise ValueError
        elif div < 0: raise ValueError
        elif (numString == "") & (div != 0): raise ValueError
        elif ''.join([e for e in numString if e.isdigit()]) != numString: raise ValueError
    
    def computeProduct(numb):
        prod = 1
        for char in numb:
            prod = prod * int(char)
        return prod
    
    checkSanity()

    max = 0

    for i in range(len(numString) - div + 1):
        prod = computeProduct(numString[i:i+div])
        if prod > max: max = prod

    return max

