def distance(dna1, dna2):
    if len(dna1) != len(dna2): 
        raise ValueError()
    else:
        count = 0
        for index in range(len(dna1)):
            if dna1[index] != dna2[index]:
                count += 1
        
        return count