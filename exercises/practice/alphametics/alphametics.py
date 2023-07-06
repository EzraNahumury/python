from itertools import permutations
from re        import findall
def word_value(word,asolution):
    return sum(asolution[x]*10**ix for ix,x in enumerate(word))
def solve(inputs):
    letters = set(findall(r'(\w)',inputs))
    notzero = set(findall(r'(\w)\w*',inputs))
    l_nz    = len(notzero)
    letters = list(letters - notzero) + list(notzero)
 
    inputs  = inputs.replace('+',',').replace('==',',').replace(' ','')
    Linputs = inputs.split(',')
    Linputs = [x[::-1] for x in Linputs]
    
    for p in permutations(range(0,10),len(letters)):
        if 0 in p[-l_nz:]:
            continue
        asolution = dict(zip(letters, p))
        if sum(word_value(word,asolution) for word in Linputs[:-1]) == word_value(Linputs[-1],asolution):
            return asolution
    return {}
