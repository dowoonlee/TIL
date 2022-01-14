import sys
#n = int(sys.stdin.readline())

n = 1300

d = 4
dd = 20
while dd<=n:
    d+=1
    dd += (d-3)*(9**(d-4)*10) + 10**(d-3)

n0 = n-(dd - (d-3)*(9**(d-4)*10) - 10**(d-3))
d_add = d-3
add = ['%04d'%i for i in range(10**d_add)]

sixes = []
six = '666'
for i in add:
    sixes.append(int(i+'666'))
    for j in range(len(i)):
        sixes.append(int(i[0:j]+'666'+i[j::]))

sixes = sorted(list(set(sixes)))
for i in range(n):
    print('%03d:'%(i+1), sixes[i])
