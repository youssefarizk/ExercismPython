def is_pangram(word):
    import string
    wordList = map(lambda x: x in word.lower(), list(string.ascii_lowercase))
    return False not in wordList


