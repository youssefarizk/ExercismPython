def sieve(numb):
    if numb < 2: return []
    numbList = range(numb+1)[2:]
    numbDic = dict(map(lambda x: (x, True), numbList))
    for entry in numbDic:
        if numbDic[entry] == True:
            for multiple in range(2*entry,numb+1,entry): numbDic[multiple] = False
    return [e for e in numbDic if numbDic[e] == True]

print sieve(5)