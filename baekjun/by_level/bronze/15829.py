import sys

l = int(sys.stdin.readline())
word = list(map(ord, str(sys.stdin.readline().rstrip())))
wordint = [0]*l

def ABmodC(a, b, c):
    binb = bin(b)[2:]
    modc = [0]*len(binb)
    modc[0] = a%c
    for i in range(1, len(binb)):
        modc[i] = (modc[i-1]*modc[i-1])%c

    res = 1
    for i in range(len(binb)):
        if int(binb[-1-i]):
            res *= (modc[i])
            res %= c
    return res

hashres = 0

r, m = 31, 1234567891
for i in range(l):
    hashres += (word[i]-96) * ABmodC(r, i, m)
    hashres %= m
print(hashres)







