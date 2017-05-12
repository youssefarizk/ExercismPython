def decode(sequence):
    
    def segmentOfSeq(word):
        finString = []
        for char in word:
            if (finString == []) :
                finString.append(char)
            elif finString[-1].isdigit():
                finString.append(char)
            else: break
        return ''.join(finString)
    
    indSegments = []
    while (len(sequence) != 0):
        segment = segmentOfSeq(sequence)
        indSegments.append(segment)
        sequence = sequence[len(segment):]

    def indDecode(seg):
        letter = seg[-1]
        number = int(seg[0:-1]) if len(seg[0:-1]) != 0 else 1
        equ = []
        for i in range(number):
            equ.append(letter)

        return ''.join(equ)

    return ''.join(indDecode(i) for i in indSegments)
        

def encode(sequence):
    def counter(char,word):
        count = 0
        for chars in word:
            if chars == char: count += 1
            else: break
        return count

    def stringFormatter(char,word):
        count = counter(char, word)
        if count == 1: return char
        else: return str(count) + char

    #function to remove duplicates for the purposes of iterationr
    def removeDup(seq):
        single = []
        for chars in seq:
            if single == [] or chars != single[-1]:
                single.append(chars)
        return ''.join(single)
    
    decodeSequence = []
    for chars in removeDup(sequence):
        decodeSequence.append(stringFormatter(chars, sequence))
        sequence = sequence[counter(chars, sequence):]

    return ''.join(decodeSequence)
