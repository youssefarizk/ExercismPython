from string import ascii_lowercase, ascii_uppercase

def rotate(word, key):
    key = key%26
    newWord = []
    for char in word:
        if char.isalpha():
            if char.islower(): char = ascii_lowercase[(ascii_lowercase.find(char)+key)%26]
            else: char = ascii_uppercase[(ascii_uppercase.find(char)+key)%26]
        newWord.append(char)

    return ''.join(newWord)