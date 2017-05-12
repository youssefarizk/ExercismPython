def sum_of_multiples(numb, lst):
    unionLst = []
    
    for member in lst:
        tempList = [e for e in range(numb) if e%member == 0]
        unionLst = list(set(unionLst + tempList))

    return sum(unionLst)