from itertools import permutations 

def print_permutations(s):
    perm = list(permutations(s))
    for permutation in perm: 
        print(str().join(permutation), end = " ")
        
s = input()
print_permutations(s)