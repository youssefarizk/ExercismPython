from string import ascii_lowercase

def encode(word):
    finWord = []
    count = 1
    for char in word.lower():
        if (count == 5):
            if char.isalpha():
                finWord.append(ascii_lowercase[25-ascii_lowercase.find(char)])
                finWord.append(' ')
                count = 1
            elif char.isdigit():
                finWord.append(char)
                finWord.append(' ')
                count = 1
        else:
            if char.isalpha():
                count += 1
                finWord.append(ascii_lowercase[25-ascii_lowercase.find(char)])
            elif char.isdigit():
                count += 1
                finWord.append(char)                
    
    return ''.join(finWord).rstrip()
        


def decode(word):
    wordList = word.split()
    decodedWord = []

    def replace(x,lst):
        if x.isalpha(): lst.append(ascii_lowercase[25-ascii_lowercase.find(x)])
        elif x.isdigit():lst.append(x)
            

    for segment in wordList:
        map(lambda x: replace(x, decodedWord),segment)
    return ''.join(decodedWord)


print encode('mindblowingly')