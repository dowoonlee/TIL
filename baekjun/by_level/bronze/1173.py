import sys

N, m, M, T, R = map(int, sys.stdin.readline().split())


if m+T>M:
    print(-1)
else:
    pres = m+0
    ptime = 0
    time = 0

    while ptime < N:
        print(pres, time, ptime)
        if pres+T<=M:
            pres += T
            time += 1
            ptime += 1
        else:
            if pres-R<m:
                pres = m
            else:
                pres -= R
            time += 1
    print(time)
