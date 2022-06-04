import sys
import random
from itertools import combinations

def make_testcase():
    N = random.randint(1, 100)
    maxnode = N*(N-1)//2
    M = random.randint(1, maxnode)

    l = list(combinations([i for i in range(1, N+1)], 2))
    combi = random.sample(l, M)
    tc = "%d %d\n"%(N, M)
    for i in range(M):
        tc += "%d %d %d\n"%(combi[i][0], combi[i][1], random.randint(1, 10_000))
    return tc

f = open("test_input.txt", "w")
for _ in range(1):
    a = make_testcase()
    f.write(a)
f.close()

