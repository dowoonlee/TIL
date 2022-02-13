import sys
from collections import deque

n = int(sys.stdin.readline())
dna = deque(list(str(sys.stdin.readline().rstrip())))

dna_order = {'AG' : 'C', 'AC' : 'A', 'AT' : 'G',
             'GA' : 'C', 'GC' : 'T', 'GT' : 'A',
             'CA' : 'A', 'CG' : 'T', 'CT' : 'G',
             'TA' : 'G', 'TG' : 'A', 'TC' : 'G'}



for i in range(n-1, 0, -1):
    if dna[i]==dna[i-1]:
        dna.pop()
    else:
        temp = dna.pop()
        temp += dna.pop()
        dna.append(dna_order[temp])
print(dna[0])