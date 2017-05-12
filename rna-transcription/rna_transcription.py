def to_rna(dna):
    def repl(strand):
        if strand == 'G': return 'C'
        elif strand == 'C': return 'G'
        elif strand == 'T': return 'A'
        elif strand == "A": return 'U'
        else: return 'X'
    
    word = ''.join (repl(e) for e in dna);

    return word if 'X' not in word else ''

print to_rna('ACGTXXXCTTAA')
