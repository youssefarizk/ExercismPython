import string

def detect_anagrams(actual, candidates):
    
    def anagram(original, check):
        checkVal = check
        check = check.lower()
        original = original.lower()
        if original == check: return ''
        while len(check) != 0:
            #print (original + ' ' + check)
            if original.find(check[0]) == -1:
                return ''
            elif original == '':
                return ''
            else:
                original = original.replace(check[0],'',1)
                check = check.replace(check[0],'',1)
        return checkVal if len(original) == 0 else ''

    anagramList = map(lambda x: anagram(actual,x), candidates)

    return [e for e in anagramList if e != '']

print detect_anagrams('orchestra', ["cashregister", "Carthorse", "radishes"])