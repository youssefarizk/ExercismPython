def slices(number, size):
    
    def stringToArr(subNumber):
        arr = []
        for char in subNumber:
            arr.append(int(char))
        return arr

    if len(number) < size or number == '' : raise ValueError('The size selected is larger than the length of the string')
    else:
        arr = []
        while len(number) >= size:
            arr.append(stringToArr(number[:size]))
            number = number[1:]
        return arr