def word_count(sentence):
    from string import punctuation

    #clearing punctuation
    for char in sentence:
        if char in punctuation: 
            sentence = sentence.replace(char,' ')

    sentence = sentence.lower().split()
    wordCount = {}

    for word in sentence:
        if word in wordCount.keys():
            wordCount[word] += 1
        else: wordCount[word] = 1

    return wordCount


print word_count('hello @my name is youssef Youssef youssef Youssef')