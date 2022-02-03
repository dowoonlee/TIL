import sys

a0 = int(sys.stdin.readline())
nmax, ans = 0, 0

if a0 == 1:
    print(4)
    print('1 1 0 1')

else:

    for i in range(1, a0):
        j = [a0, a0-i]
        while j[-2]-j[-1]>=0:
            j.append(j[-2]-j[-1])
        if len(j)>=nmax:
            nmax = len(j)
            ans = i

    print(nmax)

    j = [a0, a0-ans]
    while j[-2] - j[-1] >= 0:
        j.append(j[-2] - j[-1])
    for i, jj in enumerate(j):
        if i==len(j)-1:
            print(jj)
        else:
            print(jj, end=' ')