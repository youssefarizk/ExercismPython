def abbreviate(word):
    finString = ''
    prevChar = ''
    for char in word:
        if (char.isupper() & ~(prevChar.isupper())) | ((prevChar == ' ') | (prevChar == '-')):
            finString += char
        prevChar = char
    return finString.upper()