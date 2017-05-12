def is_isogram(word):
    
    countDictionary = {}

    def letters(input):
        valids = []
        for character in input:
            if character.isalpha():
                valids.append(character)
        return ''.join(valids)

    word = letters(word).lower()

    isogram = True

    for char in word:
        if countDictionary.has_key(char):
            isogram = False
        else:
            countDictionary[char] = 0
    
    return isogram


print(set("Hello World"))
